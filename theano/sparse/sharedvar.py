import scipy.sparse
from theano.compile import shared_constructor, SharedVariable
from theano import config
from basic import SparseType, _sparse_py_operators

class SparseTensorSharedVariable(SharedVariable, _sparse_py_operators):
    pass

@shared_constructor
def sparse_constructor(value, name=None, strict=False, format = None):
    """SharedVariable Constructor for SparseType

    writeme
    """
    if not isinstance(value, scipy.sparse.spmatrix):
        raise TypeError()

    if format is None:
        format = value.format
    type = SparseType(format =format, dtype = value.dtype)
    return SparseTensorSharedVariable(type = type, value = value, name=name, strict =strict)


