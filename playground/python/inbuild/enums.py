from enum import Enum


class A:
    class E(Enum):
        A = "a"
        B = "b"

        @classmethod
        def foo(cls):
            return [cls.value for cls in A.E]


x = A.E.foo()
print(x)


# a = [("opcja1", "opcja1"), ("opcja2", "opcja2")]
# E = Enum("E", a)
# e = E()
