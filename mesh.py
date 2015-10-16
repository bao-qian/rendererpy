from color import Color
from texture import Texture
from vector import Vector
from vertex import Vertex


class Mesh:
    def __init__(self, model_path: str, texture_path: str):
        self.position = Vector(0, 0, 0)
        self.rotation = Vector(0, 0, 0)
        self.scale = Vector(1, 1, 1)

        self.texture = Texture(texture_path)

        # load model file
        delimiter = ' '
        self.vertices = []
        self.indices = []
        with open(model_path) as model_file:

            # eat file descriptor and version
            model_file.readline()
            model_file.readline()

            vs = model_file.readline().split(delimiter)
            number_of_vertices = int(vs[1])

            ts = model_file.readline().split(delimiter)
            number_of_triangles = int(ts[1])

            # vertices
            for i in range(number_of_vertices):
                vs = model_file.readline().split(delimiter)
                x = float(vs[0])
                y = float(vs[1])
                z = float(vs[2])

                nx = float(vs[3])
                ny = float(vs[4])
                nz = float(vs[5])

                u = float(vs[6])
                v = float(vs[7])
                self.vertices.append(Vertex(Vector(x, y, z), Vector(nx, ny, nz), u, v, Color.white()))

            # triangles
            for i in range(number_of_triangles):
                t = model_file.readline().split(delimiter)
                a = int(t[0])
                b = int(t[1])
                c = int(t[2])
                self.indices.append(a)
                self.indices.append(b)
                self.indices.append(c)
