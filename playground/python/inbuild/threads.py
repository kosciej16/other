from threading import Condition, Thread
from time import sleep

cv = Condition()


def f():
    while True:
        print("S")
        sleep(3)
        print("A")
        cv.acquire()
        print("N")
        cv.notify()
        print("R")
        cv.release()


t = Thread(target=f)
t.start()
while True:
    sleep(2)
    print("ACQU")
    with cv:
        print("WAIT")
        cv.wait()
    print("AFTER")
