# Python Version: 3.x
import distutils.version
import functools
import json
import os
import pathlib
import shutil
import subprocess
import xml.etree.ElementTree as ET
from logging import getLogger
from typing import *

import onlinejudge_verify.languages.special_comments as special_comments
from onlinejudge_verify.config import get_config
from onlinejudge_verify.languages.models import Language, LanguageEnvironment

logger = getLogger(__name__)


@overload
def check_output(command: List[str], *, text: Literal[True]) -> str:
    ...


@overload
def check_output(command: List[str], *, text: Literal[False]) -> bytes:
    ...


@overload
def check_output(command: List[str]) -> bytes:
    ...


def check_output(command: List[str], *, text: bool = False) -> Union[bytes, str]:
    try:
        return subprocess.check_output(command, text=text)
    except (subprocess.CalledProcessError) as e:
        logger.error('raise subprocess.CalledProcessError')
        logger.info(' stdout: %s', e.stdout)
        logger.info(' stderr: %s', e.stderr)
        raise


@functools.lru_cache(maxsize=1)
def _check_dotnet_version() -> None:
    if not shutil.which('dotnet'):
        raise RuntimeError('`dotnet` not in $PATH')
    command = ['dotnet', '--version']
    logger.info('$ %s', ' '.join(command))
    res = check_output(command, text=True).strip()
    logger.info('dotnet version: %s', res)
    if distutils.version.LooseVersion(res) <= distutils.version.LooseVersion("6"):
        raise RuntimeError("oj-verify needs .NET 6 SDK or newer")


@functools.lru_cache(maxsize=1)
def _check_expander_console() -> None:
    if not shutil.which('dotnet-source-expand'):
        raise RuntimeError('`dotnet-source-expand` not in $PATH. Run `dotnet tool install -g SourceExpander.Console`')
    command = ['dotnet-source-expand', 'version']
    logger.info('$ %s', ' '.join(command))
    res = check_output(command, text=True).strip()
    logger.info('dotnet-source-expand version: %s', res)
    if distutils.version.LooseVersion(res) < distutils.version.LooseVersion("5"):
        raise RuntimeError('`dotnet-source-expand` version must be 5.0.0 or newer. Update SourceExpander.Console. `dotnet tool update -g SourceExpander.Console`')


class EmbeddedLibrary:
    def __init__(self, name: str, version: str) -> None:
        self.name = name
        self.version = version

    def __repr__(self) -> str:
        return 'EmbeddedLibrary("%s", "%s")' % (self.name, self.version)


@functools.lru_cache(maxsize=None)
def _list_embedded(csproj_path: pathlib.Path) -> List[EmbeddedLibrary]:
    _check_expander_console()
    if csproj_path is None or csproj_path.suffix != ".csproj":
        raise RuntimeError('csproj_path must be .csproj')
    command = ['dotnet-source-expand', 'library-list', str(csproj_path)]
    logger.info('$ %s', ' '.join(command))

    def enumerate_library(lines: List[str]):
        for line in lines:
            sp = line.split(',')
            if len(sp) >= 2:
                yield EmbeddedLibrary(sp[0], sp[1])

    res = list(enumerate_library(check_output(command, text=True).strip().splitlines()))
    logger.debug('libraries: %s', res)
    return res


@functools.lru_cache(maxsize=None)
def _check_embedded_existing(csproj_path: pathlib.Path) -> None:
    command = ['dotnet', 'build', str(csproj_path)]
    logger.info('$ %s', ' '.join(command))
    check_output(command)
    l = _list_embedded(csproj_path)
    if len(l) == 0:
        raise RuntimeError('Library needs SourceExpander.Embedder')


def _check_env(path: pathlib.Path):
    _check_dotnet_version()
    _check_expander_console()
    _check_embedded_existing(_resolve_csproj(path))


@functools.lru_cache(maxsize=None)
def _resolve_csproj(path: pathlib.Path) -> Optional[pathlib.Path]:
    path = path.resolve()
    if path.suffix == ".csproj":
        return path

    proj = next(path.glob("*.csproj"), None)
    if proj is not None:
        return proj

    if path == path.parent:
        return None
    return _resolve_csproj(path.parent)


class DependencyInfo:
    def __init__(self, filename: str, dependencies: List[str], typenames: Set[str]) -> None:
        self.filename = filename
        self.dependencies = dependencies
        self.defined_types = typenames

    def __repr__(self) -> str:
        return 'DependencyInfo("%s", %s, %s)' % (self.filename, self.dependencies, self.defined_types)


@functools.lru_cache(maxsize=None)
def _dependency_info_list(csproj_path: pathlib.Path) -> List[DependencyInfo]:
    _check_expander_console()
    _check_embedded_existing(csproj_path)
    if csproj_path is None or csproj_path.suffix != ".csproj":
        raise RuntimeError('csproj_path must be .csproj')

    command = ['dotnet-source-expand', 'dependency', '-p', str(csproj_path)]
    logger.info('$ %s', ' '.join(command))
    res = check_output(command)
    return json.loads(res, object_hook=lambda d: DependencyInfo(d['FileName'], d['Dependencies'], set(d['TypeNames'])))


@functools.lru_cache(maxsize=None)
def _dependency_info_dict(csproj_path: pathlib.Path) -> Dict[pathlib.Path, DependencyInfo]:
    deps: Dict[pathlib.Path, DependencyInfo] = dict()
    for d in _dependency_info_list(csproj_path):
        p = pathlib.Path(d.filename)
        if p.exists():
            deps[p] = d
    return deps


