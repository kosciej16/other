def deco(i):
    def wrapped(func):
        def w2(self, x):
            print(x)
            print(i)
            func(self, x)

        return w2

    return wrapped


a = 10


class M:
    def m(self):
        print(locals())


class A(M):
    def __init__(self):
        self.a = 10

    def f(self, x, y):
        self.m()


a = A()
a.f(10, 20)
