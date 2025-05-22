import os
import sys
from queue import Queue
from signal import SIGINT, pthread_kill
from threading import Condition, Event, Thread
import threading
from time import sleep


def dec(a):
    while True:
        a.a -= 1
        print("dec", a.a)
        sleep(1)


def reset(a):
    while True:
        if a.a < 2:
            a.a = 5
            print("reset", a.a)
        sleep(1)


class A:
    def __init__(self):
        self.a = 5
        t = threading.Thread(target=dec, args=(self,))
        t.start()
        t = threading.Thread(target=reset, args=(self,))
        t.start()


class StopRequested(BaseException):
    pass


class Stoppable:
    def __init__(self, *args, **kwargs):
        self._wakeup_event = Event()
        self._stop_requested = False
        # call super() at the end to ensure all needed parameter would be set
        # just in case some class attempt to use them in the constructor
        super().__init__(*args, **kwargs)

    @property
    def stop_requested(self):
        return self._stop_requested

    def raise_if_stop_requested(self):
        if self.stop_requested:
            raise StopRequested()

    def request_stop(self):
        self._stop_requested = True
        self._wakeup_event.set()

    def sleep_with_stop_checking(self, interval, raise_on_stop=True):
        """Sleep "interval" seconds interruptable by "wakeup()" or "request_stop()" calls
        :param interval - number of seconds to sleep, "None" case infinitive waiting for wakeup or request_stop
        :param raise_on_stop - determine if funtion should raise StopRequested in case of stop request
        """
        # Useful knowledge: in STAR-5429 is described certain bug in python 3, which is rare and not dangerous
        # (occurs on SIGINT handling); STAR-5429 itself is closed as WON'T FIX, but as an alternative way of
        # fixing it the code below (active waiting) could be used:
        #
        # for _ in repeat_with_timeout(interval):
        #     if self._stop_requested or self._wakeup_event.is_set():
        #         break
        #     time.sleep(0.1)

        self._wakeup_event.wait(interval)

        if self._wakeup_event.is_set() and not self._stop_requested:
            self._wakeup_event.clear()
        if self.stop_requested and raise_on_stop:
            raise StopRequested()

    def wakeup(self):
        self._wakeup_event.set()


class StoppableThread(Stoppable, Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__started = False

    @property
    def started(self):
        return self.__started

    def start(self):
        super().start()
        self.__started = True


class MyThread(StoppableThread):
    def run(self):
        try:
            while True:
                print("ABC")
                self.sleep_with_stop_checking(1000)
        except StopRequested:
            print("STOPPED")
            import time

            time.sleep(3)
            print("FINISHED")


# t = MyThread()
# t.start()
# t1 = MyThread()
# t1.start()


# print("AAA")
# t.request_stop()
# # t1.request_stop()
# t.join(timeout=10e8)
# print("ABC")
# print("JOIN")
# t1.join()
# print("JOIN")
# print("AAA")


def queue_example():
    cv = Condition()
    q = Queue()
    q.put(2)
    q.put(3)

    def foo():
        el = q.get()
        print(el)
        sys.stdout.flush()
        sleep(1)
        q.put(el * 2)
        print("sleep", el)

    for _ in range(20):
        t = Thread(target=foo)
        t.start()

    print("WATEK")


class MyThread2(Thread):
    def run(self):
        sleep(300)


class MyManager:
    def __init__(self):
        self.threads = {}

    def start(self, id_):
        t = MyThread(id_)
        t.start()
        self.threads[id_] = t

    def kill(self, id_):
        t = self.threads[id_]
        print(t.native_id)
        pthread_kill(t.native_id, SIGINT)
        # __import__("pdb").set_trace()

    def get_alive(self):
        for t in self.threads.values():
            if not t.is_alive():
                print(f"NOT ALIVE {t.id}")


def foo():
    m = MyManager()
    m.start(1)
    m.start(2)
    print("O")
    m.kill(1)


A()

# print(os.getpid())
# th = MyThread2()
# th.start()
# th.name = "your name"
#
# th = MyThread2()
# th.start()
# th = MyThread2()
# th.start()


# m.start(2)
# while True:
#     m.get_alive()
#     sleep(3)
