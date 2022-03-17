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
  code: "\uFEFFusing System;\nusing System.Reflection;\n\nnamespace Verifier\n{\n\
    \    public class LocalRunner\n    {\n        static void Main(string[] args)\n\
    \        {\n            string verifier;\n            if (args.Length == 0)\n\
    \            {\n                Console.WriteLine(\"Input verifier name:\");\n\
    \                verifier = Console.ReadLine();\n            }\n            else\n\
    \            {\n                verifier = args[0];\n            }\n         \
    \   var type = Type.GetType(verifier);\n\n            var method = type.GetMethod(\"\
    Main\", BindingFlags.Static | BindingFlags.Public | BindingFlags.NonPublic);\n\
    \            method.Invoke(null, null);\n        }\n    }\n}\n"
  dependsOn: []
  isVerificationFile: false
  path: examples/csharpsx/Tests/_LocalRunner.cs
  requiredBy: []
  timestamp: '2022-03-17 01:55:45+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: examples/csharpsx/Tests/_LocalRunner.cs
layout: document
redirect_from:
- /library/examples/csharpsx/Tests/_LocalRunner.cs
- /library/examples/csharpsx/Tests/_LocalRunner.cs.html
title: examples/csharpsx/Tests/_LocalRunner.cs
---
