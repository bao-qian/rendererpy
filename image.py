class Image:
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
