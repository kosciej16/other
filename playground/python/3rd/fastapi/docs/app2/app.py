from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn
from app2.r1 import r1_router
from app2.r2 import r2_router

app2 = FastAPI()
app2.include_router(r1_router)
app2.include_router(r2_router)


@app2.get("/other")
async def index():
    return []


class Model(BaseModel):
    c: int
    d: int


@app2.get("/simple", response_model=Model)
async def simple():
    return Model(c=10, d=20)


if __name__ == "__main__":
    kwargs = {"host": "0.0.0.0", "port": 5000}
    kwargs.update({"reload": True})
    uvicorn.run("app:app2", **kwargs)
