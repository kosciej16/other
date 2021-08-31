from dataclasses import dataclass
import numbers


@dataclass(frozen=True)
class Vector:
    x: int
    y: int
    z: int
    __slots__ = ["x", "y", "z"]

    def __iter__(self):
        return iter((self.x, self.y, self.z))

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        raise NotImplemented

    def _sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        raise NotImplemented

    def __mul__(self, other):
        if isinstance(other, numbers.Number):
            return Vector(self.x * other, self.y * other, self.z * other)
        raise NotImplemented

    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, numbers.Number):
            return Vector(self.x / other, self.y / other, self.z / other)
        raise NotImplemented


v = Vector(1, 2, 3)
print(v)
x, y, z = v
print(v == Vector(1, 2, 4))
print(v == Vector(1, 2, 3))
print(Vector(1, 2, 3) + Vector(4, 5, 6) == Vector(5, 7, 9))
print(Vector(1, 2, 3) / 4)
print(4 * Vector(1, 2, 3))
