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
# ren.glViewPort(0, 0, 499, 499)
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

width = 100
height = 100
ren.glCreateWindow(width, height)
ren.glClearColor(0, 0, 0)

ren.glColor(1, 1, 1)

ren.glViewPort(0, 0, width-1, height-1)
s = 2/50
i = -1
while (i <= 1):
    j = -1
    while (j <= 1):
        if randint(0,1) == 0:
            seed(trunc(i*j*100))
            r = uniform(0, 1)
            g = uniform(0, 1)
            b = uniform(0, 1)
            ren.glClearColor(r, g, b)
            ren.glVertex(i, j)
        j += s
    i += s

ren.glFinish('item7')

###### ------
