import schedule
import time

print("IMPORTED")


def f():
    print("B")
    return schedule.CancelJob


schedule.every().minute.do(f)
