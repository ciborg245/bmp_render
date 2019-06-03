from math import trunc, ceil, floor, cos, sin
from bitmap import Bitmap, color
import obj as obj
import random as ran
import numpy

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

def vec_length(vertex):
    return (vertex[0]**2 + vertex[1]**2 + vertex[2]**2)**0.5

def normalize(vertex):
    len = vec_length(vertex)

    if len == 0:
        return [0, 0, 0]

    return [
        vertex[0] / len,
        vertex[1] / len,
        vertex[2] / len
    ]


def matmul(mat1, mat2):

    res = []

    try:
        if type(mat1[0]) == float:
            mat1 = [mat1]
        if type(mat2[0]) == float:
            mat2 = [mat2]

        for i in range(len(mat1)):
            temp = []
            for j in range(len(mat2[0])):
                dot_prod = 0
                for k in range(len(mat1[0])):
                    dot_prod += mat1[i][k] * mat2[k][j]
                temp.append(dot_prod)
            res.append(temp)

        return res
    except:
        print("Error: Trying to multiply matrices with wrong sizes.")
        print("Sizes: {0},{1} and {2}, {3}".format(len(mat1), len(mat1[0]), len(mat2), len(mat2[0])))
        print(mat1)
        print(mat2)
        return None

a = [
    [1, -2, 3],
    [1, 0, -1]
]

b = [
    [4],
    [5],
    [6]
]

