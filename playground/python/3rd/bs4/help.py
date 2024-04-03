# Base class with common behavior
class FooBase:
    @classmethod
    def method1(cls, data):
        return data


# specialized classes
class FooA(FooBase):
    @classmethod
    def method2(cls, data):
        return data


class FooB(FooBase):
    # define extra methods
    pass
