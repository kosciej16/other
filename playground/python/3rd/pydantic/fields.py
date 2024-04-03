import pydantic


class Creator(pydantic.BaseModel):
    middle_name: str = pydantic.Field(None, title="MyTitle")


s = Creator.schema_json(indent=2)
print(s)
