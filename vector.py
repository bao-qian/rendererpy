import operator
from math import sqrt


class Vector:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x, self.y, self.z = x, y, z

    def _operation(self, other, op):
        x = op(self.x, other.x)
        y = op(self.y, other.y)
        z = op(self.z, other.z)
        return Vector(x, y, z)

    def __add__(self, other):
        return self._operation(other, operator.add)

    def __sub__(self, other):
        return self._operation(other, operator.sub)

    def __mul__(self, other):
        x, y, z = [i * other for i in [self.x, self.y, self.z]]
        return Vector(x, y, z)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def cross(self, other):
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x
        return Vector(x, y, z)

    def dot(self, other) -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z

    def length(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def normalize(self):
        factor = 0
        length = self.length()
        if length > 0:
            factor = 1 / length
        return Vector(self.x * factor, self.y * factor, self.z * factor)


