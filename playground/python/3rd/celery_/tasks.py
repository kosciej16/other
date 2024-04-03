from pydantic import BaseModel
import concurrent.futures
import time

import celery
from app import app
from celery.registry import tasks
import threading


@app.task
def add(x, y):
    return x + y


class A(BaseModel):
    def __init__(self, som):
        self.som = som

    def __json__(self):
        return self.json()


def slow_foo(param):
    # time.sleep(3)
    return A(10)


class AddTask(celery.Task):
    def run(self, params):
        try:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                futures = [executor.submit(slow_foo, param=el) for el in params]
                # time.sleep(5)
                return [fut.result() for fut in futures]
        except:
            return [555]


AddTask = app.register_task(AddTask())
