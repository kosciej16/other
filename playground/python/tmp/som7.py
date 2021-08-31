import threading


class OuterClass:
    class DecoratorTest:
        def __init__(self, fget, fset=None) -> None:
            self.fget = fget
            self.fset = fset
            self.event = threading.Event()

        def __get__(self, obj, objtype=None):
            print("A")
            print(id(self.event))
            return self

        def __set__(self, obj, value):
            print("S")
            self.fset(obj, value)
            print(id(self.event))
            self.event.set()
            self.event.clear()

        def setter(self, fset):
            return type(self)(self.fget, fset)

    def __init__(self):
        self.random_value = 10

    @DecoratorTest
    def test_property(self):
        return self.random_value * 2

    @test_property.setter
    def test_property(self, value):
        self.random_value = value


class_iteration = OuterClass()


def test_funct():
    class_iteration.test_property.event.wait()
    print("Changed!")


threading.Thread(target=test_funct).start()

# class_iteration.test_property = 100
