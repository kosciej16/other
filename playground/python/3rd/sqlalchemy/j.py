from sqlalchemy.sql.expression import func
from db import Base, Session, engine
from pydantic import BaseModel
from dataclasses import dataclass
from psycopg.rows import class_row, dict_row
import psycopg
from sqlalchemy.sql import and_, text
from db.models.jsonb import WithJson
from db.models.model import Model
from db.models.relations import User, Ticket, Parent, Child
from sqlalchemy.sql import column, select, text


import logging

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.DEBUG)


def add(s):
    j = WithJson(json={"a": 1, "b": "som", "c": [3, 2, 1]})
    s.add(j)
    s.commit()


def reset():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    with Session() as s:
        add(s)
        add(s)


reset()
c = column("id")
c2 = column("num")
cols = {c, c2}
q = select(["*"], from_obj=text("with_json"))
# q = select([c], from_obj=text("with_json"))
q = q.distinct(*cols)
# # q = q.group_by(c)
# # print(type(q))
# # q = q.where(c < 3)
with Session() as s:
    res = s.execute(q)
    print(res.rowcount)
