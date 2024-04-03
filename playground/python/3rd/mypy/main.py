from enum import Enum, IntEnum
import typing as t

T = t.TypeVar("T", bound="MyEnum")
V = t.TypeVar("V", bound="Test")


class Test:
    @classmethod
    def test(cls: t.Type[V], elem: t.Union[int, V]) -> V:
        reveal_type(cls)
        reveal_type(elem)
        if isinstance(elem, cls):
            reveal_type(elem)
            return cls()
        reveal_type(elem)
        if isinstance(elem, Test):
            reveal_type(elem)
            return cls()
        reveal_type(elem)
        return cls()


# def ff(x: union[V, int]) -> V:
#     reveal_type(x)
#     print(x)
#     if isinstance(x, V):
#         return x
#     return x


class MyEnum(Enum):
    A = 0
    B = 1

    @classmethod
    def coerce(cls: t.Type["MyEnum"], item: t.Union[int, T]) -> "MyEnum":
        return item if isinstance(item, cls) else cls(int(item))
