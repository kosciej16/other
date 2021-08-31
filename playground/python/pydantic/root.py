from typing import Dict
from pydantic import BaseModel


class B(BaseModel):
    a: int
    b: int


class A(BaseModel):
    __root__: Dict[int, B]

    def __getitem__(self, k):
        return self.__root__[k]

    def __delitem__(self, k):
        return self.d[k]

    def __getattr__(self, item):
        return getattr(self.d, item)


d = {"1": {"a": 2, "b": 3}}

a = A(__root__=d)
x = a.json()
print(x)
print(type(x))
print(type(a.__root__))
print(a)
print(a[1])
print(a.dict())
