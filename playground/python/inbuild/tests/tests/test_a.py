import pytest

from a import A


@pytest.fixture
def a():
    return A()


def test_a(a):
    assert a.f() == 1
    assert False
