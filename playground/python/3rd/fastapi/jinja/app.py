from pydantic import BaseModel
from fastapi import FastAPI, Request
import uvicorn
import asyncio
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/sttic", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def index_loader(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


class Model(BaseModel):
    a: str
    b: str


@app.get("/test")
async def test(r: Request):
    import time

    time.sleep(3)
    return "ABC"


print(app.openapi())

if __name__ == "__main__":
    kwargs = {"host": "0.0.0.0", "port": 5000}
    kwargs.update({"reload": True})
    uvicorn.run("app:app", **kwargs)
