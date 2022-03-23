---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    STANDALONE: ''
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 100, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: STANDALONE\ndef main():\n    raise RuntimeError(\"\
    error\")\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn: []
  isVerificationFile: true
  path: examples/debug/sameasrunner2.test.py
  requiredBy: []
  timestamp: '2022-03-23 23:26:26+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: examples/debug/sameasrunner2.test.py
layout: document
redirect_from:
- /verify/examples/debug/sameasrunner2.test.py
- /verify/examples/debug/sameasrunner2.test.py.html
title: examples/debug/sameasrunner2.test.py
---
