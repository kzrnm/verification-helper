---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: examples/csharpsx/Library/HelloWorld.const.cs
    title: examples/csharpsx/Library/HelloWorld.const.cs
  - icon: ':x:'
    path: examples/csharpsx/Library/HelloWorld.cs
    title: examples/csharpsx/Library/HelloWorld.cs
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: cs
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A
    - https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/csharp.py\"\
    , line 254, in bundle\n    self.config.check_bundle_enable(_resolve_csproj(path))\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/csharp.py\"\
    , line 192, in check_bundle_enable\n    raise RuntimeError('project is not enable\
    \ to bundle')\nRuntimeError: project is not enable to bundle\n"
  code: "\uFEFF// verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A\n\
    \ninternal class helloworld\n{\n    public static void Main()\n    {\n       \
    \ Library.HelloWorld.Hello();\n    }\n}\n"
  dependsOn:
  - examples/csharpsx/Library/HelloWorld.const.cs
  - examples/csharpsx/Library/HelloWorld.cs
  isVerificationFile: true
  path: examples/csharpsx/Tests/helloworld.test.cs
  requiredBy: []
  timestamp: '2022-03-17 03:43:02+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: examples/csharpsx/Tests/helloworld.test.cs
layout: document
redirect_from:
- /verify/examples/csharpsx/Tests/helloworld.test.cs
- /verify/examples/csharpsx/Tests/helloworld.test.cs.html
title: examples/csharpsx/Tests/helloworld.test.cs
---
