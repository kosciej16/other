from dataclasses import dataclass
from random import randint
import timeit


l = [1, 2, 3, 4, 5, 6, 7]


@dataclass
class A:
    a1: int
    a2: int
    a3: int
    a4: int
    a5: int
    a6: int
    a7: int


def mysetup():
    pass


def access():
    for _ in range(10000000):
        for j in range(7):
            l[j]


keys = ["abc", "afsd", "gfgs", "asds", "trtr", "tedd", "hgdhd"]


def access2():
    for _ in range(10000000):
        d = {k: l[i] for (i, k) in enumerate(keys)}
        for k in keys:
            d[k]


def access3():
    for _ in range(10000000):
        a = A(
            a1=l[0],
            a2=l[1],
            a3=l[2],
            a4=l[3],
            a5=l[4],
            a6=l[5],
            a7=l[6],
        )
        a.a1
        a.a2
        a.a3
        a.a4
        a.a5
        a.a6
        a.a7


# print(timeit.timeit(setup=mysetup, stmt=access, number=1))
# print(timeit.timeit(setup=mysetup, stmt=access2, number=1))
print(timeit.timeit(setup=mysetup, stmt=access3, number=1))
# code snippet to be executed only once
# mysetup = "from math import sqrt"
