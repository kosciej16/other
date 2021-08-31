class alias:
    def __init__(self, name, *, write=False):
        self.name = name
        self.write = write

    def __get__(self, obj, objtype=None):
        if obj is None:
            return getattr(objtype, self.name)
        return getattr(obj, self.name)

    def __set__(self, obj, value):
        if not self.write:
            raise AttributeError
        setattr(obj, self.name, value)


class RegisteredObject:
    _registry = ()
    registry = alias("_registry")

    def __init__(self, name):
        RegisteredObject._registry += (self,)
        self.name = name


o = RegisteredObject("Trey")
print(o.name)
print(o.registry)
print(RegisteredObject.registry)
