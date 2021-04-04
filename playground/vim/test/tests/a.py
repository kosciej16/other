from unittest import mock
from time import sleep
from a import A
import a
import b


# def test_a(class_a):
#     with mock.patch(A.f.c, return_value="4"):
#         class_a.f() == 0


@mock.patch.object(a.B, "__init__", return_value=None)
def test_aa(o, class_a):
    class_a.f()
    print(o)
    # print(o.call_kwargs_list)
    # print(o.call_args_list[0][0][1])
    print(o.call_args_list)
    args, kwargs = o.call_args_list[0]
    print(kwargs)
    print(args)


# @mock.patch.object(a.B, "foo", return_value=100)
@mock.patch("a.B.foo", return_value=102)
def test_ag(o, class_a):
    res = class_a.g()
    assert res == 100
    # print(o)
    # # print(o.call_kwargs_list)
    # # print(o.call_args_list[0][0][1])
    # print(o.call_args_list)
    # args, kwargs = o.call_args_list[0]
    # print(kwargs)
    # print(args)


# aa = A(10)
# aa.f()
# aa.f()
# # class_a.B("a")
# print(aa.b)
# print(aa.b.call_args_list)
# print(aa.b.method_calls)
# print(aa.b.mock_calls)
# assert False


class Base:
    var = 1

    # def setup_method(self, class_a):
    #     self.var = -1

    def test_var(self, class_a):
        assert class_a.f() == 100


@mock.patch.object(A, "f", return_value=100)
class Test2(Base):
    var = 5

    def test_var(self, my_mock, class_a):
        super().test_var(class_a)
