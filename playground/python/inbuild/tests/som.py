from dir import const
from a import A

print(const.zmienna)
a = A(const.zmienna)
print("A")


class B:
    def f(self):
        print(const.zmienna)
        return a.f()
