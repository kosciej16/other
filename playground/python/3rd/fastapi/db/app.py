from fastapi import Depends, FastAPI, Query, Request, Body
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.schema import AddConstraint
from sqlalchemy.sql import text
from sqlalchemy.sql.schema import ForeignKeyConstraint, MetaData, Table


# from sqlalchemy_utils import database_exists, create_database

from db import Base, get_db, engine, Session as Ses

import sys
import asyncio
from fastapi.responses import PlainTextResponse

from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel
import uvicorn
from models.simple import Simple
from models.foreign import User, Client

from sqlalchemy.orm import Session, relationship


# if not database_exists(engine.url):
#     create_database(engine.url)
# else:
#     # Connect the database if exists.
#     engine.connect()
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

u = User()
name = "client_user_id_fkey"
# print(name)
fk = ForeignKeyConstraint((Client.user_id,), (User.id,), name=name)
t = Table(Client.__table__.name, MetaData(), fk)
s = Ses()
s.execute(AddConstraint(fk))
s.commit()

Client.__mapper__.add_property("user", relationship(User, backref="clients"))
t = Client(user=u)

s.add(t)
s.commit()


class Data(BaseModel):
    user: str


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/simple/{some_id}")
async def add(some_id: int, db: Session = Depends(get_db)):
    res = db.query(Simple).get(some_id)
    return res


@app.delete("/simple/")
async def delete(db: Session = Depends(get_db)):
    print("LOCKING")
    # db.execute(text("LOCK TABLE simple IN ACCESS EXCLUSIVE mode"))
    await asyncio.sleep(10)
    print("AFTER SLEEP")
    db.execute(text("TRUNCATE TABLE simple"))
    print("DELETE COMMITED")
    db.commit()


@app.post("/simple/")
async def create(num: int = Body(...), db: Session = Depends(get_db)):
    # await asyncio.sleep(5)
    s = Simple(num=num)
    # db.commit()
    db.add(s)
    print("BEFORE")
    db.commit()
    print("COMMITED")
    return s.id


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=9090, reload=True)
