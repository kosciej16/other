from dataclasses import dataclass
import functools


@dataclass
class Context:
    exception: Exception = None
    traceback: str = None


class ContextDecorator(object):
    def __call__(self, f):
        @functools.wraps(f)
        def decorated(*args, **kwds):
            with self:
                return f(*args, **kwds)

        return decorated


class suppress(ContextDecorator):
    def __init__(self, *args):
        self.exc = args
        self.context = Context()

    def __enter__(self):
        return self.context

    def __exit__(self, exc_type, exc_val, traceback):
        if exc_type is None or any([issubclass(exc_type, e) for e in self.exc]):
            if exc_type is not None:
                self.context.exception = exc_type(exc_val)
                self.context.traceback = traceback
            return True
        raise exc_type


@suppress(TypeError)
def len_or_none(thing):
    return len(thing)


with suppress(ValueError, NameError) as context:
    x = int("A")
    print("a")
    print("It's nice to meet you,", name)
    print("b")

print(context.exception)
print(len_or_none("hello"))
print(len_or_none(1))
