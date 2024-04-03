from pydantic import BaseModel


class MyModel(BaseModel):
    a: int


def validate(model):
    def inner(foo):
        def wrap(param):
            resp = foo(param)
            print(resp)
            model(**resp)

        return wrap

    return inner


@validate(MyModel)
def foo(param):
    return {"a": param}


foo(4)
