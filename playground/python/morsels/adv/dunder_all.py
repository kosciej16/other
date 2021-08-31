import types
from contextlib import contextmanager

import inspect


def auto_all(g=None):
    g = g or inspect.stack()[1][0].f_globals
    res = []
    module_name = g["__name__"]
    for k, v in g.items():
        if (callable(v) or isinstance(v, types.ModuleType)) and not k.startswith("_"):
            if module_name == v.__module__:
                res.append(k)
    cur = g.get("__all__", [])
    return cur + res


@contextmanager
def public(g):
    c = g.copy()
    # print(globals()["root5"])
    try:
        yield
    finally:
        pass
        a = [k for k in g if k not in c]
        g["__all__"] = a


def start_public_attributes():
    g = inspect.stack()[1][0].f_globals
    g["__all__"] = ""
    g["__all__"] = MySeq(g)


class MySeq:
    def __init__(self, g):
        self.g = g
        self.c = g.copy()
        self.elems = []

    def __getitem__(self, i):
        if i == 0:
            self.elems = [k for k in self.g if k not in self.c]
        return self.elems[i]
