import pytest


class Base:
    def __init__(self):
        self.som = None

    # @pytest.fixture(scope="function", autouse=True)
    # def foo(self):
    #     self.som = 0
