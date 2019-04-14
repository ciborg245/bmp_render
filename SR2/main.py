from render import Render
import examples as ex

ren = Render()

ren.glCreateWindow(600, 400)
ren.glClearColor(0, 0, 0)
ren.glViewPort(0, 0, 600, 400)

ren.glLine(-1, 0.7, 1, 0.4)
ren.glLine(-0.5, -0.5, -0.55, -0.2)
ren.glLine(-0.2, -0.5, -0.2, 1)
ren.glLine(0, -0.8, 1, -0.8)

ren.display('out')
