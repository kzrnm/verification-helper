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
    , line 254, in bundle\n    self.config.check_bundle_enable(_resolve_csproj(path))\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/csharp.py\"\
    , line 192, in check_bundle_enable\n    raise RuntimeError('project is not enable\
    \ to bundle')\nRuntimeError: project is not enable to bundle\n"
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
  timestamp: '2022-03-17 23:37:21+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: examples/csharpsx/Tests/_LocalRunner.test.cs
layout: document
redirect_from:
- /verify/examples/csharpsx/Tests/_LocalRunner.test.cs
- /verify/examples/csharpsx/Tests/_LocalRunner.test.cs.html
title: examples/csharpsx/Tests/_LocalRunner.test.cs
---
