---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: cs
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/csharp.py\"\
    , line 231, in bundle\n    _check_env(path)\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/csharp.py\"\
    , line 89, in _check_env\n    _check_embedded_existing(_resolve_csproj(path))\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/csharp.py\"\
    , line 80, in _check_embedded_existing\n    subprocess.check_output(command)\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/subprocess.py\"\
    , line 420, in check_output\n    return run(*popenargs, stdout=PIPE, timeout=timeout,\
    \ check=True,\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/subprocess.py\"\
    , line 524, in run\n    raise CalledProcessError(retcode, process.args,\nsubprocess.CalledProcessError:\
    \ Command '['dotnet', 'build', '/home/runner/work/verification-helper/verification-helper/examples/csharpsx/Library/Library.csproj',\
    \ '-p:BaseIntermediateOutputPath=/home/runner/work/verification-helper/verification-helper/.verify-helper/cache/dotnet/obj/']'\
    \ returned non-zero exit status 1.\n"
  code: "\uFEFFusing System;\n\nnamespace Library\n{\n    public static partial class\
    \ HelloWorld\n    {\n        private const string Text = \"Hello World\";\n  \
    \  }\n}\n"
  dependsOn: []
  isVerificationFile: false
  path: examples/csharpsx/Library/HelloWorld.const.cs
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: examples/csharpsx/Library/HelloWorld.const.cs
layout: document
redirect_from:
- /library/examples/csharpsx/Library/HelloWorld.const.cs
- /library/examples/csharpsx/Library/HelloWorld.const.cs.html
title: examples/csharpsx/Library/HelloWorld.const.cs
---
