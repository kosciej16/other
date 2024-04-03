from fastapi import APIRouter
from pydantic import BaseModel

r1_router = APIRouter(prefix="/zone")


class ZoneSchemaOut(BaseModel):
    e: int
    f: str


@r1_router.get("/", response_model=list[ZoneSchemaOut])
def foo():
    return [ZoneSchemaOut(e=10, f="")]
