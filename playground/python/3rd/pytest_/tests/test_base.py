from tests.base import Base


class TestSom(Base):
    def test_foo(self):
        assert self.som == 0
