---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: examples/debug/include_relative.test.cpp
    title: examples/debug/include_relative.test.cpp
  _isVerificationFailed: false
  _pathExtension: hpp
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: '#line 2 "examples/macros.hpp"

    #define REP(i, n) for (int i = 0; (i) < (int)(n); ++ (i))

    #define REP3(i, m, n) for (int i = (m); (i) < (int)(n); ++ (i))

    #define REP_R(i, n) for (int i = (int)(n) - 1; (i) >= 0; -- (i))

    #define REP3R(i, m, n) for (int i = (int)(n) - 1; (i) >= (int)(m); -- (i))

    #define ALL(x) begin(x), end(x)

    '
  code: '#pragma once

    #define REP(i, n) for (int i = 0; (i) < (int)(n); ++ (i))

    #define REP3(i, m, n) for (int i = (m); (i) < (int)(n); ++ (i))

    #define REP_R(i, n) for (int i = (int)(n) - 1; (i) >= 0; -- (i))

    #define REP3R(i, m, n) for (int i = (int)(n) - 1; (i) >= (int)(m); -- (i))

    #define ALL(x) begin(x), end(x)'
  dependsOn: []
  isVerificationFile: false
  path: examples/macros.hpp
  requiredBy: []
  timestamp: '2022-03-23 23:33:19+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - examples/debug/include_relative.test.cpp
documentation_of: examples/macros.hpp
layout: document
redirect_from:
- /library/examples/macros.hpp
- /library/examples/macros.hpp.html
title: examples/macros.hpp
---
