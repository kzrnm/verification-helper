---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: examples/csharpsx/Library/HelloWorld.const.cs
    title: examples/csharpsx/Library/HelloWorld.const.cs
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: examples/csharpsx/Tests/helloworld.test.cs
    title: examples/csharpsx/Tests/helloworld.test.cs
  _isVerificationFailed: true
  _pathExtension: cs
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/csharp.py\"\
    , line 254, in bundle\n    self.config.check_bundle_enable(_resolve_csproj(path))\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/csharp.py\"\
    , line 192, in check_bundle_enable\n    raise RuntimeError('project is not enable\
    \ to bundle')\nRuntimeError: project is not enable to bundle\n"
  code: "\uFEFFusing System;\n\nnamespace Library\n{\n    public static partial class\
    \ HelloWorld\n    {\n        public static void Hello() => Console.WriteLine(Text);\n\
    \    }\n}\n"
  dependsOn:
  - examples/csharpsx/Library/HelloWorld.const.cs
  isVerificationFile: false
  path: examples/csharpsx/Library/HelloWorld.cs
  requiredBy: []
  timestamp: '2022-03-17 03:43:02+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - examples/csharpsx/Tests/helloworld.test.cs
documentation_of: examples/csharpsx/Library/HelloWorld.cs
layout: document
redirect_from:
- /library/examples/csharpsx/Library/HelloWorld.cs
- /library/examples/csharpsx/Library/HelloWorld.cs.html
title: examples/csharpsx/Library/HelloWorld.cs
---
