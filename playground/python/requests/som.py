from pydantic import BaseModel
from typing import List
import inspect
from uuid import uuid4
import json
from json import JSONEncoder
import requests
from enum import Enum


class MyEnum(str, Enum):
    a = "bb"
    b = None


class M(BaseModel):
    x: List[str]


print(type(MyEnum))
x = 1
assert list(x) == [x]
l = list(MyEnum)
l2 = [MyEnum]
m = M(x=l)
print(MyEnum.b == "None")
x = MyEnum.a
# m = M(x=x)
# print(m)
# print(type(x))
# x = str(x)
# # x = x.replace("b", "a")
# print(type(x))
# print(x)
# print(len(x))

# print(MyEnum.a.__str__())


class A:
    def __str__(self):
        return "a"


class B:
    def __str__(self):
        return "b"


class C(A, B):
    ...


a = C()
print(a)
# x = json.dumps(MyEnum.a)
# print(x)

# requests.post("http://www.example.com", json=MyEnum.a)
