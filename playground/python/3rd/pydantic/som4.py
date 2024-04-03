from pydantic import BaseModel


class Parent(BaseModel):
    p1: str


class Child(Parent):
    p2: str


def foo(p: Parent):
    pass


obj = Child(p1="a", p2="b")
# print(type(obj))
parent_cls = obj.__class__.__bases__[0]
el = parent_cls(**obj.model_dump())
print(type(el))
print(el)


foo(el)
# __import__("pdb").set_trace()
