from unittest.mock import patch
from f import g


@patch("f.A")
def f(a):
    print(a)
    g()
    pass


f()
