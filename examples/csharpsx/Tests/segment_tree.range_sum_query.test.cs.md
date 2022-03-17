---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: examples/csharpsx/Library/SegmentTree.cs
    title: examples/csharpsx/Library/SegmentTree.cs
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: cs
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/all/DSL_2_B
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/all/DSL_2_B
    - https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/all/DSL_2_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/csharp.py\"\
    , line 254, in bundle\n    self.config.check_bundle_enable(_resolve_csproj(path))\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/csharp.py\"\
    , line 192, in check_bundle_enable\n    raise RuntimeError('project is not enable\
    \ to bundle')\nRuntimeError: project is not enable to bundle\n"
  code: "using System;\nusing System.Linq;\nusing Library;\n\n// verification-helper:\
    \ PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/all/DSL_2_B\n\
    class range_sum_query\n{\n    static void Main()\n    {\n        var nq = Console.ReadLine().Split().Select(int.Parse).ToArray();\n\
    \        var (n, q) = (nq[0], nq[1]);\n        SegmentTree<int> segTree = new\
    \ SegmentTree<int>(n, 0, (x, y) => x + y);\n\n        for (int i = 0; i < q; i++)\n\
    \        {\n            var query = Console.ReadLine().Split().Select(int.Parse).ToArray();\n\
    \            if (query[0] == 0)\n            {\n                segTree[query[1]\
    \ - 1] += query[2];\n            }\n            else\n            {\n        \
    \        Console.WriteLine(segTree[(query[1] - 1)..query[2]]);\n            }\n\
    \        }\n    }\n}\n"
  dependsOn:
  - examples/csharpsx/Library/SegmentTree.cs
  isVerificationFile: true
  path: examples/csharpsx/Tests/segment_tree.range_sum_query.test.cs
  requiredBy: []
  timestamp: '2022-03-16 01:07:09+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: examples/csharpsx/Tests/segment_tree.range_sum_query.test.cs
layout: document
redirect_from:
- /verify/examples/csharpsx/Tests/segment_tree.range_sum_query.test.cs
- /verify/examples/csharpsx/Tests/segment_tree.range_sum_query.test.cs.html
title: examples/csharpsx/Tests/segment_tree.range_sum_query.test.cs
---
