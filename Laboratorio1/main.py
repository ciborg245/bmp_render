from render import Render

ren = Render()

width = 800
height = 800
ren.glCreateWindow(width, height)
ren.glClearColor(0, 0, 0)
ren.glViewPort(0, 0, width, height)

cont = 0
with open('input.txt', 'r') as f:
    for polygon in f:
        polygon = polygon.strip()
        points = polygon.split(')')
        pointsArray = []

        for i in range(len(points)):
            if points[i] != '':
                x, y = map(int, points[i].replace(')', '').replace('(','').replace(',','').split())
                pointsArray.append([x, y])

        # print(pointsArray)

        if cont == 4:
            ren.fillPolygon(pointsArray, 0, 0, 0)
        else:
            ren.fillPolygon(pointsArray, 255, 255, 255)

        cont += 1

ren.display('out')
