from typing import Dict
from pydantic import BaseModel


class B(BaseModel):
    a: int
    b: int


# class A(Dict[int, B]):
# pass
class A(BaseModel):
    d: Dict[int, B]

    def __getitem__(self, k):
        return self.d[k]

    def __delitem__(self, k):
        return self.d[k]

    def __getattr__(self, item):
        return getattr(self.d, item)


d = {"1": {"a": 2, "b": 3}}

a = A(d=d)

print(a[1])
del a[1]

for x, y in a.items():
    print(x, y)
