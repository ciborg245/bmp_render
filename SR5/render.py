from math import trunc, ceil, floor
from bitmap import Bitmap, color
import obj as obj
import random as ran

x = lambda v0, v1, y: v0[0] - ((v0[1]-y)*(v0[0]-v1[0])/(v0[1]-v1[1]))

def cross_product(v1, v2):
    return [
        v1[1]*v2[2] - v1[2]*v2[1],
        v1[2]*v2[0] - v1[0]*v2[2],
        v1[0]*v2[1] - v1[1]*v2[0]
    ]

def dot_product(v0, v1):
    return v0[0] * v1[0] + v0[1] * v1[1] + v0[2] * v1[2]

def vector_subs(v0, v1):
    return [v0[0] - v1[0], v0[1] - v1[1], v0[2] - v1[2]]

def vector_sum(v0, v1):
    return [v0[0] + v1[0], v0[1] + v1[1], v0[2] + v1[2]]

def vector_linear_mul(vertex, n):
    return [vertex[0] * n, vertex[1] * n, vertex[2] * n]

# def barycentric(a, b, c, P):
#     det = 0.5 * (-b[1] * c[0] + a[1] * (-b[0] + c[0]) + a[0] * (b[1] - c[1]) + b[0] * c[1])
#     sign = -1 if det < 0 else 1
#     v = (a[1] * c[0] - a[0] * c[1] + (c[1] - a[1]) * P[0] + (a[0] - c[0]) * P[1]) * sign
#     w = (a[0] * b[1] - a[1] * b[0] + (a[1] - b[1]) * P[0] + (b[0] - a[0]) * P[1]) * sign
#
#     return  v >= 0 and w >= 0 and (v + w) < 2 * det * sign

def barycentric2(a, b, c, P):
    prod = cross_product(
        [c[0] - a[0], b[0]-a[0], a[0]-P[0]],
        [c[1]-a[1], b[1]-a[1], a[1]-P[1]]
    )

    if abs(prod[2]) < 1:
        return [-1, 0, 0]

    u = 1.0 - (prod[0] + prod[1]) / prod[2]
    v = prod[1] / prod[2]
    w = prod[0] / prod[2]

    return u, v, w

def bounding_box(v0, v1, v2):
    x = [v0[0], v1[0], v2[0]]
    y = [v0[1], v1[1], v2[1]]
    x.sort()
    y.sort()

    return x[0], x[-1], y[0], y[-1]

def transform_vertex(vertex, translateX=0, translateY=0, translateZ=0, scale=1):
    return [
        round((vertex[0] + translateX) * scale),
        round((vertex[1] + translateY) * scale),
        round((vertex[2] + translateZ) * scale)
    ]

def normalize(vertex):
    len = (vertex[0]**2 + vertex[1]**2 + vertex[2]**2)**0.5

    if len == 0:
        return [0, 0, 0]

    return [
        vertex[0] / len,
        vertex[1] / len,
        vertex[2] / len
    ]

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


    def loadObj(self, filename, translateX=0, translateY=0, scale=1, triangle=0):
        with open(filename) as file:
            faces, vertices = obj.processObj(file)

        light = [0.2, 0.3, 0.5]

        for face in faces:

            faceLen = len(face)
            faceVer = []
            for i in range(faceLen):
                faceVer.append(transform_vertex(
                    vertices[face[i][0] - 1],
                    translateX=translateX,
                    translateY=translateY,
                    scale=scale
                ))

            loopLen = faceLen - 2
            for i in range(loopLen):
                dot = cross_product(vector_subs(faceVer[i+1], faceVer[0]), vector_subs(faceVer[i+2], faceVer[0]))

                norm = normalize(dot)

                light_int = dot_product(norm, light)

                if light_int > 0:
                    self.glColor(light_int, light_int, light_int)
                    self.barycentric_triangle(faceVer[0], faceVer[i+1], faceVer[i+2])

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


    # def line_sweeping_triangle(self, A, B, C):
    #     if (A[1] > B[1]):
    #         A, B = B, A
    #     if (B[1] > C[1]):
    #         B, C = C, B
    #     if (A[1] > B[1]):
    #         A, B = B, A
    #
    #     self.glLineC(A[0], A[1], B[0], B[1])
    #     self.glLineC(A[0], A[1], C[0], C[1])
    #     self.glLineC(B[0], B[1], C[0], C[1])
    #
    #     for i in range(A[1], B[1]):
    #         x0 = round(x(A, C, i))
    #         x1 = round(x(A, B, i))
    #         self.glLineC(x0, i, x1, i)
    #
    #     for i in range(B[1], C[1]):
    #         x0 = round(x(A, C, i))
    #         x1 = round(x(B, C, i))
    #         self.glLineC(x0, i, x1, i)

    def barycentric_triangle(self, A, B, C):
        x_min, x_max, y_min, y_max = bounding_box(A, B, C)

        for i in range(x_min, x_max + 1):
            for j in range(y_min, y_max + 1):
                u, v, w = barycentric2(A, B, C, [i, j])

                if u >= 0 and v >= 0 and w >= 0:
                    P_z = dot_product([u, v, w], [A[2], B[2], C[2]])

                    if self.bmp.getZbuffer(i, j) < P_z:
                        self.bmp.setZbuffer(i, j, P_z)
                        self.glVertexC(i, j)
