---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: examples/debug/relative_path.hpp
    title: examples/debug/relative_path.hpp
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: examples/debug/relative_path.test.cpp
    title: examples/debug/relative_path.test.cpp
  _isVerificationFailed: true
  _pathExtension: hpp
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: '#line 2 "examples/debug/relative_path.hpp"

    char *hello = "Hello World";

    #line 4 "examples/debug/d/e/f/g/foo.hpp"

    '
  code: '#pragma once

    #include "../../../../relative_path.hpp"

    #include "./../../../.././a/b/../../relative_path.hpp"

    '
  dependsOn:
  - examples/debug/relative_path.hpp
  isVerificationFile: false
  path: examples/debug/d/e/f/g/foo.hpp
  requiredBy: []
  timestamp: '2020-03-19 16:25:51+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - examples/debug/relative_path.test.cpp
documentation_of: examples/debug/d/e/f/g/foo.hpp
layout: document
redirect_from:
- /library/examples/debug/d/e/f/g/foo.hpp
- /library/examples/debug/d/e/f/g/foo.hpp.html
title: examples/debug/d/e/f/g/foo.hpp
---
