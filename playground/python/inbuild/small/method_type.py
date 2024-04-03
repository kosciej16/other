from types import MethodType
from unittest.mock import Mock


class C:
    pass


class A:
    def m(self):
        print("aaa")


a = A()


def new_m(self):
    print("bbb")


a.m = Mock()

a.m()

b = A()
b.m()
