import pytest
import const

const.ENVIRONMENT = "dev"


@pytest.mark.mark_a
def test_som():
    assert True


@pytest.mark.mark_b
def test_som2():
    assert True


@pytest.mark.mark_c
class TestSom:
    def test_som3(self):
        assert True

    def test_som4(self):
        assert False
