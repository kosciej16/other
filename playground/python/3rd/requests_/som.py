from client import Client

local = "http://127.0.0.1:5000"


m = Client(base_url=local)
m.get("test")
