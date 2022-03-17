---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: cs
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/point_set_range_composite
    links:
    - https://judge.yosupo.jp/problem/point_set_range_composite
    - https://judge.yosupo.jp/problem/point_set_range_composite
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
    \ Command '['dotnet', 'build', '/home/runner/work/verification-helper/verification-helper/examples/csharpsx/Tests/Tests.csproj',\
    \ '-p:BaseIntermediateOutputPath=/home/runner/work/verification-helper/verification-helper/.verify-helper/cache/dotnet/obj/']'\
    \ returned non-zero exit status 1.\n"
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
  dependsOn: []
  isVerificationFile: true
  path: examples/csharpsx/Tests/segment_tree.point_set_range_composite.test.cs
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: examples/csharpsx/Tests/segment_tree.point_set_range_composite.test.cs
layout: document
redirect_from:
- /verify/examples/csharpsx/Tests/segment_tree.point_set_range_composite.test.cs
- /verify/examples/csharpsx/Tests/segment_tree.point_set_range_composite.test.cs.html
title: examples/csharpsx/Tests/segment_tree.point_set_range_composite.test.cs
---
