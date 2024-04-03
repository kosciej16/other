import pytest
from entry import Entry
from arch import Arch

# from arch import Arch
from unittest.mock import patch
from a import A


# def test_mock():
#     with patch("b.B.foo", new="a"):
#         a = A()
#         assert a.foo() == 10


def test_arch_mock():
    # e = Entry()
    # e.start()
    a = Arch()
    a.setup()
    with patch("arch.Arch.setup", new=lambda _: print("MOCKED")):
        a.setup()
        # with patch.object(Arch, "setup", new=lambda _: print("MOCKED")):
        # with patch.object(Arch, new="a"):
        # e.start()
