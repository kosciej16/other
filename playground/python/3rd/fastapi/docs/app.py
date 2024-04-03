from swaggertools import resolve
from fastapi.openapi.utils import get_openapi

from fastapi import FastAPI
from starlette.routing import Mount
from app1.app import app1
from app2.app import app2
import uvicorn

app = FastAPI()
# print(app1.openapi())
# print(app2.openapi())

from starlette.applications import Starlette

# app = Starlette(routes=[Mount("/api1", app1), Mount("/api2", app2)])


def custom_openapi():
    openapi_schema = get_openapi(
        title="Custom title",
        version="2.5.0",
        description="This is a very custom OpenAPI schema",
        routes=[*app1.routes, *app2.routes],
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

    # api = app1.openapi()
    # from pprint import pprint

    # pprint(api)
    # api2 = app2.openapi()
    # pprint(api2)
    # api["paths"].update(api2["paths"])

    # pprint(api)
    # api["components"].update(api2["components"])

    # return api


app.openapi = custom_openapi
# custom_openapi()

if __name__ == "__main__":
    kwargs = {"host": "0.0.0.0", "port": 5000}
    kwargs.update({"reload": True})
    uvicorn.run("app:app", **kwargs)
