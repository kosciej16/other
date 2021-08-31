from typing import Dict
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

from typing import NewType

ModelNumber = NewType("ModelNumber", int)


class A(BaseModel):
    a: int


class B(BaseModel):
    b: int


class C(A, B):
    c: int


@app.get("/", response_model=C)
def models2():
    pass


# @app.get("/", response_model=Dict[ModelNumber, RiskModel])
# def models():
#     return {1: RiskModel(low=1, high=2), 2: RiskModel(low=10, high=20)}


if __name__ == "__main__":
    kwargs = {"host": "0.0.0.0", "port": 5000}
    kwargs.update({"debug": True, "reload": True})
    uvicorn.run("app:app", **kwargs)
