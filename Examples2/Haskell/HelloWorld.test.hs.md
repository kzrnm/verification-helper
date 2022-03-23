---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: Examples2/Haskell/HelloWorld.hs
    title: Examples2/Haskell/HelloWorld.hs
  _extendedRequiredBy:
  - icon: ':x:'
    path: Examples2/Haskell/HelloWorld.hs
    title: Examples2/Haskell/HelloWorld.hs
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: hs
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/user_defined.py\"\
    , line 68, in bundle\n    raise RuntimeError('bundler is not specified: {}'.format(str(path)))\n\
    RuntimeError: bundler is not specified: Examples2/Haskell/HelloWorld.test.hs\n"
  code: "{- verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A\n\
    \ -}\nmodule Main where\nimport Examples2.Haskell.HelloWorld (helloWorld)\n\n\
    main :: IO ()\nmain = putStrLn helloWorld\n"
  dependsOn:
  - Examples2/Haskell/HelloWorld.hs
  isVerificationFile: true
  path: Examples2/Haskell/HelloWorld.test.hs
  requiredBy:
  - Examples2/Haskell/HelloWorld.hs
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: Examples2/Haskell/HelloWorld.test.hs
layout: document
redirect_from:
- /verify/Examples2/Haskell/HelloWorld.test.hs
- /verify/Examples2/Haskell/HelloWorld.test.hs.html
title: Examples2/Haskell/HelloWorld.test.hs
---
