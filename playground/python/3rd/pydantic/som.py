from typing import reveal_type
from pydantic import BaseModel


class Foo(BaseModel):
    foo: str


class Bar(BaseModel):
    bar: str


class FooWrapper(Foo):
    action: str = "foo"


class BarWrapper(Bar):
    action: str = "bar"


class ActionsRequest(BaseModel):
    actions: list[FooWrapper | BarWrapper]


def test_bulk_actions():
    foo = {"action": "foo", "foo": "7"}
    bar = {"action": "bar", "bar": "7"}
    return ActionsRequest.model_validate({"actions": [foo, bar]})


def foo(f: Bar):
    pass


obj = FooWrapper(action="foo", foo="7")
parent_cls = obj.__class__.__bases__[0]
el = parent_cls(**obj.model_dump())
reveal_type(el)
foo(el)
