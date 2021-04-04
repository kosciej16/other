Z = 0
from b import B


class A:
    def __init__(self, a):
        self.a = a

    def f(self):
        c = 10
        self.b = B(self.a, b=c)
        self.b()

    def g(self):
        b = B()
        return b.foo()
