---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: examples/debug/include_relative.test.cpp
    title: examples/debug/include_relative.test.cpp
  - icon: ':x:'
    path: examples/segment_tree.point_set_range_composite.test.cpp
    title: examples/segment_tree.point_set_range_composite.test.cpp
  - icon: ':x:'
    path: examples/segment_tree.range_minimum_query.test.cpp
    title: examples/segment_tree.range_minimum_query.test.cpp
  - icon: ':x:'
    path: examples/segment_tree.range_sum_query.test.cpp
    title: examples/segment_tree.range_sum_query.test.cpp
  - icon: ':x:'
    path: examples/union_find_tree.aoj.test.cpp
    title: examples/union_find_tree.aoj.test.cpp
  - icon: ':x:'
    path: examples/union_find_tree.yosupo.test.cpp
    title: examples/union_find_tree.yosupo.test.cpp
  _isVerificationFailed: true
  _pathExtension: hpp
  _verificationStatusIcon: ':x:'
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

    #define ALL(x) begin(x), end(x)

    '
  dependsOn: []
  isVerificationFile: false
  path: examples/macros.hpp
  requiredBy: []
  timestamp: '2019-11-29 11:28:05+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - examples/segment_tree.range_sum_query.test.cpp
  - examples/debug/include_relative.test.cpp
  - examples/union_find_tree.yosupo.test.cpp
  - examples/segment_tree.range_minimum_query.test.cpp
  - examples/union_find_tree.aoj.test.cpp
  - examples/segment_tree.point_set_range_composite.test.cpp
documentation_of: examples/macros.hpp
layout: document
redirect_from:
- /library/examples/macros.hpp
- /library/examples/macros.hpp.html
title: examples/macros.hpp
---
