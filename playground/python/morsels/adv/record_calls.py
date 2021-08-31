from typing import Any, Optional, ClassVar
from dataclasses import dataclass
from functools import wraps


@dataclass
class Call:
    NO_RETURN: ClassVar[Any] = object()
    args: tuple
    kwargs: dict
    return_value: Any
    exception: Optional[Exception]


def record_calls(func):
    calls = []

    @wraps(func)
    def wrapped(*args, **kwargs):
        exc = None
        try:
            val = func(*args, **kwargs)
        except Exception as e:
            exc = e
            val = Call.NO_RETURN
        a = Call(args, kwargs, val, exc)
        calls.append(a)
        wrapped.call_count += 1
        if a.exception:
            raise a.exception
        return val

    setattr(wrapped, "call_count", 0)
    setattr(wrapped, "calls", calls)
    return wrapped


@record_calls
def greet(name="world"):
    """Greet someone by their name."""
    print(f"Hello {name}")


@record_calls
def cube(n):
    return n ** 3


cube(4)
try:
    cube(None)
except:
    pass
print(cube.calls)
