---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: examples/csharpscript/segment_tree.csx
    title: examples/csharpscript/segment_tree.csx
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: csx
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/all/DSL_2_B
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/all/DSL_2_B
    - https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/all/DSL_2_B
    - https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/all/DSL_2_B
    - https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/all/DSL_2_B
    - https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/all/DSL_2_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/csharpscript.py\"\
    , line 113, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "#load \"./segment_tree.csx\"\n#pragma PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/all/DSL_2_B\n\
    \nusing System;\nusing System.Linq;\n\nvar nq = Console.ReadLine().Split().Select(int.Parse).ToArray();\n\
    var (n, q) = (nq[0], nq[1]);\nSegmentTree<int> segTree = new SegmentTree<int>(n,\
    \ 0, (x, y) => x + y);\n\nfor (int i = 0; i < q; i++)\n{\n    var query = Console.ReadLine().Split().Select(int.Parse).ToArray();\n\
    \    if (query[0] == 0)\n    {\n        segTree[query[1] - 1] += query[2];\n \
    \   }\n    else\n    {\n        Console.WriteLine(segTree[(query[1] - 1)..query[2]]);\n\
    \    }\n}\n"
  dependsOn:
  - examples/csharpscript/segment_tree.csx
  isVerificationFile: true
  path: examples/csharpscript/segment_tree.range_sum_query.test.csx
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: examples/csharpscript/segment_tree.range_sum_query.test.csx
layout: document
redirect_from:
- /verify/examples/csharpscript/segment_tree.range_sum_query.test.csx
- /verify/examples/csharpscript/segment_tree.range_sum_query.test.csx.html
title: examples/csharpscript/segment_tree.range_sum_query.test.csx
---
