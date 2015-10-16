from math import radians

from numpy import ndarray

from matrix import Matrix
from mesh import Mesh
from texture import Texture
from vector import Vector
from color import Color
from vertex import Vertex
from common import *


class Canvas(object):
    def __init__(self, width: int, height: int, pixels: ndarray):
        self.width = width
        self.height = height
        self.pixels = pixels

    def clear(self):
        self.pixels.fill(0)

    def put_pixel(self, x: int, y: int, color: Color):
        index = int(y) * self.width + int(x)
        self.pixels[index] = color.uint32()

    def draw_point(self, point: Vector, color: Color = Color.white()):
        if 0 <= point.x < self.width and 0 <= point.y < self.height:
            self.put_pixel(point.x, point.y, color)

    def draw_line(self, p1: Vector, p2: Vector):
        x1, y1, x2, y2 = [int(i) for i in [p1.x, p1.y, p2.x, p2.y]]

        dx = x2 - x1
        dy = y2 - y1

        if abs(dx) > abs(dy):
            xmin, xmax = sorted([x1, x2])
            ratio = dy / dx
            for x in range(xmin, xmax):
                y = y1 + (x - xmin) * ratio
                self.draw_point(Vector(x, y))
        else:
            ymin, ymax = sorted([y1, y2])
            ratio = 0 if dy == 0 else dx / dy
            for y in range(ymin, ymax):
                x = x1 + (y - ymin) * ratio
                self.draw_point(Vector(x, y))

    def draw_scanline(self, va: Vertex, vb: Vertex, y: int, texture: Texture):
        x1 = int(va.position.x)
        x2 = int(vb.position.x)
        sign = 1 if x2 > x1 else -1
        factor = 0
        for x in range(x1, x2 + sign * 1, sign):
            if x1 != x2:
                factor = (x - x1) / (x2 - x1)
            # color = interpolate(v1.color, v2.color, factor)
            v = interpolate(va, vb, factor)
            color = texture.sample(v.u, v.v)
            self.draw_point(Vector(x, y), color)

    def draw_triangle(self, v1: Vertex, v2: Vertex, v3: Vertex, texture: Texture):
        a, b, c = sorted([v1, v2, v3], key=lambda k: k.position.y)
        middle_factor = 0
        if c.position.y - a.position.y != 0:
            middle_factor = (b.position.y - a.position.y) / (c.position.y - a.position.y)
        middle = interpolate(a, c, middle_factor)

        start_y = int(a.position.y)
        end_y = int(b.position.y)
        for y in range(start_y, end_y + 1):
            factor = (y - start_y) / (end_y - start_y) if end_y != start_y else 0
            va = interpolate(a, b, factor)
            vb = interpolate(a, middle, factor)
            self.draw_scanline(va, vb, y, texture)

        start_y = int(b.position.y)
        end_y = int(c.position.y)
        for y in range(start_y, end_y + 1):
            factor = (y - start_y) / (end_y - start_y) if end_y != start_y else 0
            va = interpolate(b, c, factor)
            vb = interpolate(middle, c, factor)
            self.draw_scanline(va, vb, y, texture)

    def project(self, v: Vertex, transform: Matrix):
        # the function for vertex shader
        p = transform.transform(v.position)

        p.x = p.x * self.width + self.width / 2
        p.y *= self.height

        return Vertex(p, v.normal, v.u, v.v, v.color)

    def draw_mesh(self, mesh: Mesh):
        camera_position = Vector(0, 0, -10)
        camera_target = Vector(0, 0, 0)
        camera_up = Vector(0, 1, 0)

        view = Matrix.lookAtLH(camera_position, camera_target, camera_up)
        projection = Matrix.perspectiveFovLH(radians(45), self.width / self.height, 0.1, 1)
        rotation = Matrix.rotation(mesh.rotation)
        translation = Matrix.translation(mesh.position)
        scale = Matrix.scale(mesh.scale)

        world = scale * rotation * translation
        transform = world * view * projection

        for i in range(0, len(mesh.indices), 3):
            a = mesh.vertices[mesh.indices[i]]
            b = mesh.vertices[mesh.indices[i + 1]]
            c = mesh.vertices[mesh.indices[i + 2]]

            v1 = self.project(a, transform)
            v2 = self.project(b, transform)
            v3 = self.project(c, transform)

            self.draw_triangle(v1, v2, v3, mesh.texture)
