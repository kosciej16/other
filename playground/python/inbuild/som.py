import itertools
from typing import Optional
from dataclasses import dataclass


class A:
    def __init__(self):
        print(dir(self))
        print(id(self.f))

    def f(self):
        raise NotImplementedError

    def g(self):
        a = 10
        print(id(a))
        print(id(a))
        print(id(a))
        print(id(self))
        print(id(self))
        print(id(self))
        print(callable(self.f))
        print(id(self.f))
        print(id(self.f))
        print(id(self.f))
        self.f()


class B(A):
    def f(self):
        print(id(self.f))
        print("a")

    def h(self):
        print("a")


# a = A()
# a.g()

for i in itertools.product(range(10), range(10)):
    print(i)
