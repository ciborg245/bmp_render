from render import Render
from texture import Texture

ren = Render()
ren.glCreateWindow(600, 800)
# ren.loadObj('./models/bears.obj', 9, 2, 40)

tex = Texture('./models/model.bmp')

## Medium shot
ren.lookAt(
    cameraPos= [1, 0, 8],
    cameraTarget= [0.4, 0, 3],
    up= [0, 1, 0]
)
ren.loadObj(
    filename='./models/model.obj',
    translate=[0, 0, 0],
    scale=[1, 1, 1],
    rotate=[0, 0, 0],
    texture=tex,
    light=[0, 0, 1]
)
ren.glFinish('medium')

## Dutch angle
ren.glCreateWindow(600, 800)
ren.lookAt(
    cameraPos= [-1, 0, 2],
    cameraTarget= [0, 0, 0],
    up= [0, 1, 1]
)

ren.loadObj(
    filename='./models/model.obj',
    translate=[0, 0, 0],
    scale=[1, 1, 1],
    rotate=[0, 0, 0],
    texture=tex,
    light=[0.5, 0, 0.8]
)
ren.glFinish('dutch_angle')


## Low angle angle
ren.glCreateWindow(600, 800)
ren.lookAt(
    cameraPos= [1, -12, 20],
    cameraTarget= [0, 0, 0],
    up= [0, 1, 0]
)

ren.loadObj(
    filename='./models/model.obj',
    translate=[0, 0, 0],
    scale=[1, 1, 1],
    rotate=[0, 0, 0],
    texture=tex,
    light=[0, 0, 1]
)
ren.glFinish('low_angle')

## High angle
ren.glCreateWindow(600, 800)
ren.lookAt(
    cameraPos= [1, 2, 4],
    cameraTarget= [0.7, 1.4, 2.5],
    up= [0, 1, 0]
)

ren.loadObj(
    filename='./models/model.obj',
    translate=[0, 0, 0],
    scale=[1, 1, 1],
    rotate=[0, 0, 0],
    texture=tex,
    light=[-0.5, 0, 0.7]
)
ren.glFinish('high_angle')

# ren.glFinish('medium')
# ren.glFinish('out')
