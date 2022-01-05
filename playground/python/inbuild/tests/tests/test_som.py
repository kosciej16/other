import asyncio
from unittest.mock import patch
import pytest
import const
from som import run, arun, d
from som import f

const.ENVIRONMENT = "dev"


def test_som():
    assert True


def test_som2():
    assert True


class TestSom:
    def test_som3(self):
        assert True


def test_mock(default_session_fixture):
    default_session_fixture["run"].assert_not_called()
    run()
    default_session_fixture["run"].assert_called()


def test_mock2(default_session_fixture):
    default_session_fixture["run"].assert_not_called()
    run()
    default_session_fixture["run"].assert_called()


@pytest.mark.asyncio
async def test_async():
    with patch("som.atask") as mock:
        await arun()
        mock.assert_called_with()


@patch("uuid")
def test_f(mock):
    assert f() == 1
