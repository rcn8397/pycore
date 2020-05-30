# -*- coding: utf-8 -*-
'''
Data objects and utilties
'''

class Dataset(set):
    def __init__(self, s=(), label=None):
        super(Dataset,self).__init__(s)
        if label is None and hasattr(s, 'label'):
            label = s.label
        self.label = label

    @classmethod
    def _wrap_methods(cls, names):
        def wrap_method_closure(name):
            def inner(self, *args):
                result = getattr(super(cls, self), name)(*args)
                if isinstance(result, set) and not hasattr(result, 'label'):
                    result = cls(result, label=self.label)
                return result
            inner.fn_name = name
            setattr(cls, name, inner)
        for name in names:
            wrap_method_closure(name)

Dataset._wrap_methods(['__ror__', 'difference_update', '__isub__', 
    'symmetric_difference', '__rsub__', '__and__', '__rand__', 'intersection',
    'difference', '__iand__', 'union', '__ixor__', 
    'symmetric_difference_update', '__or__', 'copy', '__rxor__',
    'intersection_update', '__xor__', '__ior__', '__sub__',
])
