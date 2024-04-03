from dataclasses import asdict
from pydantic import BaseModel

from abc import abstractmethod
from time import sleep
from celery import Celery, Task
from pydantic.dataclasses import dataclass


class AB(BaseModel):
    som: int

    def __json__(self):
        return self.json()


@dataclass
class Klasa:
    a: int
    ab: AB

    def __json__(self):
        return asdict(self)


class AddTask(Task):
    def run(self, params):
        return [555]


__tasks__ = [AddTask]


def create_celery_app() -> Celery:
    app = Celery()
    # app.config_from_object(celeryconfig)
    return app


# app = create_celery_app()
app = Celery("tasks", backend="redis://localhost", broker="redis://localhost")
# app = Celery("tasks")


def start():
    with Celery("tasks") as app:

        @app.task()
        def g(v):
            # raise TypeError
            # sleep(5)
            print("AAA")
            return v

        app.conf.update(backend_url="redis://localhost", broker_url="redis://localhost")
        app.Worker().start()


@app.task()
def g(v):
    # raise TypeError
    # sleep(5)
    print("AAA")
    return v


class BaseClass:
    def f(self, x):
        val = self.calc(x)
        return g.delay(val)

    @abstractmethod
    def calc(self, x):
        pass


class A(BaseClass):
    def calc(self, x):
        return 2 * x


class B(BaseClass):
    def calc(self, x):
        return 3 * x


@app.task
def add(x, y):
    # sleep(5)
    print("AAA")
    # return x + y
    return Klasa(a=1, ab=AB(som=10))
