from unittest.mock import patch
import pytest


@pytest.fixture(autouse=True)
# @pytest.fixture(scope="session")
def default_session_fixture():
    print("DEFAULT")
    with patch("som.fun_to_mock") as mock:
        yield {"run": mock}
