from typing import reveal_type
from sqlalchemy import TEXT, Column, Integer, MetaData, Table, desc
from sqlalchemy.orm import Query
from sqlalchemy.sql.expression import func
from sqlalchemy.sql.functions import count
from db import Base, Session, engine
from pydantic import BaseModel
from dataclasses import dataclass
from psycopg.rows import class_row, dict_row
import psycopg
from sqlalchemy.sql import and_, text
from db.models.model import Model
from db.models.relations import User, Ticket, Parent, Child
from sqlalchemy.sql import column, select, text


import logging

from utils import query_to_sql

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.DEBUG)


sql = """
SELECT 
    count(*) OVER (PARTITION BY name) same_name_count, 
    count(*) OVER (RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS count_all
FROM
    {tbl}
ORDER BY
    same_name_count DESC
LIMIT 1;
"""


def add(id, other_id, s):
    p = Parent(id=id, other_id=other_id)
    c = Child(id=id, other_id=other_id * 2 - 1)
    if id != 4:
        p.child = c
    s.add(p)
    s.commit()


def reset():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    with Session() as s:
        add(1, 1, s)
        add(2, 1, s)
        add(3, 2, s)
        add(4, 3, s)


def tmp_table(s, q, tbl):
    columns_stmt = ", ".join(f"{col.name} {col.type}" for col in cols)
    create_table_stmt = text(f"CREATE TEMP TABLE {table_name} ({columns_stmt}) ON COMMIT DROP")
    s.execute(create_table_stmt)
    s.execute(f"INSERT INTO {table_name} values (1, 'abc'), (1, 'def'), (10, 'x')")
    return q.join(tbl, Parent.id == tbl.c.myid, isouter=True)
    # return q.join(tbl, Parent.id == tbl.c.myid).distinct(tbl.c.myid)


@dataclass
class Person:
    # class Person(BaseModel):
    id: int
    name: str
    address: str


# reset()
c = column("other_id")


# q = select([c], from_obj=text("Parent"))
# q = q.distinct()
# q = q.group_by(c)
# print(type(q))
# q = q.where(c < 3)
def subqueries():
    with Session() as s:
        # q = s.query(Parent.id, Parent.other_id)
        # q = q.distinct(c)
        # q = q.order_by(None)
        # q = q.order_by("other_id")
        # q = q.order_by("id")
        # q = q.order_by("other_id")
        # print(q.column_descriptions)
        # new_q = Query(q.column_descriptions, q.session).select_from(q._from_obj[0])
        # new_q = new_q.order_by("other_id")

        # __import__("pdb").set_trace()
        # for x in q:
        #     print(x)
        # print(x.__dict__)
        table_name = "testowa"
        cols = [Column("myid", Integer), Column("name", TEXT)]
        tbl = Table(table_name, MetaData(), *cols)
        columns_stmt = ", ".join(f"{col.name} {col.type}" for col in cols)
        create_table_stmt = text(f"CREATE TEMP TABLE {table_name} ({columns_stmt}) ON COMMIT DROP")
        s.execute(create_table_stmt)
        # s.execute(text(f"insert into {table_name} values (1, 'a'), (1, 'e'), (1, 'a'), (2, 'b')"))

        # q = s.query(Parent).join(Child, Parent.id == Child.id)
        subquery = s.query(tbl).distinct().subquery()
        q = s.query(Parent.id, subquery.c.name).join(subquery, Parent.id == subquery.c.myid)
        # q = s.query(Parent)
        # q = tmp_table(s, q, tbl)
        # q_str = query_to_sql(s, q)
        # print(q_str)
        # s.execute(f"CREATE TABLE Tabelka AS {q_str};")

        # q = select(["*"], from_obj=text("Tabelka"))
        # res = s.execute(q).all()
        # print(res)
        for x in q:
            print(x)

        el = (
            s.query(count().label("c"))
            .select_from(tbl)
            .where(tbl.c.name == "5")
            .group_by(tbl.c.name)
            .order_by(desc("c"))
            .limit(1)
        )
        print(el)
        res = s.execute(text(sql.format(tbl="testowa"))).mappings().first()
        print(res)
        print(tbl.name)
        # print(x.__dict__)
        # print(q.rowcount)
        # print(q.scalar())


# def sorting():
#     with Session() as s:


# url = "postgresql://postgres:pass@127.0.0.1:35432"
# conn = psycopg.connect(url, row_factory=class_row(Person))
# conn = psycopg.connect(url, row_factory=dict_row)
# cur = conn.cursor(row_factory=class_row(Person))
# res = conn.execute("select 'John Doe' as name, 33 as address").fetchone()
# res = cur.execute("select 'John Doe' as name, 33 as address").fetchone()
# res = cur.execute("select id, name, address FROM person AS data (id, name, address) where id=1").fetchone()
# print(res)

# with conn.cursor(row_factory=class_row(Person)) as cursor:
#     result = cursor.execute(
#         """
#         SELECT (id, name, address)
#         FROM person AS data (id, name, address)
#         WHERE id = 1;"""
#     ).fetchone()


# with Session() as s:
#     # p = s.query(Parent.other_id, Child.parent_id)
#     # p = s.query(Parent, Child).join(Parent, and_(Parent.id == Child.parent_id, Parent.other_id == 2))
#     p = s.query(Parent, Child).join(Child.parent)
#     print(p)
#     for q in p:
#         print("RECORD")
#         print(q[0].__dict__)
#         print(q[1].__dict__)
#         # print(q.__dict__)

# res = s.execute(text("select * from test() as t(s1 int, s2 int, s3 int)"))
# for x in res.fetchall():
#     print(x)
# s.execute("insert into model values(1, 1)")

# reset()
subqueries()
