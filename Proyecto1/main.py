from render import Render
from texture import Texture

ren = Render()
ren.glCreateWindow(600, 720)


# Ping pong table
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

## Ping pong paddle 1
tex = Texture('./models/paddle.bmp')
ren.lookAt(
    cameraPos= [-1, -3, 6],
    cameraTarget= [0.55, -0.18, 0],
    up= [0, 1, 5]
)
ren.loadObj(
    filename='./models/paddle.obj',
    translate=[0, 0, 0],
    scale=[0.008, 0.008, 0.008],
    rotate=[-1, 0, 0],
    texture=tex,
    light=[0.5, 0.3, 0.8]
)

## Ping pong paddle 2
tex = Texture('./models/paddle.bmp')
ren.lookAt(
    cameraPos= [-1, -3, 6],
    cameraTarget= [-0.52, 0.06, 0],
    up= [0, 1, -2.2]
)
ren.loadObj(
    filename='./models/paddle.obj',
    translate=[0, 0, 0],
    scale=[0.008, 0.008, 0.008],
    rotate=[-1, 0, 0],
    texture=tex,
    light=[0.5, 0.3, 0.8]
)
# Asian man
tex = Texture('./models/suit01_diffuse.bmp')
ren.lookAt(
    cameraPos= [4, 0, -10],
    cameraTarget= [-0.3, 0.52, -1.6],
    up= [0, 1, 0]
)
ren.loadObj(
    filename='./models/Old_Asian_Business_Man.obj',
    translate=[0, 0, 0],
    scale=[0.0007, 0.0007, 0.0007],
    rotate=[0, 0, 0],
    texture=tex,
    light=[0.5, 0.3, 0.8]
)

# Dragon
tex = Texture('./models/dragon.bmp')
ren.lookAt(
    cameraPos= [0.5, 0, 3],
    cameraTarget= [-0.6, -0.6, 0],
    up= [0.3, 1, 0]
)
ren.loadObj(
    filename='./models/dragon.obj',
    translate=[0, 0, 0],
    scale=[0.004, 0.004, 0.004],
    rotate=[0, 0, 0],
    texture=tex,
    light=[0.5, 0.3, 0.8]
)

ren.glFinish('out')
