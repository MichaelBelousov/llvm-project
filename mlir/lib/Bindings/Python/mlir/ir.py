#  Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
#  See https://llvm.org/LICENSE.txt for license information.
#  SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

# Simply a wrapper around the extension module of the same name.
from ._cext_loader import _reexport_cext
_reexport_cext("ir", __name__)
del _reexport_cext

# Extra functions that are not visible to _reexport_cext.
# TODO: is this really necessary?
from _mlir.ir import _enable_debug
_enable_debug = _enable_debug