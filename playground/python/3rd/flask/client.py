import requests
import socketio

cl = socketio.Client()


@cl.on("event_name")
def foo(data):
    print(f"client 1 {data}")


cl.connect("http://127.0.0.1:5000/")  # server prints "on connect"
