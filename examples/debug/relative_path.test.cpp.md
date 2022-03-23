---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: examples/debug/a/b/c/foo.hpp
    title: examples/debug/a/b/c/foo.hpp
  - icon: ':x:'
    path: examples/debug/d/e/f/g/foo.hpp
    title: examples/debug/d/e/f/g/foo.hpp
  - icon: ':x:'
    path: examples/debug/h/i/j/k/l/foo.hpp
    title: examples/debug/h/i/j/k/l/foo.hpp
  - icon: ':x:'
    path: examples/debug/relative_path.hpp
    title: examples/debug/relative_path.hpp
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: cpp
  _verificationStatusIcon: ':x:'
  attributes:
    '*NOT_SPECIAL_COMMENTS*': ''
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
  bundledCode: "#line 1 \"examples/debug/relative_path.test.cpp\"\n#define PROBLEM\
    \ \"http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A\"\n#include\
    \ <cstdio>\n#line 2 \"examples/debug/relative_path.hpp\"\nchar *hello = \"Hello\
    \ World\";\n#line 6 \"examples/debug/relative_path.test.cpp\"\n\nint main() {\n\
    \    printf(\"%s\\n\", hello);\n    return 0;\n}\n"
  code: "#define PROBLEM \"http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A\"\
    \n#include <cstdio>\n#include \"./a/b/c/foo.hpp\"\n#include \"d/e/f/g/foo.hpp\"\
    \n#include \"examples/debug/h/i/j/k/l/foo.hpp\"\n\nint main() {\n    printf(\"\
    %s\\n\", hello);\n    return 0;\n}\n"
  dependsOn:
  - examples/debug/a/b/c/foo.hpp
  - examples/debug/relative_path.hpp
  - examples/debug/d/e/f/g/foo.hpp
  - examples/debug/h/i/j/k/l/foo.hpp
  isVerificationFile: true
  path: examples/debug/relative_path.test.cpp
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: examples/debug/relative_path.test.cpp
layout: document
redirect_from:
- /verify/examples/debug/relative_path.test.cpp
- /verify/examples/debug/relative_path.test.cpp.html
title: examples/debug/relative_path.test.cpp
---
