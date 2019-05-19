import struct

def color(r, g, b):
    return bytes([b, g, r])

class Texture(object):
    def __init__(self, path):
        self.path = path
        self.read()

    def read(self):
        image = open(self.path, "rb")

        #skip BM, bmp size and zeros
        image.seek(10)
        header_size = struct.unpack("=l", image.read(4))[0]
        image.seek(18)

        self.width = struct.unpack("=l", image.read(4))[0]
        self.height = struct.unpack("=l", image.read(4))[0]
        self.pixels = []
        image.seek(header_size)

        for y in range(self.height):
            self.pixels.append([])
            for x in range(self.width):
                b = ord(image.read(1))
                g = ord(image.read(1))
                r = ord(image.read(1))
                self.pixels[y].append(color(r,g,b))
        image.close()

    def getColor(self, pos_x, pos_y, intensity=1):
        x = int(pos_x * self.width)
        y = int(pos_y * self.height)

        try:
            return bytes(map(lambda b: round(b*intensity) if b*intensity > 0 else 0, self.pixels[y][x]))
        except:
            pass
