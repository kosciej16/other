from fastapi import FastAPI, Query, Request, HTTPException
from dataclasses import dataclass
from fastapi.middleware.cors import CORSMiddleware

import sys
import asyncio
from fastapi.responses import PlainTextResponse

from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel
import uvicorn


from pydantic import BaseModel, model_validator


class A(BaseModel):
    action: str = "akcja_a"
    f1: int


class B(BaseModel):
    action: str = "akcja_b"
    f2: str


class C(BaseModel):
    f1: int
    f2: int
    f3: bool


class BulkAction(BaseModel):
    a: A | None = None
    b: B | None = None
    c: C | None = None

    @model_validator(mode="after")
    def check_only_one_action(self) -> "BulkAction":
        actions: list[str | None] = [
            "a" if self.a is not None else None,
            "b" if self.b is not None else None,
            "c" if self.c is not None else None,
        ]
        actions_received = [i for i in actions if i is not None]
        if len(actions_received) != 1:
            raise ValueError(f"can specify only one action, received {actions_received}")
        return self


class BulkActionsRequest(BaseModel):
    actions: list[BulkAction]


class BulkActionsRequest2(BaseModel):
    actions: list[B | A | C]


class AllSModel(BaseModel):
    s_id: int
    s_name: str


class Data(BaseModel):
    user: str


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request: Request, exc: RequestValidationError):
#     return PlainTextResponse(str("the string does not match the correct regex"), status_code=422)


@app.get("/other")
async def index(i: int):
    return []


@app.get("/simple")
async def simple():
    return "abc"


@app.get("/timeout")
async def tm():
    import time

    time.sleep(10)
    return


@app.get("/error")
async def error():
    raise HTTPException(status_code=429, detail="ERROR")


@app.get("/")
async def stop(user: str):
    pass


queue = asyncio.Queue()


async def foo():
    print("A")


@app.get("/task")
async def schedule():
    await queue.put(foo)


@app.post("/")
async def test(req: Request):
    data = dict(await req.form())
    print(data)
    return data


# @app.on_event("startup")
async def queue_manager():
    while True:
        print("GET")
        foo = await queue.get()

        await foo()
        queue.task_done()


# @app.on_event("startup")
async def app_startup():
    task = asyncio.create_task(queue_manager())
    await asyncio.gather(task)


@app.post("/api/volumes/{volume_id}/bulk/")
def bulk(*, volume_id: int, bulk_actions_request: BulkActionsRequest):
    pass


@app.post("/api/volumes/{volume_id}/bulk2/")
def bulk2(*, volume_id: int, bulk_actions_request: BulkActionsRequest2):
    pass


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=5959, reload=True)
