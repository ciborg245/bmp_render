from render import Render
from random import uniform, randint, random, seed
from math import floor, trunc

ren = Render()

####### Item 1
# ren.glCreateWindow(600, 400)
# ren.glClearColor(0, 0, 0)
# ren.glViewPort(0, 0, 600, 400)
# ren.glVertex(uniform(-1, 1), uniform(-1, 1))
# ren.glColor(1, 1, 1)
#
# ren.glFinish("item1")

###### --------

# ##### Item 2
# ren.glCreateWindow(500, 500)
# ren.glClearColor(0, 0, 0)
# ren.glViewPort(0, 0, 500, 500)
# ren.glColor(1, 1, 1)
# ren.glVertex(-1, 1)
# ren.glVertex(1, 1)
# ren.glVertex(1, -1)
# ren.glVertex(-1, -1)
#
# ren.glFinish('item2')
# ##### --------

###### Item 3
# width = 500
# height = 500
# ren.glCreateWindow(width, height)
# ren.glClearColor(0, 0, 0)
#
# xVP = floor(height/2 - 50)
# yVP = floor(width/2 - 50)
#
# ren.glColor(1, 1, 1)
#
# ren.glViewPort(xVP, yVP, 100, 100)
# i = 2/100
# cont = -1
# while (cont <= 1):
#     ren.glVertex(1, cont)
#     ren.glVertex(cont, 1)
#     ren.glVertex(-1, cont)
#     ren.glVertex(cont, -1)
#     cont += i

# xVP = floor(height/2 - 50)
# yVP = floor(width/2 - 50)
# ren.glViewPort(xVP, yVP, 150, 50)

# ren.glFinish('item3')

###### ------

###### Item 4

# width = 500
# height = 500
# ren.glCreateWindow(width, height)
# ren.glClearColor(0, 0, 0)
#
# xVP = 0
# yVP = 0
#
# ren.glColor(1, 1, 1)
#
# ren.glViewPort(5, 5, 490, 490)
# i = 2/486
# cont = -1
# while (cont <= 1):
#     ren.glVertex(1, cont)
#     ren.glVertex(cont, 1)
#     ren.glVertex(-1, cont)
#     ren.glVertex(cont, -1)
#     cont += i
#
# ren.glFinish('item4')

###### ------

###### Item 5

# width = 500
# height = 500
# ren.glCreateWindow(width, height)
# ren.glClearColor(0, 0, 0)
#
# ren.glColor(1, 1, 1)
#
# ren.glViewPort(0, 0, 499, 499)
# i = 2/500
# cont = -1
# while (cont <= 1):
#     ren.glVertex(cont, cont)
#     cont += i
#
# ren.glFinish('item5')

###### ------

###### Item 6

# width = 500
# height = 500
# ren.glCreateWindow(width, height)
# ren.glClearColor(0, 0, 0)
#
# ren.glColor(1, 1, 1)
#
# ren.glViewPort(0, 0, 499, 499)
# s = 2/500
# i = -1
# while (i <= 1):
#     j = -1
#     while (j <= 1):
#         if randint(0,1) == 0:
#             ren.glVertex(i, j)
#         j += s
#     i += s
#
# ren.glFinish('item6')

###### ------

###### Item 7
#
# width = 500
# height = 500
# ren.glCreateWindow(width, height)
#
# ren.glViewPort(0, 0, width, height)
# s = 2/500
# i = -1
# while (i <= 1):
#     j = -1
#     while (j <= 1):
#         r = uniform(0, 1)
#         g = uniform(0, 1)
#         b = uniform(0, 1)
#         # print(r)
#         # print(g)
#         # print(b)
#         ren.glColor(r, g, b)
#         ren.glVertex(i, j)
#         j += s
#     i += s
#
# ren.glFinish('item7')

###### ------

###### Item 8

# width = 500
# height = 500
# ren.glCreateWindow(width, height)
# ren.glClearColor(0, 0, 0)
#
# ren.glColor(1, 1, 1)
#
# for i in range(0, width, 5):
#     for j in range(0, height, 5):
#         num = uniform(0, 1)
#         if (num < 0.008):
#             type = randint(1, 3)
#             if (type == 1):
#                 ren.glViewPort(i, j, 5, 5)
#                 ren.glVertex(0, 0)
#                 ren.glVertex(0, 0.5)
#                 ren.glVertex(0, 1)
#                 ren.glVertex(0, -0.5)
#                 ren.glVertex(0, -1)
#                 ren.glVertex(0.5, 0)
#                 ren.glVertex(1, 0)
#                 ren.glVertex(-0.5, 0)
#                 ren.glVertex(-1, 0)
#                 ren.glVertex(0.5, 0.5)
#                 ren.glVertex(-0.5, 0.5)
#                 ren.glVertex(0.5, -0.5)
#                 ren.glVertex(-0.5, -0.5)
#
#             elif (type == 2):
#                 ren.glViewPort(i,j,3,3)
#                 ren.glVertex(0, 0)
#                 ren.glVertex(0, 1)
#                 ren.glVertex(0, -1)
#                 ren.glVertex(1, 0)
#                 ren.glVertex(-1, 0)
#
#             elif (type == 3):
#                 ren.glViewPort(i,j,1,1)
#                 ren.glVertex(0,0)
#
# ren.glFinish('item8')

###### ------

###### Item 9

width = 192
height = 160
ren.glCreateWindow(width, height)
ren.glClearColor(0, 0, 0)

vpWidth = 12
vpHeight = 100
ren.glColor(1, 1, 1)
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
ren.glColor(1, 1, 1)
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

ren.glFinish('item9')

###### ------
