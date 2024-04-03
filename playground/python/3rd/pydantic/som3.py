from datetime import datetime
import json
import pydantic


myint = int


class SnowflakeId(int):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v: str):
        return cls(v)

    @classmethod
    def __modify_schema__(cls, field_schema: dict) -> None:
        field_schema["type"] = "string"


def my_dumps(v, *, default):
    for key, value in v.items():
        print(type(value))
        if isinstance(value, SnowflakeId):
            v[key] = str(value)
        else:
            v[key] = value
    return json.dumps(v)


class M(pydantic.BaseModel):

    id: SnowflakeId

    class Config:
        json_dumps = my_dumps


m = M(id="123")
print(m.json())
