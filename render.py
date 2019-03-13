from math import trunc, floor
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
        self.x = trunc(self.view['x'] + (self.view['width'] / 2) * (x + 1))
        self.y = trunc(self.view['y'] + (self.view['height'] / 2) * (y + 1))

        # print(self.x)
        # print(self.y)
        self.bmp.point(self.y, self.x, self.color)

    def glColor(self, r, g, b):
        self.color = color(floor(r * 255), floor(g * 255), floor(b * 255))
        # self.bmp.point(self.x, self.y, color(trunc(r * 255), trunc(g * 255), trunc(b * 255)))

    def glFinish(self, name = 'out'):
        self.bmp.write(name+'.bmp')
