import sys

from numpy import ndarray

from canvas import Canvas
from color import Color
from mesh import Mesh
from vector import Vector
from vertex import Vertex


class Window(object):
    def __init__(self, width: int, height: int, pixels: ndarray):
        self.pixels = pixels
        self.width = width
        self.height = height

        self.canvas = Canvas(width, height, pixels)

        # setup key handlers
        key_esc = 27
        self.handlers = {
            key_esc: self.exit
        }

        # self.v1 = Vertex(Vector(0, 0),Vector(0, 0),1,1, Color.cyan())
        # self.v2 = Vertex(Vector(300, 100),Vector(0, 0),1,1,  Color.red())
        # self.v3 = Vertex(Vector(200, 300),Vector(0, 0),1,1,  Color.green())

        model_path = "illidan.model"
        texture_path = "illidan.texture"

        self.mesh = Mesh(model_path, texture_path)

    def clear(self):
        self.canvas.clear()

    def update(self, dt):
        pass

    def draw(self):
        # self.canvas.draw_triangle(self.v1, self.v2, self.v3, self.mesh.texture)
        self.canvas.draw_mesh(self.mesh)

    def mouse_event(self, button, state, x, y):
        print('mouse event', button, state, x, y)
        # 0, left button
        # 2, right button
        # 0, state press
        # 1, state release

    def exit(self):
        sys.exit(0)

    def cmd404(self):
        pass

    def key_event(self, key, key_is_down):
        print('key event', key, key_is_down)
        cmd = self.handlers.get(key, self.cmd404)
        cmd()
