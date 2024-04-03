from db import Session
from sqlalchemy import nulls_last, text
from db.models.model import Model


def insert(s):
    s.add(Model())
    s.commit()


def foo():
    with Session() as s:
        # q = s.query(Model).order_by(nulls_last(Model.num))
        q = s.query(Model).order_by(text("num desc nulls last"))
        for row in q:
            print(row.num)
        # insert(s)


foo()
