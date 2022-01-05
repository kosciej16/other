import uvicorn
from fastapi import FastAPI

import socketio

sio = socketio.AsyncServer(async_mode="asgi")
socket_app = socketio.ASGIApp(sio)
app = FastAPI()


@app.get("/test")
async def test():
    print("test")
    return "WORKS"


app.mount("/", socket_app)  # Here we mount socket app to main fastapi app


@sio.on("connect")
async def connect(sid, env):
    print("on connect")


@sio.on("direct")
async def send_message(sid, msg):
    print(f"direct {msg}")
    await sio.emit("event_name", msg, room=sid)  # we can send message to specific sid


@sio.on("broadcast")
async def send_message(sid, msg):
    print(f"broadcast {msg}")
    await sio.emit("event_name", msg)  # or send to everyone


@sio.on("disconnect")
async def disconnect(sid):
    print("on disconnect")


if __name__ == "__main__":
    kwargs = {"host": "0.0.0.0", "port": 5000}
    kwargs.update({"debug": True, "reload": True})
    uvicorn.run("tmp:app", **kwargs)
