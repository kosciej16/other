from sqlalchemy.sql import text
import time
from threading import Thread

from db import Base, engine, Session

from models.simple import Simple


Base.metadata.create_all(engine)


def get(some_id: int):
    with Session() as s:
        return s.query(Simple).get(some_id)


def delete():
    print("DELETE")
    with Session() as s:
        s.execute(text("LOCK TABLE simple IN ACCESS EXCLUSIVE mode"))
        s.execute(text("TRUNCATE TABLE simple"))
        time.sleep(10)
        s.commit()


def create(num: int):
    print("CREATE")
    with Session() as s:
        mode = Simple(num=num)
        s.add(mode)
        s.commit()
        print("CREATE COMMITED")
        return mode.id


if __name__ == "__main__":
    t = Thread(target=delete)
    t.start()
    print("A")
    time.sleep(1)
    mid = create(5)
    # res = get(mid)
    # print(res)
