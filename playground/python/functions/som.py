from dataclasses import dataclass
from functools import partial, partialmethod


@dataclass
class A:
    a: int


class B(A):
    def __init__(self, x, *args):
        super().__init__(*args)
        self.x = x


b = B(1, 3)
print(b)

z = partial(B, x=1)
res = z(2)
print(res)
