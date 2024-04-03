import pytest


class TestMarkers:
    @pytest.mark.long
    def test_simple_marker(self):
        assert True
