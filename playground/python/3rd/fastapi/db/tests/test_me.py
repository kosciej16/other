import os
from unittest.mock import patch

from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


class TestMe:
    def setup_method(self):
        os.environ["FOO"] = "A"

    def test_1(self):
        resp = client.get("/")
        assert resp.json() == 1

    def test_2(self):
        with patch.dict(os.environ):
            resp = client.get("/")
            assert resp.json() is None

    def test_3(self):
        resp = client.get("/")
        assert resp.json() == 1
