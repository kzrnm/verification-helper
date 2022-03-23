---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    STANDALONE: ''
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 100, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: STANDALONE\nimport subprocess\nimport sys\n\ndef main():\n\
    \    subprocess.run([sys.executable, '-V'], check=True)\n\n\nif __name__ == '__main__':\n\
    \    main()\n"
  dependsOn: []
  isVerificationFile: true
  path: examples/debug/sameasrunner.test.py
  requiredBy: []
  timestamp: '2022-03-24 00:05:01+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: examples/debug/sameasrunner.test.py
layout: document
redirect_from:
- /verify/examples/debug/sameasrunner.test.py
- /verify/examples/debug/sameasrunner.test.py.html
title: examples/debug/sameasrunner.test.py
---
