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
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/all/DSL_2_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/all/DSL_2_A
    - https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/all/DSL_2_A
    - https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/all/DSL_2_A
    - https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/all/DSL_2_A
    - https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/all/DSL_2_A
  bundledCode: "using Library;\nusing System;\nusing System.Linq;\nclass range_minimum_query\n\
    {\n    static void Main()\n    {\n        var nq = Console.ReadLine().Split().Select(int.Parse).ToArray();\n\
    \        var (n, q) = (nq[0], nq[1]);\n        SegmentTree<int> segTree = new\
    \ SegmentTree<int>(n, int.MaxValue, Math.Min);\n\n        for (int i = 0; i <\
    \ q; i++)\n        {\n            var query = Console.ReadLine().Split().Select(int.Parse).ToArray();\n\
    \            if (query[0] == 0)\n            {\n                segTree[query[1]]\
    \ = query[2];\n            }\n            else\n            {\n              \
    \  Console.WriteLine(segTree[query[1]..(query[2] + 1)]);\n            }\n    \
    \    }\n    }\n}\n#region Expanded by https://github.com/kzrnm/SourceExpander\n\
    namespace Library { public class SegmentTree<T> { public int Count { get; private\
    \ set; }  T Identity; T[] Data; Func<T, T, T> Merge; int LeafCount; public SegmentTree(int\
    \ count, T identity, Func<T, T, T> merge) { Count = count; Identity = identity;\
    \ Merge = merge; LeafCount = 1; while (LeafCount < count) LeafCount <<= 1; Data\
    \ = new T[LeafCount << 1]; for (int i = 1; i < Data.Length; i++) Data[i] = identity;\
    \ }  public T this[int index] { get { return Data[LeafCount + index]; }  set {\
    \ Assign(index, value); } }  public void Assign(int i, T x) { Data[i += LeafCount]\
    \ = x; while (0 < (i >>= 1)) Data[i] = Merge(Data[i << 1], Data[(i << 1) | 1]);\
    \ }  public void Operate(int i, T x) { Data[i += LeafCount] = Merge(Data[i], x);\
    \ while (0 < (i >>= 1)) Data[i] = Merge(Data[i << 1], Data[(i << 1) | 1]); } \
    \ public T Slice(int l, int length) => Fold(l, l + length); public T Fold(int\
    \ l, int r) { T lRes = Identity, rRes = Identity; for (l += LeafCount, r += LeafCount\
    \ - 1; l <= r; l = (l + 1) >> 1, r = (r - 1) >> 1) { if ((l & 1) == 1) lRes =\
    \ Merge(lRes, Data[l]); if ((r & 1) == 0) rRes = Merge(Data[r], rRes); }  return\
    \ Merge(lRes, rRes); } } }\n#endregion Expanded by https://github.com/kzrnm/SourceExpander\n"
  code: "using System;\nusing System.Linq;\nusing Library;\n\n// verification-helper:\
    \ PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/all/DSL_2_A\n\
    class range_minimum_query\n{\n    static void Main()\n    {\n        var nq =\
    \ Console.ReadLine().Split().Select(int.Parse).ToArray();\n        var (n, q)\
    \ = (nq[0], nq[1]);\n        SegmentTree<int> segTree = new SegmentTree<int>(n,\
    \ int.MaxValue, Math.Min);\n\n        for (int i = 0; i < q; i++)\n        {\n\
    \            var query = Console.ReadLine().Split().Select(int.Parse).ToArray();\n\
    \            if (query[0] == 0)\n            {\n                segTree[query[1]]\
    \ = query[2];\n            }\n            else\n            {\n              \
    \  Console.WriteLine(segTree[query[1]..(query[2] + 1)]);\n            }\n    \
    \    }\n    }\n}\n"
  dependsOn:
  - examples/csharpsx/Library/SegmentTree.cs
  isVerificationFile: true
  path: examples/csharpsx/Tests/segment_tree.range_minimum_query.test.cs
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: examples/csharpsx/Tests/segment_tree.range_minimum_query.test.cs
layout: document
redirect_from:
- /verify/examples/csharpsx/Tests/segment_tree.range_minimum_query.test.cs
- /verify/examples/csharpsx/Tests/segment_tree.range_minimum_query.test.cs.html
title: examples/csharpsx/Tests/segment_tree.range_minimum_query.test.cs
---
