from time import perf_counter
import builtins
import statistics


class Timer:
    def __init__(self, f=None):
        self.f = f
        self.runs = []
        self.elapsed = 0

    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, *args):
        self.elapsed = perf_counter() - self.start
        self.runs.append(self.elapsed)

    def __call__(self, *a, **kw):
        assert self.f
        with Timer(self.f) as t:
            res = self.f(*a, **kw)
        self.runs.append(t.elapsed)
        self.elapsed = t.elapsed
        return res

    @property
    def min(self):
        return builtins.min(self.runs)

    @property
    def max(self):
        return builtins.max(self.runs)

    @property
    def mean(self):
        return statistics.mean(self.runs)

    @property
    def media(self):
        return statistics.median(self.runs)


@Timer
def a(num):
    return 1


x = a(1)
print(x)
print(a.runs)
print(a.elapsed)
print(a.min)
