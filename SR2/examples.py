from render import Render
from random import uniform, randint
from math import floor, fsum

ren = Render()

####### Item 1
def random_point():
    ren.glCreateWindow(600, 400)
    ren.glClearColor(0, 0, 0)
    ren.glViewPort(0, 0, 600, 400)
    ren.glVertex(uniform(-1, 1), uniform(-1, 1))
    ren.glColor(1, 1, 1)

    ren.display("item1")


###### --------

# ##### Item 2
def white_point_each_corner():
    ren.glCreateWindow(500, 500)
    ren.glClearColor(0, 0, 0)
    ren.glViewPort(0, 0, 500, 500)
    ren.glColor(1, 1, 1)
    ren.glVertex(-1, 1)
    ren.glVertex(1, 1)
    ren.glVertex(1, -1)
    ren.glVertex(-1, -1)

    ren.display('item2')
# ##### --------

###### Item 3

###### ------

###### Item 4
def square():
    width = 500
    height = 500
    ren.glCreateWindow(width, height)
    ren.glClearColor(0, 0, 0)

    xVP = 0
    yVP = 0

    ren.glColor(1, 1, 1)

    ren.glViewPort(5, 5, 490, 490)
    i = 2/486
    cont = -1
    while (cont <= 1):
        ren.glVertex(1, cont)
        ren.glVertex(cont, 1)
        ren.glVertex(-1, cont)
        ren.glVertex(cont, -1)
        cont += i

    ren.display('item4')

###### ------

###### Item 5
def diagonal():
    width = 500
    height = 500
    ren.glCreateWindow(width, height)
    ren.glClearColor(0, 0, 0)

    ren.glColor(1, 1, 1)

    ren.glViewPort(0, 0, 500, 500)
    i = 2/500
    cont = -1
    while (cont <= 1):
        ren.glVertex(cont, cont)
        cont += i

    ren.display('item5')

###### ------

###### Item 6
def static():
    width = 500
    height = 500
    ren.glCreateWindow(width, height)
    ren.glClearColor(0, 0, 0)

    ren.glColor(1, 1, 1)

    ren.glViewPort(0, 0, 500, 500)
    s = 2/500
    i = -1
    cont = 0
    while (i <= 1):
        print("Iteracion ", cont)
        j = -1
        while (j <= 1):
            if randint(0,1) == 0:
                ren.glVertex(i, j)
            j += s
        i += s
        cont += 1

    ren.display('item6')

###### ------

###### Item 7
def random_colors():
    width = 500
    height = 500
    ren.glCreateWindow(width, height)

    ren.glViewPort(0, 0, width, height)
    s = 2/500
    i = -1
    while (i <= 1):
        j = -1
        while (j <= 1):
            r = uniform(0, 1)
            g = uniform(0, 1)
            b = uniform(0, 1)
            # print(r)
            # print(g)
            # print(b)
            ren.glColor(r, g, b)
            ren.glVertex(i, j)
            j += s
        i += s

    ren.display('item7')

###### ------

###### Item 8
def stars():
    width = 500
    height = 500
    ren.glCreateWindow(width, height)
    ren.glClearColor(0, 0, 0)

    ren.glColor(1, 1, 1)

    for i in range(0, width, 5):
        for j in range(0, height, 5):
            num = uniform(0, 1)
            if (num < 0.01):
                type = randint(1, 3)
                if (type == 1):
                    ren.glViewPort(i, j, 5, 5)
                    ren.glVertex(0, 0)
                    ren.glVertex(0, 0.5)
                    ren.glVertex(0, 1)
                    ren.glVertex(0, -0.5)
                    ren.glVertex(0, -1)
                    ren.glVertex(0.5, 0)
                    ren.glVertex(1, 0)
                    ren.glVertex(-0.5, 0)
                    ren.glVertex(-1, 0)
                    ren.glVertex(0.5, 0.5)
                    ren.glVertex(-0.5, 0.5)
                    ren.glVertex(0.5, -0.5)
                    ren.glVertex(-0.5, -0.5)

                elif (type == 2):
                    ren.glViewPort(i,j,3,3)
                    ren.glVertex(0, 0)
                    ren.glVertex(0, 1)
                    ren.glVertex(0, -1)
                    ren.glVertex(1, 0)
                    ren.glVertex(-1, 0)

                elif (type == 3):
                    ren.glViewPort(i,j,1,1)
                    ren.glVertex(0,0)

    ren.display('item8')

