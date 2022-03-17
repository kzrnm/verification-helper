---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: cs
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/csharp.py\"\
    , line 231, in bundle\n    _check_env(path)\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/csharp.py\"\
    , line 89, in _check_env\n    _check_embedded_existing(_resolve_csproj(path))\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/csharp.py\"\
    , line 80, in _check_embedded_existing\n    subprocess.check_output(command)\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/subprocess.py\"\
    , line 420, in check_output\n    return run(*popenargs, stdout=PIPE, timeout=timeout,\
    \ check=True,\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/subprocess.py\"\
    , line 524, in run\n    raise CalledProcessError(retcode, process.args,\nsubprocess.CalledProcessError:\
    \ Command '['dotnet', 'build', '/home/runner/work/verification-helper/verification-helper/examples/csharpsx/Library/Library.csproj',\
    \ '-p:BaseIntermediateOutputPath=/home/runner/work/verification-helper/verification-helper/.verify-helper/cache/dotnet/obj/']'\
    \ returned non-zero exit status 1.\n"
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
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: examples/csharpsx/Library/SegmentTree.cs
layout: document
redirect_from:
- /library/examples/csharpsx/Library/SegmentTree.cs
- /library/examples/csharpsx/Library/SegmentTree.cs.html
title: examples/csharpsx/Library/SegmentTree.cs
---
