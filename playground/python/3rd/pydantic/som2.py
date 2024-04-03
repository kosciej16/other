from pydantic import BaseModel, Field


class A(BaseModel):
    date = ""


class B(A):
    person: float = 0

    def __init__(self):
        super().__init__()
        self.extra = {}


class C(BaseModel):
    s: str = Field(max_length=5)


# b = B()
# print(b.person)
c = C(s="abcsdasd")
