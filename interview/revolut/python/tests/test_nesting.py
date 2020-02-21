import json
import os
from pathlib import Path

import pytest

from nest import nest_dict

DATA_PATH = Path(os.path.dirname(os.path.realpath(__file__))) / 'data'

INPUT_FILE_PATH = DATA_PATH / 'input.json'
EXPECTED_FILE_PATH = DATA_PATH / 'expected.json'


@pytest.fixture
def test_data():
    with open(INPUT_FILE_PATH) as f:
        return json.load(f)


def test_nesting_wth_no_levels(test_data):
    assert nest_dict(test_data, []) == test_data


def test_nesting_wth_one_level(test_data):
    with open(EXPECTED_FILE_PATH) as f:
        assert nest_dict(test_data, ['country']) == json.load(f)
