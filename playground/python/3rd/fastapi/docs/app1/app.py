from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn

app1 = FastAPI()


@app1.get("/")
async def index():
    return []


class Model(BaseModel):
    a: int
    b: int


@app1.get("/simple", response_model=Model)
async def simple():
    return Model(a=10, b=20)


if __name__ == "__main__":
    kwargs = {"host": "0.0.0.0", "port": 5000}
    kwargs.update({"reload": True})
    uvicorn.run("app:app1", **kwargs)
