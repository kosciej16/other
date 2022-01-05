from abc import abstractmethod
from time import sleep
from celery import Celery, Task


def create_celery_app() -> Celery:
    app = Celery()
    # app.config_from_object(celeryconfig)
    return app


# app = create_celery_app()
app = Celery("tasks", backend="redis://localhost", broker="redis://localhost")


@app.task()
def g(v):
    raise TypeError
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
    return x + y
