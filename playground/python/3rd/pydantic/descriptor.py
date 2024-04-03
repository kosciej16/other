from dataclasses import dataclass


class Descriptor:
    def __get__(self, obj, objtype=None):
        print("GET")
        return obj._a

    def __set__(self, obj, value):
        print("SET")
        obj._a = value


@dataclass
class MyDataclass:
    x: int
    d = Descriptor()

    def dict(self):
        return self.d


m = MyDataclass(10, d=3)
# m.d = 9
print(m.dict())
# print(asdict(m))

# How to make it works?
class MyModel(BaseModel):
    d = Descriptor()

    class Config:
        arbitrary_types_allowed = True


# if __name__ == "__main__":
#     item = MyDataclass()
#     item.d = 1
#     print(item.d)

#     item = MyModel()
#     item.d = 1  # ValueError: "MyModel" object has no field "d"
#     print(item.d)
