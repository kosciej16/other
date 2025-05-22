from dataclasses import asdict, dataclass


@dataclass
class B:
    LOL: str


@dataclass
class A:
    A: int
    BB: str
    ref: B


a = A(A=1, BB="a", ref=B(LOL="1"))
print(asdict(a))
