from render import Render

ren = Render()
ren.glCreateWindow(800, 600)
# ren.loadObj('./models/bears.obj', 9, 2, 40)
ren.loadObj('./models/face.obj', translateX=25, translateY=8,scale=15)
ren.glFinish('out')
