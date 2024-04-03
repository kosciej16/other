import pytest


@pytest.mark.parametrize("param", ["value1", "value2", "value3"])
class TestMe:
    # Override the setup method
    def setup_method(self, method):
        # Check the name of the test method
        if method.__name__ == "test_specific":
            # Modify the parameter for this specific test
            self.param = "specific_value"

    # This test will use the class parametrization ('value1', 'value2', 'value3')
    def test_general(self, param):
        assert param in ["value1", "value2", "value3"]

    # This test will use the specific value set in setup_method
    def test_specific(self, param):
        assert self.param == "specific_value"
