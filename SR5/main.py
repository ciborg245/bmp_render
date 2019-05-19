from render import Render
from texture import Texture

ren = Render()
ren.glCreateWindow(600, 800)
# ren.loadObj('./models/bears.obj', 9, 2, 40)

tex = Texture('./models/model.bmp')

ren.loadObj('./models/model.obj',
    translateX=1,
    translateY=1.1,
    scale=300,
    texture=tex,
    light = [0, 0, 1])
    
ren.glFinish('out')
