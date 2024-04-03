from unittest.mock import patch
import logging
import pytest


@pytest.fixture(autouse=True)
# @pytest.fixture(scope="session")
def default_session_fixture():
    pass
    print("DEFAULT")
    # with patch("som.fun_to_mock") as mock:
    #     yield {"run": mock}


def pytest_exception_interact(report):
    logging.error(f"Test eDUPDxception:\n{report.longreprtext}")


# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_call():
#     yield
#     pytest.fail("log problems found")


# def pytest_runtest_call(__multicall__):
#     try:
#         __multicall__.execute()
#     except KeyboardInterrupt:
#         raise
#     except:
#         logging.exception("pytest_runtest_call caught exception:")
#         raise
