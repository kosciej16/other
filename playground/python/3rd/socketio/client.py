import asyncio
from uuid import uuid4
import requests

# from httpx import AsyncClient, Response

import socketio

# r = requests.get("http://127.0.0.1:5000/test")


class MyCustomNamespace(socketio.ClientNamespace):
    def on_connect(self):
        pass

    def on_disconnect(self):
        pass

    def on_my_event(self, data):
        self.emit("my_response", data)


# async def req():
#     async with AsyncClient() as client:
#         resp = await client.get("http://127.0.0.1:5000/test")
#         print(resp)


# loop = asyncio.get_event_loop()

# loop.run_until_complete(req())

# loop.run_forever()
# print(r)
# print(r.status_code)
cl = socketio.Client()
cl.connect("http://127.0.0.1:5000/")
# cl.disconnect()
cl.connect("http://127.0.0.1:5000/", namespaces=["/chat", "/"])
# cl.connect("http://127.0.0.1:5000/", namespaces=["/test"])
# cl.register_namespace(MyCustomNamespace("/chat"))
# cl.register_namespace(MyCustomNamespace("/chat2"))
# cl.emit("kickme", namespace="/chat")
# cl.emit("dupa", "asd")
# cl.emit("do", {"a": "b"})
# cl.emit("do", {"a": "b"})
# cl2 = socketio.Client()
# cl2.connect("http://127.0.0.1:5000/")
# cl2.emit("do", {"a": "b"})
# cl2.emit("do", {"a": "b"})
# cl2.emit("do", {"a": "b"})
