import httpx
import requests
from datetime import datetime
from pydantic import BaseModel, Field


class Foo(BaseModel):
    param: str
    other: str = Field(..., serialization_alias="OTHER")
    foo: str = Field("", init=False)
    to_exclude: str = Field(..., exclude=True)

    def model_post_init(self, _) -> None:
        self.foo = "aaaa"


class Bar(BaseModel):
    bar: str
    foo: Foo


class Types(BaseModel):
    d: datetime
    s: str = "1"

    class Config:
        json_encoders = {
            datetime: lambda v: v.strftime("%H:%M"),
        }


f = Foo(param="file.txt", to_exclude="b", other="ll")
b = Bar(bar="barr", foo=f)

res = b.model_dump_json()
print(res)

s = {1, 2, 3}
s.update([1, 2])

t = Types(d=datetime.now())
# res = t.model_dump_json(exclude={"d"})
res = t.model_dump()
print(res)
print(type(res))

headers = {"Content-Type": "application/json"}

requests.post("http://127.0.0.1:8000/message", data=t.model_dump_json(), headers=headers)
