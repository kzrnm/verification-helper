---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: cs
  _verificationStatusIcon: ':x:'
  attributes:
    IGNORE: ''
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
    \ Command '['dotnet', 'build', '/home/runner/work/verification-helper/verification-helper/examples/csharpsx/Tests/Tests.csproj',\
    \ '-p:BaseIntermediateOutputPath=/home/runner/work/verification-helper/verification-helper/.verify-helper/cache/dotnet/obj/']'\
    \ returned non-zero exit status 1.\n"
  code: "\uFEFFusing System;\nusing System.Reflection;\n// verification-helper: IGNORE\n\
    namespace Verifier\n{\n    public class LocalRunner\n    {\n        static void\
    \ Main(string[] args)\n        {\n            string verifier;\n            if\
    \ (args.Length == 0)\n            {\n                Console.WriteLine(\"Input\
    \ verifier name:\");\n                verifier = Console.ReadLine();\n       \
    \     }\n            else\n            {\n                verifier = args[0];\n\
    \            }\n            var type = Type.GetType(verifier);\n\n           \
    \ var method = type.GetMethod(\"Main\", BindingFlags.Static | BindingFlags.Public\
    \ | BindingFlags.NonPublic);\n            method.Invoke(null, null);\n       \
    \ }\n    }\n}\n"
  dependsOn: []
  isVerificationFile: true
  path: examples/csharpsx/Tests/_LocalRunner.test.cs
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: examples/csharpsx/Tests/_LocalRunner.test.cs
layout: document
redirect_from:
- /verify/examples/csharpsx/Tests/_LocalRunner.test.cs
- /verify/examples/csharpsx/Tests/_LocalRunner.test.cs.html
title: examples/csharpsx/Tests/_LocalRunner.test.cs
---
