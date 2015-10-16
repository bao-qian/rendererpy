from unittest import TestCase

from matrix import Matrix
from mesh import Mesh
from texture import Texture


class Test(TestCase):
    def test_matrix(self):
        m1 = Matrix.identity()
        m2 = m1 * m1
        self.assertEqual(m2, m1)

    def test_texture(self):
        texture = Texture("illidan.texture")
        self.assertEqual(texture.width, 256)
        self.assertEqual(texture.height, 256)
        self.assertEqual(len(texture.pixels), 256 * 256)
        self.assertEqual(texture.pixels[256], 387453183)

        # def test_color(self):
        #     c = 1683838207
        #     self.assertEqual(Color(c).uint32(), c)

    def test_mesh(self):
        mesh = Mesh("illidan.model", "illidan.texture")
        self.assertEqual(len(mesh.vertices), 4042)
        self.assertEqual(len(mesh.indices), 5603 * 3)
        self.assertEqual(mesh.vertices[2].position.x, -0.1)
        self.assertEqual(mesh.indices[6], 3)
