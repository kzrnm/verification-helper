---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: examples/csharpsx/Library/SegmentTree.cs
    title: examples/csharpsx/Library/SegmentTree.cs
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: cs
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/point_set_range_composite
    links:
    - https://judge.yosupo.jp/problem/point_set_range_composite
  bundledCode: "using Library;\nusing System;\nusing System.Linq;\nclass point_set_range_composite\n\
    {\n    static void Main()\n    {\n        var nq = Console.ReadLine().Split().Select(int.Parse).ToArray();\n\
    \        var (n, q) = (nq[0], nq[1]);\n        SegmentTree<Linear> segTree = new\
    \ SegmentTree<Linear>(n, new Linear(1, 0), Linear.Merge);\n\n        for (int\
    \ i = 0; i < n; i++)\n        {\n            var ab = Console.ReadLine().Split().Select(int.Parse).ToArray();\n\
    \            segTree[i] = new Linear(ab[0], ab[1]);\n        }\n\n        for\
    \ (int i = 0; i < q; i++)\n        {\n            var query = Console.ReadLine().Split().Select(int.Parse).ToArray();\n\
    \            if (query[0] == 0)\n            {\n                segTree[query[1]]\
    \ = new Linear(query[2], query[3]);\n            }\n            else\n       \
    \     {\n                Console.WriteLine(segTree[query[1]..query[2]].EvalWith(query[3]));\n\
    \            }\n        }\n    }\n\n    struct Linear\n    {\n        const int\
    \ MOD = 998244353;\n        public long A;\n        public long B;\n        public\
    \ Linear(long a, long b) { A = a; B = b; }\n        public static Linear Merge(Linear\
    \ a, Linear b) => new Linear(a.A * b.A % MOD, (a.B * b.A + b.B) % MOD);\n    \
    \    public long EvalWith(int x) => (A * x + B) % MOD;\n        public override\
    \ string ToString() => $\"{A} {B}\";\n    }\n}\n#region Expanded by https://github.com/kzrnm/SourceExpander\n\
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
  code: "\uFEFF// verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_set_range_composite\n\
    using System;\nusing System.Linq;\nusing Library;\n\nclass point_set_range_composite\n\
    {\n    static void Main()\n    {\n        var nq = Console.ReadLine().Split().Select(int.Parse).ToArray();\n\
    \        var (n, q) = (nq[0], nq[1]);\n        SegmentTree<Linear> segTree = new\
    \ SegmentTree<Linear>(n, new Linear(1, 0), Linear.Merge);\n\n        for (int\
    \ i = 0; i < n; i++)\n        {\n            var ab = Console.ReadLine().Split().Select(int.Parse).ToArray();\n\
    \            segTree[i] = new Linear(ab[0], ab[1]);\n        }\n\n        for\
    \ (int i = 0; i < q; i++)\n        {\n            var query = Console.ReadLine().Split().Select(int.Parse).ToArray();\n\
    \            if (query[0] == 0)\n            {\n                segTree[query[1]]\
    \ = new Linear(query[2], query[3]);\n            }\n            else\n       \
    \     {\n                Console.WriteLine(segTree[query[1]..query[2]].EvalWith(query[3]));\n\
    \            }\n        }\n    }\n\n    struct Linear\n    {\n        const int\
    \ MOD = 998244353;\n        public long A;\n        public long B;\n        public\
    \ Linear(long a, long b) { A = a; B = b; }\n        public static Linear Merge(Linear\
    \ a, Linear b) => new Linear(a.A * b.A % MOD, (a.B * b.A + b.B) % MOD);\n    \
    \    public long EvalWith(int x) => (A * x + B) % MOD;\n        public override\
    \ string ToString() => $\"{A} {B}\";\n    }\n}\n"
  dependsOn:
  - examples/csharpsx/Library/SegmentTree.cs
  isVerificationFile: true
  path: examples/csharpsx/Tests/segment_tree.point_set_range_composite.test.cs
  requiredBy: []
  timestamp: '2022-03-16 01:07:09+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: examples/csharpsx/Tests/segment_tree.point_set_range_composite.test.cs
layout: document
redirect_from:
- /verify/examples/csharpsx/Tests/segment_tree.point_set_range_composite.test.cs
- /verify/examples/csharpsx/Tests/segment_tree.point_set_range_composite.test.cs.html
title: examples/csharpsx/Tests/segment_tree.point_set_range_composite.test.cs
---
