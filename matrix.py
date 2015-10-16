from math import *

from vector import Vector


class Matrix:
    # def __init__(self):
    #     self.length = 16
    #     self.p = np.zeros(self.length)

    def __init__(self, values):
        # todo??
        self.length = 16
        self.p = values

    def __eq__(self, other):
        equal = True
        for i in range(self.length):
            equal = equal and self.p[i] == other.p[i]
        return equal

    def __mul__(self, other):
        values = []
        for index in range(self.length):
            i = index // 4
            j = index % 4
            values.append(self.p[i * 4]     * other.p[j] +
                          self.p[i * 4 + 1] * other.p[1 * 4 + j] +
                          self.p[i * 4 + 2] * other.p[2 * 4 + j] +
                          self.p[i * 4 + 3] * other.p[3 * 4 + j])
        return Matrix(values)

    def __repr__(self):
        text = ""
        end = 0
        for i in range(4):
            start = end
            end = (self.length * (i+1)) // 4
            text += str(self.p[start:end]) + '\n'
        return text

    @staticmethod
    def identity():
        values = [
            1, 0, 0, 0,
            0, 1, 0, 0,
            0, 0, 1, 0,
            0, 0, 0, 1,
        ]
        return Matrix(values)

    @staticmethod
    def lookAtLH(eye: Vector, target: Vector, up: Vector):
        zaxis = (target - eye).normalize()
        xaxis = up.cross(zaxis).normalize()
        yaxis = zaxis.cross(xaxis).normalize()

        xeye = -xaxis.dot(eye)
        yeye = -yaxis.dot(eye)
        zeye = -zaxis.dot(eye)

        values = [
            xaxis.x(), yaxis.x(), zaxis.x(), 0,
            xaxis.y(), yaxis.y(), zaxis.y(), 0,
            xaxis.z(), yaxis.z(), zaxis.z(), 0,
            xeye,    yeye,    zeye,    1,
        ]

        return Matrix(values)

    @staticmethod
    def perspectiveFovLH(fieldOfView: float, aspect: float, znear: float, zfar: float):
        height = 1 / tan(fieldOfView / 2)
        width = height / aspect
        values = [
            width,  0,      0,                                  0,
            0,      height, 0,                                  0,
            0,      0,      zfar / (zfar - znear),              1,
            0,      0,      (znear * zfar) / (znear - zfar),    0,
        ]
        return Matrix(values)

    @staticmethod
    def rotationX(angle: float):
        s = sin(angle)
        c = cos(angle)
        values = [
            1, 0,  0, 0,
            0, c,  s, 0,
            0, -s, c, 0,
            0, 0,  0, 1,
        ]
        return Matrix(values)

    @staticmethod
    def rotationY(angle: float):
        s = sin(angle)
        c = cos(angle)
        values = [
            c, 0, -s, 0,
            0, 1, 0,  0,
            s, 0, c,  0,
            0, 0, 0,  1,
        ]
        return Matrix(values)

    @staticmethod
    def rotationZ(angle: float):
        s = sin(angle)
        c = cos(angle)
        values = [
            c,  s, 0, 0,
            -s, c, 0, 0,
            0,  0, 1, 0,
            0,  0, 0, 1,
        ]
        return Matrix(values)

    @staticmethod
    def rotation(r: Vector):
        x = Matrix.rotationX(r.x())
        y = Matrix.rotationY(r.y())
        z = Matrix.rotationZ(r.z())
        return z * x * y

    @staticmethod
    def translation(t: Vector):
        values = [
            1,   0,   0,   0,
            0,   1,   0,   0,
            0,   0,   1,   0,
            t.x(), t.y(), t.z(), 1,
        ]
        return Matrix(values)

    @staticmethod
    def scale(s: Vector):
        values = [
            s.x(), 0,     0,     0,
            0,     s.y(), 0,     0,
            0,     0,     s.z(), 0,
            0,     0,     0,     1,
        ]
        return Matrix(values)

    def transform(self, v: Vector):
        x = v.x() * self.p[0 * 4 + 0] + v.y() * self.p[1 * 4 + 0] + v.z() * self.p[2 * 4 + 0] + self.p[3 * 4 + 0]
        y = v.x() * self.p[0 * 4 + 1] + v.y() * self.p[1 * 4 + 1] + v.z() * self.p[2 * 4 + 1] + self.p[3 * 4 + 1]
        z = v.x() * self.p[0 * 4 + 2] + v.y() * self.p[1 * 4 + 2] + v.z() * self.p[2 * 4 + 2] + self.p[3 * 4 + 2]
        w = v.x() * self.p[0 * 4 + 3] + v.y() * self.p[1 * 4 + 3] + v.z() * self.p[2 * 4 + 3] + self.p[3 * 4 + 3]
        return Vector(x / w, y / w, z / w)


