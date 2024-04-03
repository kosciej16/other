# import pytest


# class Thing:
#     def __init__(self, val) -> None:
#         self.val = val
#         print(f"Made a thing with val {val}", end=" ")


# values = [1, 2]


# @pytest.fixture(scope="class", params=values)
# def thing(request):
#     return Thing(request.param)


# class TestThing:
#     @pytest.mark.parametrize(
#         "thing_instance,expected_val",
#         [(pytest.lazy_fixture("thing"), [1, 2])],
#     )
#     def test_thing_val(self, thing_instance, expected_val, request):
#         test_nr = int(request.node.name.split("[")[-1].split("]")[0][-1])
#         assert thing_instance.val == expected_val[test_nr - 1]

#     @pytest.mark.parametrize(
#         "thing_instance",
#         [
#             (pytest.lazy_fixture("thing")),
#         ],
#     )
#     def test_thing_useless(self, thing_instance):
#         assert thing_instance
