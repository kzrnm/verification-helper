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
    - https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A
    - https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A
    - https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A
  bundledCode: "using System;\ninternal class helloworld\n{\n    public static void\
    \ Main()\n    {\n        Library.HelloWorld.Hello();\n    }\n}\n#region Expanded\
    \ by https://github.com/kzrnm/SourceExpander\nnamespace Library { public static\
    \ partial class HelloWorld { private const string Text = \"Hello World\"; } }\n\
    namespace Library { public static partial class HelloWorld { public static void\
    \ Hello() => Console.WriteLine(Text); } }\n#endregion Expanded by https://github.com/kzrnm/SourceExpander\n"
  code: "\uFEFF// verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A\n\
    \ninternal class helloworld\n{\n    public static void Main()\n    {\n       \
    \ Library.HelloWorld.Hello();\n    }\n}\n"
  dependsOn:
  - examples/csharpsx/Library/HelloWorld.const.cs
  - examples/csharpsx/Library/HelloWorld.cs
  isVerificationFile: true
  path: examples/csharpsx/Tests/helloworld.test.cs
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: examples/csharpsx/Tests/helloworld.test.cs
layout: document
redirect_from:
- /verify/examples/csharpsx/Tests/helloworld.test.cs
- /verify/examples/csharpsx/Tests/helloworld.test.cs.html
title: examples/csharpsx/Tests/helloworld.test.cs
---
