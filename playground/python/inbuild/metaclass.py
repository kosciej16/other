from dataclasses import dataclass, fields


@dataclass
class A:
    dupadupa: int


print(fields(A))


def extend_class(base_cls):
    return type("ExtA", (), base_cls.__dict__)


ExtA = extend_class(A)

a = ExtA()
print(a)
