from render import Render
import obj as obj

ren = Render()
ren.glCreateWindow(800, 600)

print('Elija el modelo a cargar:')
print('1. Osos')
print('2. Rostro')
try:
    res = int(input())
    if res == 1:
        ren.loadObj('./models/bears.obj', 9, 2, 40)
        ren.glFinish('out')
    elif res == 2:
        ren.loadObj('./models/face.obj', translateX=25, translateY=8,scale=15)
        ren.glFinish('out')
    else:
        print('Opcion invalida.')
except e:
    print('Opcion invalida.')
