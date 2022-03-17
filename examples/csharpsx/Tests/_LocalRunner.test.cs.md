---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: cs
  _verificationStatusIcon: ':x:'
  attributes:
    IGNORE: ''
    links: []
  bundledCode: "using System;\nusing System.Reflection;\nnamespace Verifier\n{\n \
    \   public class LocalRunner\n    {\n        static void Main(string[] args)\n\
    \        {\n            string verifier;\n            if (args.Length == 0)\n\
    \            {\n                Console.WriteLine(\"Input verifier name:\");\n\
    \                verifier = Console.ReadLine();\n            }\n            else\n\
    \            {\n                verifier = args[0];\n            }\n         \
    \   var type = Type.GetType(verifier);\n\n            var method = type.GetMethod(\"\
    Main\", BindingFlags.Static | BindingFlags.Public | BindingFlags.NonPublic);\n\
    \            method.Invoke(null, null);\n        }\n    }\n}\n#region Expanded\
    \ by https://github.com/kzrnm/SourceExpander\n#endregion Expanded by https://github.com/kzrnm/SourceExpander\n"
  code: "\uFEFFusing System;\nusing System.Reflection;\n// verification-helper: IGNORE\n\
    namespace Verifier\n{\n    public class LocalRunner\n    {\n        static void\
    \ Main(string[] args)\n        {\n            string verifier;\n            if\
    \ (args.Length == 0)\n            {\n                Console.WriteLine(\"Input\
    \ verifier name:\");\n                verifier = Console.ReadLine();\n       \
    \     }\n            else\n            {\n                verifier = args[0];\n\
    \            }\n            var type = Type.GetType(verifier);\n\n           \
    \ var method = type.GetMethod(\"Main\", BindingFlags.Static | BindingFlags.Public\
    \ | BindingFlags.NonPublic);\n            method.Invoke(null, null);\n       \
    \ }\n    }\n}\n"
  dependsOn: []
  isVerificationFile: true
  path: examples/csharpsx/Tests/_LocalRunner.test.cs
  requiredBy: []
  timestamp: '2022-03-17 11:57:58+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: examples/csharpsx/Tests/_LocalRunner.test.cs
layout: document
redirect_from:
- /verify/examples/csharpsx/Tests/_LocalRunner.test.cs
- /verify/examples/csharpsx/Tests/_LocalRunner.test.cs.html
title: examples/csharpsx/Tests/_LocalRunner.test.cs
---
