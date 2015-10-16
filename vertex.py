import operator

from color import Color
from vector import Vector


class Vertex(object):
    def __init__(self, position: Vector, normal: Vector, u: float, v: float, color: Color = Color.cyan()):
        self.position = position
        self.normal = normal
        self.u = u
        self.v = v
        self.color = color

    def _operation(self, other, op):
        position = op(self.position, other.position)
        normal = op(self.normal, other.normal)
        u = op(self.u, other.u)
        v = op(self.v, other.v)
        color = op(self.color, other.color)
        return Vertex(position, normal, u, v, color)

    def __add__(self, other):
        return self._operation(other, operator.add)

    def __sub__(self, other):
        return self._operation(other, operator.sub)

    def __mul__(self, value):
        position = self.position * value
        normal = self.normal * value
        u = self.u * value
        v = self.v * value
        color = self.color * value
        return Vertex(position, normal, u, v, color)
