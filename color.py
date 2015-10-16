import operator


class Color(object):
    def __init__(self, r, g, b, a):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def _operation(self, other, op):
        r = op(self.r, other.r)
        g = op(self.g, other.g)
        b = op(self.b, other.b)
        a = op(self.a, other.a)
        return Color(r, g, b, a)

    def __add__(self, other):
        return self._operation(other, operator.add)

    def __sub__(self, other):
        return self._operation(other, operator.sub)

    def __mul__(self, value):
        r, g, b, a = [i * value for i in [self.r, self.g, self.b, self.a]]
        return Color(r, g, b, a)

    def uint32(self):
        r = int(self.r * 255)
        g = int(self.g * 255)
        b = int(self.b * 255)
        a = int(self.a * 255)
        return a << 24 | b << 16 | g << 8 | r

    @staticmethod
    def rgba(rgba):
        r = ((rgba & 0xff000000) >> 24) / 255.0
        g = ((rgba & 0x00ff0000) >> 16) / 255.0
        b = ((rgba & 0x0000ff00) >> 8) / 255.0
        a = (rgba & 0x000000ff) / 255.0
        return r, g, b, a

    @staticmethod
    def red():
        return Color(1, 0, 0, 1)

    @staticmethod
    def green():
        return Color(0, 1, 0, 1)

    @staticmethod
    def blue():
        return Color(0, 0, 1, 1)

    @staticmethod
    def cyan():
        return Color(0, 1, 1, 1)

    @staticmethod
    def white():
        return Color(1, 1, 1, 1)
