# Simple Load Balancer Service

# You are asked to implement a load balancing service server.
# The server receives http requests and forwards them to one of several microservices.

# The server should have the following endpoints:
# /register- receives the parameters url path, ip address, port. After receiving this request
#            the load balancer will start sending some of the requests to the microservice
#            listening on the relevant ip and port.
# HTTP requests to other endpoints are forwarded to one of the microservices
# according to load balancing scheme, and replies are sent  back to the client.
# The initial load balancing scheme is Round Robin

# For example:
# Microservice A sends: http://<load balancer>/register "/test", ip address, port
# Microservice B sends: http://<load balancer>/register "/test2", ip address, port
# Microservice C sends: http://<load balancer>/register "/test", ip address, port
# Microservice D sends: http://<load balancer>/register "/test", ip address, port
# A client calls http://<load balancer>/test  -> This will be forwarded to either A,C or D

import asyncio
from dataclasses import dataclass
from typing import DefaultDict
from urllib.parse import urljoin

import uvicorn
from fastapi import BackgroundTasks, FastAPI, HTTPException, Request
from httpx import AsyncClient, TimeoutException
import os

# and then check the response...

TIMEOUT = 10
SCHEME = "http"


@dataclass
class RegisterIn:
    path: str
    ip: str
    port: int


app = FastAPI()


# could be deque instead
db = DefaultDict(list)
available_hosts = set()


class Strategy:
    def get_host(self, path):
        pass


class RoundRobinStrategy(Strategy):
    def get_host(self, path):
        if path in db:
            while db[path]:
                host = db[path].pop(0)
                if host in available_hosts:
                    db[path].append(host)
                    return host

        return None


strategy = RoundRobinStrategy()


async def healthcheck(host):
    while True:
        await asyncio.sleep(10)
        response = os.system("ping -c 1 " + host.rsplit(":", 1)[0])
        # We should unregister after many unsuccesful pings
        if response != 0:
            unregister(host)
            break


# we can list more like PATCH or PATCH_JSON
@app.api_route("/{path_name:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def catch_all(req: Request, path_name: str):
    host = strategy.get_host(path_name)
    # Not sure how to do that properly yet but it hasn't to be json - probably need to look into content-type
    # header and req.form()
    data = await req.json()
    while True:
        if not host:
            raise HTTPException(status_code=404, detail="No host registered")

        async with AsyncClient() as client:
            try:
                resp = await client.request(
                    req.method, urljoin(host, path_name), headers=req.headers, data=data, timeout=TIMEOUT
                )
            except TimeoutException:
                continue
            # we should handle some other statuses like 500 as well, to unregister microservice that has a bug

        return resp


@app.post("/register")
def register(data: RegisterIn, background_tasks: BackgroundTasks):
    # kinda mixed host with url, have no time to fix that naming issue
    host = f"{SCHEME}://{data.ip}:{data.port}"
    background_tasks.add_task(healthcheck, host)
    # We could check if its not registered already
    db[data.path].append(host)
    available_hosts.add(host)


def unregister(host):
    available_hosts.remove(host)


if __name__ == "__main__":
    uvicorn.run("som:app", host="0.0.0.0", port=9000, reload=True)
