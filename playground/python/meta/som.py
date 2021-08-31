import inspect


def f():
    pass


def verbose(func):
    def wrapped(*args, **kwargs):
        res = func(*args, **kwargs)
        signature = inspect.signature(func)
        print(signature)
        arg_names = inspect.getfullargspec(func).args
        if arg_names and arg_names[0] == "self":
            print("Running class %s", args[0].__class__.__name__)
            arg_names = arg_names[1:]
            args = args[1:]
        passed_args = ", ".join("{}={!r}".format(k, v) for k, v in zip(arg_names, args))
        passed_kwargs = ", ".join(["{}={!r}".format(k, v) for k, v in kwargs.items()])
        print(passed_args)
        print(passed_kwargs)
        return res

    return wrapped


class LoggedClass(type):
    def __new__(cls, clsname, bases, attrs):
        for k, v in attrs.items():
            print(k)
            print(callable(v))
            if not k.startswith("_") and callable(v):
                attrs[k] = verbose(attrs[k])
        return super().__new__(cls, clsname, bases, attrs)


class A(metaclass=LoggedClass):
    b = 10

    def __init__(self, a):
        self.a = a

    def calculate(self, a, b, c=20):
        pass

    def _calculate(self, a, b):
        pass

    @property
    def som(self):
        return 10


a = A(10)
# a.som
# a.calculate(10, b=20)
# a.calculate(10, 20, 30)
