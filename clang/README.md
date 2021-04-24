
Mike's prologue
===============

This a fork of clang testing a concept called "virtual templates"
which is basically templates that can optionally be generics instead
(so a virtual template is a template that doesn't get instantiated and instead
requires per-type indirection tables, a runtime indirection resulting in a
performance penalty, a tradeoff for no longer needing instantions
which is a size optimization)

In theory, it might be useful to mark individual parameters as virtual,
so that only they require the redirection, but I'm not going to do that for the MVP

Proof of concept:

translation unit A.cpp (headers assumed)
```cpp
virtual template <typename T, size_t X, size_t Y>
struct Matrix {
  T data[X][Y];

  void reset(const T& t) {
    for (int x = 0; x < X; ++x)
      for (int y = 0; y < Y; ++y)
        data[x][y] = t;
  }
};

// becomes

struct Matrix {
  struct __vt_entry {
    // type parameters thunks
    bool (*op_lt)(void* l, void* r);
    void* (*op_eq)(void* l, const void* r);
    // non-type parameters get values
    size_t X, Y;
  };

  // this requires a Variable-Length-Array, except that the compiler does know max X and Y at compile time
  void* data[X][Y];

  // every templated function takes an additional runtime argument pointer to the instantiation's table
  void reset(const void* t, const __vt_entry& entry) {
    // the entry contains non-type template parameters
    for (int x = 0; x < entry.X; ++x)
      for (int y = 0; y < entry.Y; ++y)
        // and thunks to the correct methods
        entry.op_eq(&data[x][y], t);
  }
};
```

translation unit C.cpp (headers assumed)
```cpp
int C() {
  Matrix<int,3,3> mat;
  mat.reset(10);
  return mat.data[0][0];
}

// becomes

static const __float_2_2_entry = __vt_entry {
  +[](void* a, void* b){return *(int*)a < *(int*)b; },
  +[](void* a, const void* b){return *(int*)a = *(const int*)b; },
  3,
  3
};

int C() {
  Matrix<int,3,3> mat;
  mat.reset(10, __float_2_2_entry);
  return *mat.data[0][0];
}
```

C Language Family Front-end
==============================

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
