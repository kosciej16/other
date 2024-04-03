import pytest
from litestar.di import Provide
from litestar.testing import create_test_client

import app

ITEMS = []


@pytest.fixture
def test_client():
    items = []

    def get_todo_list_mock():
        return ITEMS

    # the above seems to not work - no idea why

    try:
        # with TestClient(app=app.app) as client:
        with create_test_client(
            # route_handlers=[app.get_list, app.get_item, app.add_item, app.update_item],
            route_handlers=[app.get_item, app.add_item],
            dependencies={"todo_list": Provide(get_todo_list_mock)},
        ) as client:
            yield client
    finally:
        ITEMS.clear()


def test_create_and_get_item(test_client):
    task_name = "new"
    item = {"title": task_name, "done": False, "deadline": 4}
    r = test_client.post("/", json=item)
    assert r.status_code == 201

    r2 = test_client.get(f"/{task_name}")
    assert r2.status_code == 200
    assert r2.json() == item
