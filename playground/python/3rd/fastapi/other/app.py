from typing import NewType
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import uvicorn


from pydantic import BaseModel, Field

ZoneId = NewType("ZoneId", int)

f = Field(ge=0)


class Data(BaseModel):
    value: ZoneId = f
    value2: ZoneId = f


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/v1/client")
async def simple():
    return "abc"


@app.post("/test")
async def simple2(data: Data):
    return "abc"


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