###### ------

###### Item 9
def atari():
    width = 192
    height = 160
    ren.glCreateWindow(width, height)
    ren.glClearColor(0, 0, 0)

    vpWidth = 12
    vpHeight = 100
    #909090
    #144, 144, 144
    #
    ren.glColor(0.5625, 0.5625, 0.5625)
    ren.glViewPort(0, 20, vpWidth, vpHeight)

    sx = 2 / vpWidth
    sy = 2 / vpHeight

    i = -1
    while (i <= 1):
        j = -1
        while(j <= 1):
            ren.glVertex(i, j)
            j += sy
        i += sx

    vpWidth = 192 - vpWidth * 2 + 2
    vpHeight = 12
    ren.glViewPort(11, 20 + 100 - 12 - 1, vpWidth, vpHeight)

    sx = 2 / vpWidth
    sy = 2 / vpHeight

    i = -1
    while (i <= 1):
        j = -1
        while(j <= 1):
            ren.glVertex(i, j)
            j += sy
        i += sx

    vpWidth = 12
    vpHeight = 100
    ren.glViewPort(width - 12, 20, vpWidth, vpHeight)

    sx = 2 / vpWidth
    sy = 2 / vpHeight

    i = -1
    while (i <= 1):
        j = -1
        while(j <= 1):
            ren.glVertex(i, j)
            j += sy
        i += sx


    vpWidth = 170
    vpHeight = 5
    #909090
    #176, 60, 60
    ren.glColor(0.6875, 0.234375, 0.234375)
    ren.glViewPort(11, 90, vpWidth, vpHeight)
    sx = 2 / vpWidth
    sy = 2 / vpHeight

    i = -1
    while (i <= 1):
        j = -1
        while(j <= 1):
            ren.glVertex(i, j)
            j += sy
        i += sx

    vpWidth = 170
    vpHeight = 5
    #909090
    #208, 128, 92
    ren.glColor(0.8125, 0.5, 0.359375)
    ren.glViewPort(11, 85, vpWidth, vpHeight)
    sx = 2 / vpWidth
    sy = 2 / vpHeight

    i = -1
    while (i <= 1):
        j = -1
        while(j <= 1):
            ren.glVertex(i, j)
            j += sy
        i += sx


    vpWidth = 170
    vpHeight = 5
    #909090
    #224, 148, 112
    ren.glColor(0.875, 0.578125, 0.4375)
    ren.glViewPort(11, 80, vpWidth, vpHeight)
    sx = 2 / vpWidth
    sy = 2 / vpHeight

    i = -1
    while (i <= 1):
        j = -1
        while(j <= 1):
            ren.glVertex(i, j)
            j += sy
        i += sx

    vpWidth = 170
    vpHeight = 5
    #909090
    #232, 232, 92
    ren.glColor(0.90625, 0.90625, 0.359375)
    ren.glViewPort(11, 75, vpWidth, vpHeight)
    sx = 2 / vpWidth
    sy = 2 / vpHeight

    i = -1
    while (i <= 1):
        j = -1
        while(j <= 1):
            ren.glVertex(i, j)
            j += sy
        i += sx

    vpWidth = 170
    vpHeight = 5
    #909090
    #64, 124, 64
    ren.glColor(0.25, 0.5, 0.25)
    ren.glViewPort(11, 70, vpWidth, vpHeight)
    sx = 2 / vpWidth
    sy = 2 / vpHeight

    i = -1
    while (i <= 1):
        j = -1
        while(j <= 1):
            ren.glVertex(i, j)
            j += sy
        i += sx

    vpWidth = 170
    vpHeight = 5
    #909090
    #56, 64, 176
    ren.glColor(0.21875, 0.25, 0.6875)
    ren.glViewPort(11, 65, vpWidth, vpHeight)
    sx = 2 / vpWidth
    sy = 2 / vpHeight

    i = -1
    while (i <= 1):
        j = -1
        while(j <= 1):
            ren.glVertex(i, j)
            j += sy
        i += sx

    vpWidth = 20
    vpHeight = 3
    #909090
    #192, 88, 88
    ren.glColor(0.75, 0.34375, 0.34375)
    ren.glViewPort(100, 20, vpWidth, vpHeight)
    sx = 2 / vpWidth
    sy = 2 / vpHeight

    i = -1
    while (i <= 1):
        j = -1
        while(j <= 1):
            ren.glVertex(i, j)
            j += sy
        i += sx

    vpWidth = 3
    vpHeight = 3
    #909090
    #192, 88, 88
    ren.glColor(0.75, 0.34375, 0.34375)
    ren.glViewPort(125, 40, vpWidth, vpHeight)
    sx = 2 / vpWidth
    sy = 2 / vpHeight

    i = -1
    while (i <= 1):
        j = -1
        while(j <= 1):
            ren.glVertex(i, j)
            j += sy
        i += sx

    vpWidth = 12
    vpHeight = 5
    #909090
    #112, 208, 172
    ren.glColor(0.4375, 0.8125, 0.671875)
    ren.glViewPort(0, 20, vpWidth, vpHeight)
    sx = 2 / vpWidth
    sy = 2 / vpHeight

    i = -1
    while (i <= 1):
        j = -1
        while(j <= 1):
            ren.glVertex(i, j)
            j += sy
        i += sx

    vpWidth = 12
    vpHeight = 5
    #909090
    #156, 32, 32
    ren.glColor(0.609375, 0.125, 0.125)
    ren.glViewPort(180, 20, vpWidth, vpHeight)
    sx = 2 / vpWidth
    sy = 2 / vpHeight

    i = -1
    while (i <= 1):
        j = -1
        while(j <= 1):
            ren.glVertex(i, j)
            j += sy
        i += sx

    vpWidth = 16
    vpHeight = 5
    #909090
    #156, 32, 32
    ren.glColor(0,0,0)
    ren.glViewPort(150, 65, vpWidth, vpHeight)
    sx = 2 / vpWidth
    sy = 2 / vpHeight

    i = -1
    while (i <= 1):
        j = -1
        while(j <= 1):
            ren.glVertex(i, j)
            j += sy
        i += sx

    ## 00000000000000000000000000
    vpWidth = 3
    vpHeight = 9
    ren.glColor(0.5625,0.5625,0.5625)
    ren.glViewPort(40, 120, vpWidth, vpHeight)
    sx = 2 / vpWidth
    sy = 2 / vpHeight

    i = -1
    while (i <= 1):
        j = -1
        while(j <= 1):
            ren.glVertex(i, j)
            j += sy
        i += sx

    vpWidth = 9
    vpHeight = 3
    ren.glColor(0.5625,0.5625,0.5625)
    ren.glViewPort(40, 120, vpWidth, vpHeight)
    sx = 2 / vpWidth
    sy = 2 / vpHeight

    i = -1
    while (i <= 1):
        j = -1
        while(j <= 1):
            ren.glVertex(i, j)
            j += sy
        i += sx

    vpWidth = 9
    vpHeight = 3
    ren.glColor(0.5625,0.5625,0.5625)
    ren.glViewPort(40, 129, vpWidth, vpHeight)
    sx = 2 / vpWidth
    sy = 2 / vpHeight

    i = -1
    while (i <= 1):
        j = -1
        while(j <= 1):
            ren.glVertex(i, j)
            j += sy
        i += sx

    vpWidth = 3
    vpHeight = 9
    ren.glColor(0.5625,0.5625,0.5625)
    ren.glViewPort(46, 120, vpWidth, vpHeight)
    sx = 2 / vpWidth
    sy = 2 / vpHeight

    i = -1
    while (i <= 1):
        j = -1
        while(j <= 1):
            ren.glVertex(i, j)
            j += sy
        i += sx

    ## 0000000000000000000000000

    ## 00000000000000000000000000
    vpWidth = 3
    vpHeight = 9
    ren.glColor(0.5625,0.5625,0.5625)
    ren.glViewPort(55, 120, vpWidth, vpHeight)
    sx = 2 / vpWidth
    sy = 2 / vpHeight

    i = -1
    while (i <= 1):
        j = -1
        while(j <= 1):
            ren.glVertex(i, j)
            j += sy
        i += sx

    vpWidth = 9
    vpHeight = 3
    ren.glColor(0.5625,0.5625,0.5625)
    ren.glViewPort(55, 120, vpWidth, vpHeight)
    sx = 2 / vpWidth
    sy = 2 / vpHeight

    i = -1
    while (i <= 1):
        j = -1
        while(j <= 1):
            ren.glVertex(i, j)
            j += sy
        i += sx

    vpWidth = 9
    vpHeight = 3
    ren.glColor(0.5625,0.5625,0.5625)
    ren.glViewPort(55, 129, vpWidth, vpHeight)
    sx = 2 / vpWidth
    sy = 2 / vpHeight

    i = -1
    while (i <= 1):
        j = -1
        while(j <= 1):
            ren.glVertex(i, j)
            j += sy
        i += sx

    vpWidth = 3
    vpHeight = 9
    ren.glColor(0.5625,0.5625,0.5625)
    ren.glViewPort(61, 120, vpWidth, vpHeight)
    sx = 2 / vpWidth
    sy = 2 / vpHeight

    i = -1
    while (i <= 1):
        j = -1
        while(j <= 1):
            ren.glVertex(i, j)
            j += sy
        i += sx

    ## 0000000000000000000000000

    ## 1111111111111111111111111

    vpWidth = 3
    vpHeight = 12
    ren.glColor(0.5625,0.5625,0.5625)
    ren.glViewPort(76, 120, vpWidth, vpHeight)
    sx = 2 / vpWidth
    sy = 2 / vpHeight

    i = -1
    while (i <= 1):
        j = -1
        while(j <= 1):
            ren.glVertex(i, j)
            j += sy
        i += sx


    ## 1111111111111111111111111

    ## 3333333333333333333333333

    vpWidth = 3
    vpHeight = 12
    ren.glColor(0.5625,0.5625,0.5625)
    ren.glViewPort(112, 120, vpWidth, vpHeight)
    sx = 2 / vpWidth
    sy = 2 / vpHeight

    i = -1
    while (i <= 1):
        j = -1
        while(j <= 1):
            ren.glVertex(i, j)
            j += sy
        i += sx

    vpWidth = 6
    vpHeight = 2
    ren.glColor(0.5625,0.5625,0.5625)
    ren.glViewPort(106, 120, vpWidth, vpHeight)
    sx = 2 / vpWidth
    sy = 2 / vpHeight

    i = -1
    while (i <= 1):
        j = -1
        while(j <= 1):
            ren.glVertex(i, j)
            j += sy
        i += sx

    vpWidth = 6
    vpHeight = 2
    ren.glColor(0.5625,0.5625,0.5625)
    ren.glViewPort(106, 125, vpWidth, vpHeight)
    sx = 2 / vpWidth
    sy = 2 / vpHeight

    i = -1
    while (i <= 1):
        j = -1
        while(j <= 1):
            ren.glVertex(i, j)
            j += sy
        i += sx

    vpWidth = 6
    vpHeight = 2
    ren.glColor(0.5625,0.5625,0.5625)
    ren.glViewPort(106, 130, vpWidth, vpHeight)
    sx = 2 / vpWidth
    sy = 2 / vpHeight

    i = -1
    while (i <= 1):
        j = -1
        while(j <= 1):
            ren.glVertex(i, j)
            j += sy
        i += sx
    ## 3333333333333333333333333

    ## 1111111111111111111111111

    vpWidth = 3
    vpHeight = 12
    ren.glColor(0.5625,0.5625,0.5625)
    ren.glViewPort(150, 120, vpWidth, vpHeight)
    sx = 2 / vpWidth
    sy = 2 / vpHeight

    i = -1
    while (i <= 1):
        j = -1
        while(j <= 1):
            ren.glVertex(i, j)
            j += sy
        i += sx


    ## 1111111111111111111111111
    ren.display('item9')

###### ------
