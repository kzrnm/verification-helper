---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: examples/rust/src/lib.rs
    title: examples/rust/src/lib.rs
  _extendedVerifiedWith:
  - icon: ':x:'
    path: examples/rust/verification/src/bin/aizu-online-judge-itp1-1-a.rs
    title: examples/rust/verification/src/bin/aizu-online-judge-itp1-1-a.rs
  - icon: ':x:'
    path: examples/rust/verification/src/bin/library-checker-aplusb.rs
    title: examples/rust/verification/src/bin/library-checker-aplusb.rs
  _isVerificationFailed: true
  _pathExtension: rs
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/rust.py\"\
    , line 288, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '//! Provides `"World"`.


    pub static WORLD: &str = "World";

    '
  dependsOn: []
  isVerificationFile: false
  path: examples/rust/crates/helloworld/world/src/lib.rs
  requiredBy:
  - examples/rust/src/lib.rs
  timestamp: '2020-11-30 13:30:54+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - examples/rust/verification/src/bin/aizu-online-judge-itp1-1-a.rs
  - examples/rust/verification/src/bin/library-checker-aplusb.rs
documentation_of: examples/rust/crates/helloworld/world/src/lib.rs
layout: document
redirect_from:
- /library/examples/rust/crates/helloworld/world/src/lib.rs
- /library/examples/rust/crates/helloworld/world/src/lib.rs.html
title: examples/rust/crates/helloworld/world/src/lib.rs
---
