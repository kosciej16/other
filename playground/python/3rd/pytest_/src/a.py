from b import B


class A:
    def __init__(self):
        self.b = B()

    def foo(self):
        return self.b.foo()


a = A()
print(a.foo())
