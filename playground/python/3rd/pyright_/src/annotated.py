from typing import Annotated, reveal_type


class A:
    pass


def foo(cls: type[A]) -> type[A]:
    x = Annotated[cls, "Heja"]
    reveal_type(x)
    return x
