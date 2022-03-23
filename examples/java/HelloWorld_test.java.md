---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: examples/java/HelloWorld.java
    title: examples/java/HelloWorld.java
  _extendedRequiredBy:
  - icon: ':x:'
    path: examples/java/HelloWorld.java
    title: examples/java/HelloWorld.java
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: java
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/user_defined.py\"\
    , line 68, in bundle\n    raise RuntimeError('bundler is not specified: {}'.format(str(path)))\n\
    RuntimeError: bundler is not specified: examples/java/HelloWorld_test.java\n"
  code: "// verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A\n\
    package examples.java;\nimport examples.java.HelloWorld;\n\npublic class HelloWorld_test\
    \ {\n    public static void main(String[] args) {\n        System.out.println(HelloWorld.getHelloWorld());\n\
    \    }\n}\n"
  dependsOn:
  - examples/java/HelloWorld.java
  isVerificationFile: true
  path: examples/java/HelloWorld_test.java
  requiredBy:
  - examples/java/HelloWorld.java
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: examples/java/HelloWorld_test.java
layout: document
redirect_from:
- /verify/examples/java/HelloWorld_test.java
- /verify/examples/java/HelloWorld_test.java.html
title: examples/java/HelloWorld_test.java
---
