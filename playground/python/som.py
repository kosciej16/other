from types import CoroutineType
from typing import Callable, Protocol, overload
from typing import Any, Awaitable, Callable, TypeVar


class Child:
    pass


class Parent(Child):
    pass


def foo(i: int):
    pass


class PluginCallable(Protocol):
    def __call__(self, content: int | str) -> None: ...


def foo2(p: PluginCallable):
    pass


foo2(foo)