@functools.lru_cache(maxsize=None)
def _list_dependencies(path: pathlib.Path) -> List[pathlib.Path]:
    path = path.resolve()
    depinfo = _dependency_info_dict(_resolve_csproj(path))
    return [p for p in (pathlib.Path(dep) for dep in depinfo[path].dependencies) if p.exists()]


@functools.lru_cache(maxsize=None)
def _get_target_framework(csproj_path: pathlib.Path) -> str:
    root = ET.parse(csproj_path).getroot()
    target = root.findtext('.//TargetFramework')
    if target is None:
        raise RuntimeError('<TargetFramework> is not found')
    return target


class CSharpConfig:
    def __init__(self, config: Dict[str, Any]) -> None:
        root = config.get('languages', {}).get('csharp', {})
        self.static_embedding: Optional[str] = root.get('static_embedding', None)
        self.csproj_template: Optional[str] = root.get('csproj_template', None)


class CSharpLanguageEnvironment(LanguageEnvironment):
    def __init__(self, config: CSharpConfig) -> None:
        super().__init__()
        self.config = config

    @staticmethod
    def _write_default_project(output_file: pathlib.Path, target_framework: str) -> None:
        with open(output_file, 'w') as f:
            f.write('''<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>{}</TargetFramework>
  </PropertyGroup>
</Project>'''.format(target_framework))

    def _write_csproj(self, output_file: pathlib.Path, csproj_template_path: Optional[pathlib.Path], target_framework: str) -> None:
        if csproj_template_path is None:
            self._write_default_project(output_file, target_framework)
        elif not csproj_template_path.exists():
            logger.warning('%s is not found.', str(csproj_template_path))
            self._write_default_project(output_file, target_framework)
        else:
            shutil.copy(str(csproj_template_path), str(output_file))

    def _create_runner_project(self, code: bytes, target_framework: str, csproj_template_path: Optional[pathlib.Path], output_dir: pathlib.Path):
        os.makedirs(str(output_dir), exist_ok=True)
        self._write_csproj(output_dir / 'runner.csproj', csproj_template_path, target_framework)
        with open(output_dir / 'main.cs', 'wb') as f:
            f.write(code)

    def compile(self, path: pathlib.Path, *, basedir: pathlib.Path, tempdir: pathlib.Path) -> None:
        path = path.resolve()
        output_dir = tempdir / 'dotnet'
        _check_env(path)
        target_framework = _get_target_framework(_resolve_csproj(path))
        logger.info('build: TargetFramework = %s', target_framework)
        csproj_template_path = (basedir / pathlib.Path(self.config.csproj_template)) if self.config.csproj_template else None
        self._create_runner_project(self._expand_code(path), target_framework, csproj_template_path, output_dir)

        command = ['dotnet', 'build', str(output_dir / 'runner.csproj'), '-c', 'Release', '-o', str(output_dir / 'bin')]
        logger.info('$ %s', ' '.join(command))
        check_output(command)

    def get_execute_command(self, path: pathlib.Path, *, basedir: pathlib.Path, tempdir: pathlib.Path) -> List[str]:
        path = path.resolve()
        output_dir = tempdir / 'dotnet'
        path = path.resolve()
        _check_env(path)
        return [str(output_dir / 'bin' / 'runner')]

    @functools.lru_cache(maxsize=None)
    def _expand_code_dict(self, csproj_path: pathlib.Path) -> Dict[pathlib.Path, str]:
        _check_expander_console()
        command = ['dotnet-source-expand', 'expand-all', str(csproj_path)]
        if self.config.static_embedding:
            command.extend(['--static-embedding', self.config.static_embedding])
        logger.info('$ %s', ' '.join(command))
        json_res = check_output(command)
        return {pathlib.Path(t['FilePath']): t['ExpandedCode'] for t in json.loads(json_res)}

    @functools.lru_cache(maxsize=None)
    def _expand_code(self, path: pathlib.Path) -> bytes:
        _check_expander_console()
        csproj_path = _resolve_csproj(path)
        d = self._expand_code_dict(csproj_path)
        return d[path].encode('utf-8')


class CSharpLanguage(Language):
    def __init__(self) -> None:
        super().__init__()
        self.config = CSharpConfig(get_config())
        self.environment = CSharpLanguageEnvironment(self.config)

    def list_attributes(self, path: pathlib.Path, *, basedir: pathlib.Path) -> Dict[str, Any]:
        path = path.resolve()
        attributes: Dict[str, Any] = special_comments.list_special_comments(path)
        attributes.update(special_comments.list_doxygen_annotations(path))
        attributes.setdefault('links', [])
        attributes['links'].extend(special_comments.list_embedded_urls(path))
        return attributes

    def list_dependencies(self, path: pathlib.Path, *, basedir: pathlib.Path) -> List[pathlib.Path]:
        path = path.resolve()
        _check_env(path)
        return _list_dependencies(path)

    def bundle(self, path: pathlib.Path, *, basedir: pathlib.Path, options: Dict[str, Any]) -> bytes:
        path = path.resolve()
        _check_env(path)
        return self.environment._expand_code(path)

    def list_environments(self, path: pathlib.Path, *, basedir: pathlib.Path) -> Sequence[CSharpLanguageEnvironment]:
        return [self.environment]
