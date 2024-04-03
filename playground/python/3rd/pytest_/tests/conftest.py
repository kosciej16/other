import pytest
import json
import glob

files = glob.glob("tests/res/")


@pytest.fixture(params=files)
def test_data(request):
    with open(request.param) as f:
        return json.load(f)


@pytest.fixture
def good_response(test_data):
    # process test_data in some way -- Ex. mimic the content of a Response obj
    return response


@pytest.fixture(scope="function")
def x(request):
    print(request)
    print(dir(request))
    return request.param * 3


@pytest.fixture(scope="function")
def y(request):
    return request.param * 2
