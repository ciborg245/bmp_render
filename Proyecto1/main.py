from render import Render
from texture import Texture

ren = Render()
ren.glCreateWindow(600, 800)


## Ping pong table
tex = Texture('./models/pingpongtable.bmp')
ren.lookAt(
    cameraPos= [4, 5, 1],
    cameraTarget= [0.02, 0.24, -1],
    up= [0, 0, 1]
)
ren.loadObj(
    filename='./models/pingpongtable.obj',
    translate=[0, 0, 0],
    scale=[0.003, 0.003, 0.003],
    rotate=[0, 0, 0],
    texture=tex,
    light=[0.5, 0.3, 0.8]
)
ren.glFinish('out')

# Pattrick
tex = Texture('./models/Skin_Patrick.bmp')
ren.lookAt(
    cameraPos= [-0.8, 0, 10],
    cameraTarget= [1, -0.7, 7],
    up= [0, 1, 0]
)
ren.loadObj(
    filename='./models/Patrick.obj',
    translate=[0, 0, 0],
    scale=[0.3, 0.3, 0.3],
    rotate=[0, 0, 0],
    texture=tex,
    light=[0.5, 0.3, 0.8]
)
ren.glFinish('out')