# print(matmul(a, b))
# print(cos(a))

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

    def glColorC(self, r, g, b):
        self.color = color(r, g, b)

    def glColorFull(self, color):
        self.color = color

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


    def loadObj(self, filename, translate=[0, 0, 0], scale=[1, 1, 1], rotate=[0, 0, 0], texture=None, light = [0, 0, 1]):
        with open(filename) as file:
            faces, vertices, textures_coor = obj.processObj(file)

        self.calcModelMat(rotate, scale, translate)

        for i in range(len(vertices)):
            vertices[i] = self.transform(vertices[i])

        # light = [0.3, 0.1, 0.6]
        # light = [0, 0, 1]
        asdf = 0
        for face in faces:
            asdf += 1
            # print(asdf)

            #Se obtienen las coordenadas de los vertices
            faceLen = len(face)
            faceVer = []
            faceTex = []
            for i in range(faceLen):
                faceVer.append(vertices[face[i][0] - 1])
                # faceVer.append(transform_vertex(
                    # vertices[face[i][0] - 1],
                    # translateX=translateX,
                    # translateY=translateY,
                    # scale=scale
                # ))
                if texture:
                    faceTex.append(textures_coor[face[i][1] - 1])

            #Se obtiene la intensidad
            dot = cross_product(vector_subs(faceVer[1], faceVer[0]), vector_subs(faceVer[2], faceVer[0]))
            norm = normalize(dot)
            light_int = dot_product(norm, light)

            #Se recorren todos los vertices de cada cara
            loopLen = faceLen - 2
            if faceLen <= 4:
                for i in range(loopLen):

                    if light_int > 0:
                        if not texture:
                            self.glColor(light_int, light_int, light_int)

                            tex_coor_temp = None
                        else:
                            tex_coor_temp = (faceTex[0], faceTex[i+1], faceTex[i+2])

                        self.barycentric_triangle(
                            faceVer[0],
                            faceVer[i+1],
                            faceVer[i+2],
                            tex_coor=tex_coor_temp,
                            texture=texture,
                            intensity=light_int
                        )

    def calcViewportMat(self, x=0, y=0):
        res = [
            [self.width / 2,            0,                          0,      x + self.width/2],
            [0,                         self.height / 2,            0,      y + self.height/2],
            [0,                         0,                          128,    128],
            [0,                         0,                          0,      1]
        ]

        self.viewport_matrix = res

    def calcModelMat(self, rotate=[0, 0, 0], scale=[1, 1, 1], translate=[0, 0, 0]):
        rotate_x = [
            [1,     0,                  0,                  0],
            [0,     cos(rotate[0]),     -sin(rotate[0]),    0],
            [0,     sin(rotate[0]),     cos(rotate[0]),     0],
            [0,     0,                  0,                  1]
        ]

        rotate_y = [
            [cos(rotate[1]),    0,      sin(rotate[1]),     0],
            [0,                 1,      0,                  0],
            [-sin(rotate[1]),   0,      cos(rotate[1]),     0],
            [0,                 0,      0,                  1]
        ]

        rotate_z = [
            [cos(rotate[2]),    -sin(rotate[2]),    0,  0],
            [sin(rotate[2]),    cos(rotate[2]),     0,  0],
            [0,                 0,                  1,  0],
            [0,                 0,                  0,  1]
        ]

        rotate_all = matmul(matmul(rotate_x, rotate_y), rotate_z)

        translation=[
            [1, 0, 0, translate[0]],
            [0, 1, 0, translate[1]],
            [0, 0, 1, translate[2]],
            [0, 0, 0, 1]
        ]

        scale_mat = [
            [scale[0],  0,          0,          0],
            [0,         scale[1],   0,          0],
            [0,         0,          scale[2],   0],
            [0,         0,          0,          1]
        ]

        self.model_matrix = matmul(matmul(translation, rotate_all), scale_mat)

    def calcViewMat(self, x, y, z, center):

        view_mat = [
          [x[0],    x[1],   x[2],   -center[0]],
          [y[0],    y[1],   y[2],   -center[1]],
          [z[0],    z[1],   z[2],   -center[2]],
          [0,       0,      0,      1]
        ]

        self.view_matrix = view_mat

    def calcProjectionMat(self, c):
        proj = [
            [1,     0,      0,      0],
            [0,     1,      0,      0],
            [0,     0,      1,      0],
            [0,     0,      c,      1]
        ]

        self.proj_matrix = proj

    def transform(self, vertex):
        vertex = [
            [vertex[0]],
            [vertex[1]],
            [vertex[2]],
            [1]
        ]

        # homog_mat = self.viewport_matrix @ self.proj_matrix @ self.view_matrix @ self.model_matrix @ vertex
        homog_mat = matmul(matmul(matmul(matmul(self.viewport_matrix, self.proj_matrix), self.view_matrix), self.model_matrix), vertex)

        trans_vertex = [
            round(homog_mat[0][0] / homog_mat[3][0]),
            round(homog_mat[1][0] / homog_mat[3][0]),
            round(homog_mat[2][0] / homog_mat[3][0])
        ]

        return trans_vertex

    def lookAt(self, cameraPos, cameraTarget, up):
        z = normalize(vector_subs(cameraPos, cameraTarget))
        x = normalize(cross_product(up, z))
        y = normalize(cross_product(z, x))

        self.calcViewMat(x, y, z, cameraTarget)
        self.calcProjectionMat(-1 / vec_length(vector_subs(cameraPos, cameraTarget)))
        self.calcViewportMat()


    def barycentric_triangle(self, A, B, C, tex_coor=(), texture=None, intensity=1):
        x_min, x_max, y_min, y_max = bounding_box(A, B, C)

        for i in range(x_min, x_max + 1):
            for j in range(y_min, y_max + 1):
                if i < 0 or j < 0:
                    continue
                u, v, w = barycentric2(A, B, C, [i, j])

                if u >= 0 and v >= 0 and w >= 0:

                    if texture:
                        tex_A, tex_B, tex_C = tex_coor
                        tex_x = tex_A[0] * u + tex_B[0] * v + tex_C[0] * w
                        tex_y = tex_A[1] * u + tex_B[1] * v + tex_C[1] * w

                        self.glColorFull(texture.getColor(tex_x, tex_y, intensity))

                    P_z = dot_product([u, v, w], [A[2], B[2], C[2]])


                    if j < len(self.bmp.zbuffer) and i < len(self.bmp.zbuffer[j]) and self.bmp.getZbuffer(i, j) < P_z:
                        self.bmp.setZbuffer(i, j, P_z)
                        self.glVertexC(i, j)
