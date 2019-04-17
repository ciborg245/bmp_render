from render import Render
# import render as ren
import obj as obj
import operator
import timeit as ti


ren = Render()
ren.glCreateWindow(800, 600)
# ren.line_sweeping([100 , 10, 10], [500, 5, 3], [30, 300, 30])
# ren.barycentric_triangle([100, 10, 10], [500, 5, 3], [30, 300, 30])
# ren.loadObj('./models/bears.obj', 9, 2, 40)
ren.loadObj('./models/face.obj', translateX=25, translateY=8,scale=15, triangle=1)
ren.glFinish()


#
# imp = "ren = Render();ren.glCreateWindow(800, 600);"
#
# s = imp + "ren.loadObj('./models/face.obj', translateX=25, translateY=8,scale=15, triangle=0)"
# print("Barycentric algorithm")
# print(ti.timeit(s, setup="from render import Render", number=20))
# s = imp + "ren.loadObj('./models/face.obj', translateX=25, translateY=8,scale=15, triangle=1)"
# print("Line-sweeping algorithm")
# print(ti.timeit(s, setup="from render import Render", number=20))
