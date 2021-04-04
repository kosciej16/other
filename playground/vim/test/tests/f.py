from funs import f
from unittest.mock import patch


def test_f():
    with patch("funs.rand2", return_value=10) as m:
        # with patch("random.randint", return_value=10) as m:
        m.return_value = 10
        assert f() == 10
