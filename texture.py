from color import Color


class Texture:
    def __init__(self, path: str):
        with open(path) as image_file:
            # eat file descriptor and version
            image_file.readline()
            image_file.readline()

            self.width = int(image_file.readline())
            self.height = int(image_file.readline())

            self.pixels = []

            delimiter = ' '
            for line in image_file:
                row = [int(x) for x in line.split(delimiter)]
                self.pixels.extend(row)

    def sample(self, u: float, v: float):
        # todo why not None
        if self.pixels is not None:
            tu = abs(int(u * (self.width - 1)))
            tv = abs(int(v * (self.height - 1)))

            index = tu + tv * self.width
            r, g, b, a = Color.rgba(self.pixels[index])
            c = Color(r, g, b, a)

            return c
        else:
            return Color.white()
