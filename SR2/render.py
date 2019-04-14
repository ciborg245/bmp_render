from math import trunc, ceil, floor
from bitmap import Bitmap, color

class Render(object):
    def __init__(self, width = None, height = None):
        self.x = 0
        self.y = 0
        self.view = {}
        self.color = color(255, 255, 255)

        if (width == None and height == None):
            self.bmp = None
            self.width = width
            self.height = height
        else:
            self.glCreateWindow(width, height)

    def glInit(self):
        pass

    def glCreateWindow(self, width, height):
        self.bmp = Bitmap(width, height)
        self.width = width
        self.height = height

    def glViewPort(self, x, y, width, height):
        self.view['x'] = x
        self.view['y'] = y
        self.view['width'] = width - 1
        self.view['height'] = height - 1

    def glClear(self):
        self.bmp.clear()

    def glClearColor(self, r, g, b):
        for i in range(self.height):
            for j in range(self.width):
                self.bmp.point(i, j, color(trunc(r * 255), trunc(g * 255), trunc(b * 255)))

    def glVertex(self, x, y):
        self.x = ceil(self.view['x'] + (self.view['width'] / 2) * (x + 1))
        self.y = ceil(self.view['y'] + (self.view['height'] / 2) * (y + 1))

        self.glVertexC(self.x, self.y)

    def glVertexC(self, x, y):
        self.bmp.point(y, x, self.color)

    def glColor(self, r, g, b):
        self.color = color(floor(r * 255), floor(g * 255), floor(b * 255))

    def glFinish(self, name = 'out'):
        self.bmp.write(name+'.bmp')

    def glLine(self, x0p, y0p, x1p, y1p):
        x0 = round(self.view['x'] + (self.view['width'] / 2) * (x0p + 1))
        y0 = round(self.view['y'] + (self.view['height'] / 2) * (y0p + 1))
        x1 = round(self.view['x'] + (self.view['width'] / 2) * (x1p + 1))
        y1 = round(self.view['y'] + (self.view['height'] / 2) * (y1p + 1))

        self.glLineC(x0, y0, x1, y1)

    def glLineC(self, x0, y0, x1, y1):
        # print(x0)
        # print(y0)
        # print(x1)
        # print(y1)

        dx = abs(x1 - x0)
        dy = abs(y1 - y0)

        if x1 < x0:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        px = 2 * dy - dx
        py = 2 * dx - dy

        if dx >= dy:
            y = y0
            for x in range(x0, x1 + 1):
                # print(x)
                # print(y)
                self.glVertexC(x, y)

                if px < 0:
                    px += 2 * dy
                else:
                    y += 1 if y0 < y1 else -1
                    px += 2 * (dy - dx)

        else:
            x = x0
            step = 1 if y0 < y1 else -1
            for y in range(y0, y1, step):
                # print(x)
                # print(y)
                self.glVertexC(x, y)

                if py < 0:
                    py += 2 * dx
                else:
                    x += 1 if x0 < x1 else -1
                    py += 2 * (dx - dy)


    def display(self, name = 'out'):
        self.glFinish(name)

        try:
            from wand.image import Image
            from wand.display import display

            with Image(filename = name + '.bmp') as image:
                display(image)
        except Exception as e:
            print(e)
            pass  # do nothing if no wand is installed
