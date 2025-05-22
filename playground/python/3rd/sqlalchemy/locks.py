import time
from psycopg.errors import LockNotAvailable
from sqlalchemy import text
from sqlalchemy.exc import OperationalError
from db import Base, Session, engine
import logging

from db.models.simple import Simple, Simple2

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.DEBUG)


def add(s, num):
    u = Simple(num=num)
    s.add(u)
    u = Simple2(num=num)
    s.add(u)
    s.commit()


def reset():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    with Session() as s:
        add(s, 1)
        add(s, 2)


# reset()
with Session() as s:
    s.execute(text("LOCK TABLE simple IN EXCLUSIVE MODE"))
    i = 0
    while True:
        time.sleep(3)
        print("Loop")
        with Session() as s2:
            # s.commit()
            try:
                if i == 0:
                    s2.execute(text("SET lock_timeout = '0.1s'"))
                    i += 1
                s2.execute(text("TRUNCATE TABLE simple2"))
                s2.commit()
                # break
            except OperationalError as e:
                s2.rollback()
                print("HAHA")
