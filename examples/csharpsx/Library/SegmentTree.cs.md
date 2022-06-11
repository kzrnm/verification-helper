---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: examples/csharpsx/Tests/segment_tree.point_set_range_composite.test.cs
    title: examples/csharpsx/Tests/segment_tree.point_set_range_composite.test.cs
  - icon: ':heavy_check_mark:'
    path: examples/csharpsx/Tests/segment_tree.range_minimum_query.test.cs
    title: examples/csharpsx/Tests/segment_tree.range_minimum_query.test.cs
  - icon: ':heavy_check_mark:'
    path: examples/csharpsx/Tests/segment_tree.range_sum_query.test.cs
    title: examples/csharpsx/Tests/segment_tree.range_sum_query.test.cs
  _isVerificationFailed: false
  _pathExtension: cs
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "using System;\nnamespace Library\n{\n    public class SegmentTree<T>\n\
    \    {\n        public int Count { get; private set; }\n        T Identity;\n\
    \        T[] Data;\n        Func<T, T, T> Merge;\n        int LeafCount;\n   \
    \     public SegmentTree(int count, T identity, Func<T, T, T> merge)\n       \
    \ {\n            Count = count;\n            Identity = identity;\n          \
    \  Merge = merge;\n            LeafCount = 1;\n            while (LeafCount <\
    \ count) LeafCount <<= 1;\n            Data = new T[LeafCount << 1];\n       \
    \     for (int i = 1; i < Data.Length; i++) Data[i] = identity;\n        }\n \
    \       public T this[int index]\n        {\n            get { return Data[LeafCount\
    \ + index]; }\n            set { Assign(index, value); }\n        }\n        public\
    \ void Assign(int i, T x) { Data[i += LeafCount] = x; while (0 < (i >>= 1)) Data[i]\
    \ = Merge(Data[i << 1], Data[(i << 1) | 1]); }\n        public void Operate(int\
    \ i, T x) { Data[i += LeafCount] = Merge(Data[i], x); while (0 < (i >>= 1)) Data[i]\
    \ = Merge(Data[i << 1], Data[(i << 1) | 1]); }\n        public T Slice(int l,\
    \ int length) => Fold(l, l + length);\n        public T Fold(int l, int r)\n \
    \       {\n            T lRes = Identity, rRes = Identity;\n            for (l\
    \ += LeafCount, r += LeafCount - 1; l <= r; l = (l + 1) >> 1, r = (r - 1) >> 1)\n\
    \            {\n                if ((l & 1) == 1) lRes = Merge(lRes, Data[l]);\n\
    \                if ((r & 1) == 0) rRes = Merge(Data[r], rRes);\n            }\n\
    \            return Merge(lRes, rRes);\n        }\n    }\n}\n#region Expanded\
    \ by https://github.com/kzrnm/SourceExpander\n#endregion Expanded by https://github.com/kzrnm/SourceExpander\n"
  code: "\uFEFFusing System;\n\nnamespace Library\n{\n    public class SegmentTree<T>\n\
    \    {\n        public int Count { get; private set; }\n        T Identity;\n\
    \        T[] Data;\n        Func<T, T, T> Merge;\n        int LeafCount;\n   \
    \     public SegmentTree(int count, T identity, Func<T, T, T> merge)\n       \
    \ {\n            Count = count;\n            Identity = identity;\n          \
    \  Merge = merge;\n            LeafCount = 1;\n            while (LeafCount <\
    \ count) LeafCount <<= 1;\n            Data = new T[LeafCount << 1];\n       \
    \     for (int i = 1; i < Data.Length; i++) Data[i] = identity;\n        }\n \
    \       public T this[int index]\n        {\n            get { return Data[LeafCount\
    \ + index]; }\n            set { Assign(index, value); }\n        }\n        public\
    \ void Assign(int i, T x) { Data[i += LeafCount] = x; while (0 < (i >>= 1)) Data[i]\
    \ = Merge(Data[i << 1], Data[(i << 1) | 1]); }\n        public void Operate(int\
    \ i, T x) { Data[i += LeafCount] = Merge(Data[i], x); while (0 < (i >>= 1)) Data[i]\
    \ = Merge(Data[i << 1], Data[(i << 1) | 1]); }\n        public T Slice(int l,\
    \ int length) => Fold(l, l + length);\n        public T Fold(int l, int r)\n \
    \       {\n            T lRes = Identity, rRes = Identity;\n            for (l\
    \ += LeafCount, r += LeafCount - 1; l <= r; l = (l + 1) >> 1, r = (r - 1) >> 1)\n\
    \            {\n                if ((l & 1) == 1) lRes = Merge(lRes, Data[l]);\n\
    \                if ((r & 1) == 0) rRes = Merge(Data[r], rRes);\n            }\n\
    \            return Merge(lRes, rRes);\n        }\n    }\n}\n"
  dependsOn: []
  isVerificationFile: false
  path: examples/csharpsx/Library/SegmentTree.cs
  requiredBy: []
  timestamp: '2022-06-12 02:18:40+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - examples/csharpsx/Tests/segment_tree.point_set_range_composite.test.cs
  - examples/csharpsx/Tests/segment_tree.range_sum_query.test.cs
  - examples/csharpsx/Tests/segment_tree.range_minimum_query.test.cs
documentation_of: examples/csharpsx/Library/SegmentTree.cs
layout: document
redirect_from:
- /library/examples/csharpsx/Library/SegmentTree.cs
- /library/examples/csharpsx/Library/SegmentTree.cs.html
title: examples/csharpsx/Library/SegmentTree.cs
---
