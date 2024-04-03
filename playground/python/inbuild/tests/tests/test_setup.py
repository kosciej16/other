import pytest


@pytest.fixture
def foo():
    print("BEF")
    yield
    pytest.fail()


class TestClass:
    def setup(self):
        print("AAA")
        pass

    def test_foo(self, foo):
        print("CCC")
        assert False
