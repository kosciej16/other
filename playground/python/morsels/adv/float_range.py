import math


class float_range:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            start, stop = 0, start
        (self.start, self.stop, self.step) = (start, stop, step)

    def __repr__(self):
        return f"{type(self).__name__}({self.start}, {self.stop}, {self.step})"

    def __len__(self):
        return max(math.ceil((self.stop - self.start) / self.step), 0)

    def _attrs(self):
        if len(self) == 0:
            return ()
        return (self[0], self[-1], len(self))

    def __eq__(self, other):
        if not isinstance(other, (float_range, range)):
            return NotImplemented
        return self._attrs() == float_range._attrs(other)

    def _item(self, index):
        """Return item at given location, even if out of bounds."""
        return self.start + self.step * index

    def __getitem__(self, index):
        if isinstance(index, slice):
            start, stop, step = index.indices(len(self))
            return float_range(
                self._item(start),
                self._item(stop),
                self.step * step,
            )
        if 0 <= index < len(self):
            return self._item(index)
        if -len(self) <= index < 0:
            return self._item(len(self) + index)
        raise IndexError(f"index out of range: {index}")
