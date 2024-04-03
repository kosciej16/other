from unittest import TestCase


class SomBase(TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("INIT")
        self.x = 1

    def setUp(self):
        self.x = 1


class Som(SomBase):
    def test_som(self):
        assert self.x == 1

    def test_som2(self):
        assert self.x == 1

    def test_som3(self):
        assert self.x == 1
