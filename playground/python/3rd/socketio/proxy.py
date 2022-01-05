import asyncio
from dataclasses import dataclass
from typing import Any
import socketio
import uvicorn

from fastapi import FastAPI, APIRouter

sio: Any = socketio.AsyncServer(async_mode="asgi", cors_allowed_origins=[])
socket_app = socketio.ASGIApp(sio)
app = FastAPI()

router = APIRouter()

lock = asyncio.Lock()


class MyCustomNamespace(socketio.AsyncNamespace):
    async def trigger_event(self, event_name, sid, *args):
        print(f"{event_name=}, {sid=}")
        if args:
            print(f"data is {args[0]}")


sio.register_namespace(MyCustomNamespace())

app.mount("/", socket_app)


if __name__ == "__main__":
    kwargs = {"host": "0.0.0.0", "port": 5000}
    kwargs.update({"debug": True, "reload": True})
    uvicorn.run("proxy:app", **kwargs)
