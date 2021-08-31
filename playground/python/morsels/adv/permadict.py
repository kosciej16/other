from collections import UserDict
from typing import Mapping


class PermaDict(UserDict):
    def __init__(self, *args, silent=False, **kwargs):
        super().__init__(*args, **kwargs)
        self.silent = silent

    def __setitem__(self, k, v):
        print(k)
        if k in self:
            if self.silent:
                return
            raise KeyError
        super().__setitem__(k, v)

    def update(self, *args, force=False, **kwargs):
        if force:
            if args:
                if isinstance(args[0], Mapping):
                    for (k, v) in args[0].items():
                        super().__setitem__(k, v)
                else:
                    for (k, v) in args[0]:
                        super().__setitem__(k, v)
        else:
            if args:
                super().update(args[0])
        for k, v in kwargs.items():
            super().__setitem__(k, v)

    def force_set(self, k, v):
        super().__setitem__(k, v)


locations = PermaDict({"David": "Boston"})
locations.update([("David", "Amsterdam"), ("Asheesh", "SF")], force=True)
print(locations)
# locations["David"] = "Amsterdam"
