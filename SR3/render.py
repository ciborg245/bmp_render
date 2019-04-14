from math import trunc, ceil, floor
from bitmap import Bitmap, color
import obj as obj

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


    def loadObj(self, filename, translateX=0, translateY=0, scale=1):
        with open(filename) as file:
            faces, vertices = obj.processObj(file)

        for face in faces:

            faceLen = len(face)-1

            for j in range(-1, faceLen):
                v1 = vertices[face[j][0] - 1]
                v2 = vertices[face[j+1][0] - 1]

                x0 = round((v1[0] + translateX) * scale)
                y0 = round((v1[1] + translateY) * scale)
                x1 = round((v2[0] + translateX) * scale)
                y1 = round((v2[1] + translateY) * scale)

                self.glLineC(x0, y0, x1, y1)



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

    def fillPolygon(self, points, r, g, b):
        self.glColor(r / 255, g / 255, b / 255)

        for i in range(-1,len(points)-1):
            self.glLineC(points[i][0], points[i][1], points[i+1][0], points[i+1][1])

        edges = self.createPolygonEdges(points)

        y_min = min([points[i][1] for i in range(len(points))])
        y_max = max([points[i][1] for i in range(len(points))])
        x_min = min([points[i][0] for i in range(len(points))])
        x_max = max([points[i][0] for i in range(len(points))])


        for i in range(y_min, y_max+1):
            activeEdges = [edges[n] for n in range(len(edges)) if edges[n]['yMin'] <= i <= edges[n]['yMax']]
            activeEdges = sorted(activeEdges, key=lambda item: item['x'])

            count = 0
            intercepts = []
            for j in range(len(activeEdges)):
                if activeEdges[j]['m'] == 0:
                    adjEdges = []
                    for k in range(len(activeEdges)):
                        if j != k:
                            if (activeEdges[j]['v0'] == activeEdges[k]['v0'] or activeEdges[j]['v0'] == activeEdges[k]['v1']):
                                adjEdges.append(activeEdges[k])
                            if (activeEdges[j]['v1'] == activeEdges[k]['v0'] or activeEdges[j]['v1'] == activeEdges[k]['v1']):
                                adjEdges.append(activeEdges[k])
                            if len(adjEdges) == 2:
                                break
                    if not (adjEdges[0]['yMax'] == adjEdges[1]['yMax'] or adjEdges[0]['yMin'] == adjEdges[1]['yMin']):
                        intercepts.append(activeEdges[j]['x'])
                elif j < len(activeEdges)-1:
                    if not ((
                        (i == activeEdges[j]['v0'][1] and (
                            activeEdges[j]['v0'] == activeEdges[j+1]['v0'] or
                            activeEdges[j]['v0'] == activeEdges[j+1]['v1']
                        )) or
                        (i == activeEdges[j]['v1'][1] and (
                            activeEdges[j]['v1'] == activeEdges[j+1]['v0'] or
                            activeEdges[j]['v1'] == activeEdges[j+1]['v1']
                        ))
                    ) and ((activeEdges[j]['yMin'] != activeEdges[j+1]['yMin']) and (activeEdges[j]['yMax'] != activeEdges[j+1]['yMax']))):
                        if activeEdges[j]['m'] == 0:
                            intercepts.append(activeEdges[j]['x'])
                        else:
                            intercepts.append(round(
                                activeEdges[j]['x0'] - ((activeEdges[j]['y0'] - i) / activeEdges[j]['m'])
                            ))
                else:
                    if activeEdges[j]['m'] == 0:
                        intercepts.append(activeEdges[j]['x'])
                    else:
                        intercepts.append(round(
                            activeEdges[j]['x0'] - ((activeEdges[j]['y0'] - i) / activeEdges[j]['m'])
                        ))

            for j in range(x_min, x_max + 1):
                count = 0
                for k in range(len(intercepts)):
                    if intercepts[k] < j:
                        count += 1

                if count % 2 == 1:
                    self.glVertexC(j, i)

    def createPolygonEdges(self, ver):
        edges = []
        for i in range(-1, len(ver)-1):
            edge = {}
            # if ver[i][1] - ver[i+1][1] != 0:
            edge['yMax'] = max([ver[i][1], ver[i+1][1]])
            edge['yMin'] = min([ver[i][1], ver[i+1][1]])
            edge['x'] = min([ver[i][0], ver[i+1][0]])
            edge['x0'] = ver[i][0]
            edge['y0'] = ver[i][1]
            edge['v0'] = [ver[i][0], ver[i][1]]
            edge['v1'] = [ver[i+1][0], ver[i+1][1]]
            if ver[i][0] - ver[i+1][0] == 0:
                edge['m'] = 999999999
            else:
                edge['m'] = ((ver[i][1]-ver[i+1][1])/(ver[i][0]-ver[i+1][0]))

            edges.append(edge)

        return edges
