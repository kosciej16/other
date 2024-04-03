import asyncio
from dataclasses import dataclass
from datetime import datetime
from time import sleep
from uuid import uuid4
from som import MyLock
from typing import Any
import socketio
import uvicorn
import json
from uuid import UUID


class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            # if the obj is uuid, we simply return the value of uuid
            return obj.hex
        return json.JSONEncoder.default(self, obj)


class MyJson:
    def dumps(self, *args, **kwargs):
        return json.dumps(*args, default=str, **kwargs)

    def loads(self, *args, **kwargs):
        return json.loads(*args, **kwargs)


from fastapi import FastAPI, APIRouter

sio: Any = socketio.AsyncServer(async_mode="asgi", cors_allowed_origins=[], json=MyJson())
socket_app = socketio.ASGIApp(sio)
app = FastAPI()

router = APIRouter()

lock = asyncio.Lock()


def safe_on(f):
    async def inner(self, sid, *args, **kwargs):
        username = "ABC"
        return await f(self, username, *args, **kwargs)

    return inner


class MyCustomNamespace(socketio.AsyncNamespace):
    def on_connect(self, sid, environ):
        print("CUSTOM CONNECT")
        pass

    def on_disconnect(self, sid):
        print("CUSTOM DISCONNECT")
        pass

    @safe_on
    async def on_my_event(self, a, data):
        print(a)
        print(data)
        print("on my event")


sio.register_namespace(MyCustomNamespace("/chat"))


@app.get("/test")
async def tmp():
    sleep(3)
    a = MyLock()
    Cache.l = a
    pass


app.mount("/", socket_app)


class Cache:
    l: MyLock


@sio.on("connect")
async def connect(sid, env):
    # await asyncio.sleep(3)
    # a = MyLock()
    # Cache.l = a
    print("on connect")


@sio.on("connect", namespace="/global")
async def glob_connect(sid, env):
    print("on global connect")


@sio.on("kickme")
async def kickme(sid):
    print("kick")
    await sio.emit("okey", datetime.utcnow())
    # await sio.disconnect(sid, "a")


@sio.on("do")
async def do(sid, data):
    print("BEFORE")
    # async with Cache.l.lock:
    async with lock:
        print("IN")
        await asyncio.sleep(3)
    print("AFTER")


@sio.on("disconnect")
async def disconnect(sid):
    print("on disconnect")


@sio.on("disconnect", namespace="/global")
async def glob_disconnect(sid):
    print("on global disconnect")


if __name__ == "__main__":

    kwargs = {"host": "0.0.0.0", "port": 5000}
    kwargs.update({"debug": True, "reload": True})
    uvicorn.run("server:app", **kwargs)
