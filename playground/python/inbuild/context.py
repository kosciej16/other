from time import perf_counter, sleep


class Timer:
    def con(self):
        pass

    def __enter__(self):
        self.start = perf_counter()
        print(self.start)
        return self

    @property
    def elapsed(self):
        return perf_counter() - self.start

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass


with Timer() as t:
    while True:
        print(t.elapsed)
        if t.elapsed > 2:
            break
        sleep(1)
