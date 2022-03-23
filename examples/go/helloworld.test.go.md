---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: examples/go/helloworld.go
    title: examples/go/helloworld.go
  - icon: ':heavy_check_mark:'
    path: examples/go/helloworld/helloworld.go
    title: examples/go/helloworld/helloworld.go
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: examples/go/helloworld.go
    title: examples/go/helloworld.go
  - icon: ':heavy_check_mark:'
    path: examples/go/helloworld/helloworld.go
    title: examples/go/helloworld/helloworld.go
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: go
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/user_defined.py\"\
    , line 68, in bundle\n    raise RuntimeError('bundler is not specified: {}'.format(str(path)))\n\
    RuntimeError: bundler is not specified: examples/go/helloworld.test.go\n"
  code: "// verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A\n\
    \npackage main\n\nimport (\n    \"fmt\"\n    \"./helloworld\"\n)\n\nfunc main()\
    \ {\n    fmt.Printf(\"%s\\n\", helloworld.GetHelloWorld())\n}\n"
  dependsOn:
  - examples/go/helloworld/helloworld.go
  - examples/go/helloworld.go
  isVerificationFile: true
  path: examples/go/helloworld.test.go
  requiredBy:
  - examples/go/helloworld.go
  - examples/go/helloworld/helloworld.go
  timestamp: '2020-09-17 19:04:09+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: examples/go/helloworld.test.go
layout: document
redirect_from:
- /verify/examples/go/helloworld.test.go
- /verify/examples/go/helloworld.test.go.html
title: examples/go/helloworld.test.go
---
