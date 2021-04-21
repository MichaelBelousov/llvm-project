//===----------------------------------------------------------------------===//
// Mike's prologue
//===----------------------------------------------------------------------===//
This a fork of clang testing a concept called "virtual templates"
which is basically templates that can optionally be generics instead
(so a virtual template is a template that doesn't get instantiated and instead
requires per-type indirection tables, a runtime indirection resulting in a
performance penalty, a tradeoff for no longer needing instantions
which is a size optimization)

TODO:

propagate:
- ActOnCXXMemberDeclarator
- ActOnStartOfFunctionDef

//===----------------------------------------------------------------------===//
// C Language Family Front-end
//===----------------------------------------------------------------------===//

Welcome to Clang.  This is a compiler front-end for the C family of languages
(C, C++, Objective-C, and Objective-C++) which is built as part of the LLVM
compiler infrastructure project.

Unlike many other compiler frontends, Clang is useful for a number of things
beyond just compiling code: we intend for Clang to be host to a number of
different source-level tools.  One example of this is the Clang Static Analyzer.

If you're interested in more (including how to build Clang) it is best to read
the relevant web sites.  Here are some pointers:

Information on Clang:             http://clang.llvm.org/
Building and using Clang:         http://clang.llvm.org/get_started.html
Clang Static Analyzer:            http://clang-analyzer.llvm.org/
Information on the LLVM project:  http://llvm.org/

If you have questions or comments about Clang, a great place to discuss them is
on the Clang development mailing list:
  http://lists.llvm.org/mailman/listinfo/cfe-dev

If you find a bug in Clang, please file it in the LLVM bug tracker:
  http://llvm.org/bugs/
