from collections import OrderedDict


class Unpacker(OrderedDict):
    def __getitem__(self, k):
        if isinstance(k, tuple):
            return tuple(self[kk] for kk in k)
        return super().__getitem__(k)

    def __setitem__(self, k, v):
        if isinstance(k, tuple):
            vl = list(v)
            if len(k) != len(vl):
                raise ValueError
            for kk, vv in zip(k, vl):
                self[kk] = vv
            return
        super().__setitem__(k, v)

    def __getattr__(self, k):
        return self.get(k)

    def __setattr__(self, k, v):
        self[k] = v

    def __iter__(self):
        return iter(self.values())

    def __repr__(self):
        s = [f"{k}={repr(v)}" for k, v in self.items()]
        return f"Unpacker({', '.join(s)})"


d = {"hello": 4, "hi": 5}
u = Unpacker(d)
print(u["hello"])
print(u.hi)
u["hello"] = 8
print(u["hello"])

coordinates = OrderedDict([("x", 34), ("y", 67)])
print(coordinates)
point = Unpacker(coordinates)
x_axis, y_axis = point
x_axis, y_axis
print(x_axis, y_axis)

row = Unpacker({"a": 234, "b": 54})
row["a"] = 11
row["c"] = "abc"
print(row)

row = Unpacker({"a": 234, "b": 54})
row["b", "a", "c"] = (11, 22)
print(row)
