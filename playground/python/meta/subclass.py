from typing import Union, cast, overload

import pytest


class UserWrapper:
    def get_user(self):
        ...


class EventWrapper:
    def get_event(self):
        ...


class OtherWrapper:
    def get_other(self):
        ...


class Base:
    # @pytest.fixture(autouse=True)
    def setup(self, cliet):
        self.client = cliet

    # def __init_subclass__(cls, wrapper: Union[EventWrapper, UserWrapper, OtherWrapper], **kwargs):

    @overload
    def __init_subclass__(cls, w1: UserWrapper) -> None:
        ...

    @overload
    def __init_subclass__(cls, w1: EventWrapper) -> None:
        ...

    def __init_subclass__(cls, w1):
        cls.wrapper = w1
        # cls.wrapper = wrapper


class TestUserApi(Base):
    def seup(self):
        self.wrapper = UserWrapper()

    def test_create(self):
        resp = self.client.post(...)
        assert self.wrapper.get_user(resp.json())
        self.wrapper.get_user()


class TestEventApi(Base, w1=EventWrapper()):
    def setup(self):
        assert isinstance(self.wrapper, EventWrapper)

    def test_create(self):
        resp = self.client.post(...)
        assert self.wrapper.get_event()


# class TestOtherApi(Base, wrapper=OtherWrapper()):
#     def test_create(self):
#         resp = self.client.post(...)
#         assert self.wrapper.get_other()
