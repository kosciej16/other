import pytest
import responses
import requests


@pytest.fixture
def mocked_responses():
    with responses.RequestsMock() as rsps:
        yield rsps


@pytest.fixture
def t(mocked_responses):
    mocked_responses.add(
        responses.GET, "http://twitter.com/api/1/foobar", json={"error": "not found"}, status=404
    )
    mocked_responses.add(
        responses.GET, "http://twitter.com/api/1/foobar", json={"dupa": "not found"}, status=404
    )
    mocked_responses.add(
        responses.GET, "http://twitter.com/api/1/foobar", json={"error": "not found"}, status=404
    )
    mocked_responses.add(
        responses.GET, "http://twitter.com/api/1/foobar", json={"dupa": "not found"}, status=404
    )
    mocked_responses.add(
        responses.GET, "http://twitter.com/api/1/foobar", json={"dupa": "not found"}, status=404
    )
    mocked_responses.add(
        responses.GET, "http://twitter.com/api/1/foobar", json={"dupa": "not found"}, status=404
    )
    mocked_responses.add(
        responses.GET, "http://twitter.com/api/1/foobar", json={"error": "not found"}, status=404
    )
    # mocked_responses.add(
    #     responses.GET, "http://twitter.com/api/1/foobar", json={"error": "not found"}, status=404
    # )


# @responses.activate
def test_simple(t):
    # responses.add(
    #     responses.GET, "http://twitter.com/api/2/foobar", json={"error": "not found"}, status=404
    # )
    # responses.add(
    #     responses.GET, "http://twitter.com/api/1/foobar", json={"error": "not found"}, status=404
    # )

    resp = requests.get("http://twitter.com/api/1/foobar")
    print(resp.json())
    resp = requests.get("http://twitter.com/api/1/foobar")
    print(resp.json())
    resp = requests.get("http://twitter.com/api/1/foobar")
    print(resp.json())
    resp = requests.get("http://twitter.com/api/1/foobar")
    print(resp.json())
    # requests.get("http://twitter.com/api/2/foobar")
    assert resp.json() == {"error": "not found"}

