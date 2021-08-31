from dataclasses import dataclass


@dataclass
class Ref:
    @staticmethod
    def deco(name):
        def f(func):
            def wrapped(instance, *args):
                print(f"put {name}")
                func(instance, *args)
                if getattr(instance, "_referral"):
                    print(f"put referral {name}")

            return wrapped

        return f

    _referral: bool = False

    def mark_as_referral(self):
        self._referral = True


class A(Ref):
    @Ref.deco("nazwa")
    def foo(self, a):
        if a < 10:
            self.mark_as_referral()
            return a
        return a


a = A()
a.foo(15)
a.foo(5)

getattr(a, "aa")
