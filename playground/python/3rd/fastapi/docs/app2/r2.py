from fastapi import APIRouter
from pydantic import BaseModel

r2_router = APIRouter(prefix="/other")


class ZoneSchemaOut(BaseModel):
    e: int
    f: str


@r2_router.get("/", response_model=list[ZoneSchemaOut])
def foo():
    return [ZoneSchemaOut(e=10, f="")]


@r2_router.get("/new", response_model=list[ZoneSchemaOut])
def foo2():
    return [ZoneSchemaOut(e=10, f="")]
