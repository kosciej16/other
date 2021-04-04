import pytest

from a import A, Z


@pytest.fixture
def class_a():
    return A(Z)
