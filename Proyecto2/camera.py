import pygame
from OpenGL.GL import *
import OpenGL.GL.shaders as shaders
import glm
import pyassimp
import numpy
import math

# pygame

pygame.init()
pygame.display.set_mode((800, 600), pygame.HWSURFACE | pygame.OPENGLBLIT | pygame.DOUBLEBUF)
clock = pygame.time.Clock()
pygame.key.set_repeat(1, 10)


glClearColor(0.18, 0.18, 0.18, 1.0)
glEnable(GL_DEPTH_TEST)
glEnable(GL_TEXTURE_2D)

# shaders

vertex_shader = """
#version 460

layout (location = 0) in vec4 position;
layout (location = 1) in vec4 normal;
layout (location = 2) in vec2 texcoords;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;
uniform vec4 color;
uniform vec4 light;

out vec4 vertexColor;
out vec2 vertexTexcoords;

void main()
{
    float intensity = dot(normal, normalize(light - position));
    gl_Position = projection * view * model * position;
    vertexColor = color * intensity;
    vertexTexcoords = texcoords;
}
"""

fragment_shader = """
#version 460

layout (location = 0) out vec4 diffuseColor;

in vec4 vertexColor;
in vec2 vertexTexcoords;

uniform sampler2D tex;

void main()
{
    diffuseColor = vertexColor * texture(tex, vertexTexcoords);
}
"""


shader1 = shaders.compileProgram(
    shaders.compileShader(vertex_shader, GL_VERTEX_SHADER),
    shaders.compileShader(fragment_shader,GL_FRAGMENT_SHADER)
)

shader = shader1

glUseProgram(shader)


# matrixes
model = glm.mat4(1)
view = glm.mat4(1)
projection = glm.perspective(glm.radians(45), 800/600, 0.1, 1000.0)

glViewport(0, 0, 800, 600)


scene = pyassimp.load('./models/moscow.obj')

texture_surface = pygame.image.load("./models/body_diff.png")
texture_data = pygame.image.tostring(texture_surface, "RGB", 1)
width = texture_surface.get_width()
height = texture_surface.get_height()

light_intensity = 1
light_intensity_x = 1
light_intensity_y = 1
light_intensity_z = 1



def glize(node):
    # global light_intensity

    model = node.transformation.astype(numpy.float32)

    for mesh in node.meshes:
        material = dict(mesh.material.properties.items())

        texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, texture_data)
        glGenerateMipmap(GL_TEXTURE_2D)

        vertex_data = numpy.hstack((
            numpy.array(mesh.vertices, dtype=numpy.float32),
            numpy.array(mesh.normals, dtype=numpy.float32),
            numpy.array(mesh.texturecoords[0], dtype=numpy.float32)
        ))

        faces = numpy.hstack(
            numpy.array(mesh.faces, dtype=numpy.int32)
        )

        vertex_buffer_object = glGenVertexArrays(1)
        glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer_object)
        glBufferData(GL_ARRAY_BUFFER, vertex_data.nbytes, vertex_data, GL_STATIC_DRAW)

        glVertexAttribPointer(0, 3, GL_FLOAT, False, 9 * 4, None)
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(1, 3, GL_FLOAT, False, 9 * 4, ctypes.c_void_p(3 * 4))
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(2, 3, GL_FLOAT, False, 9 * 4, ctypes.c_void_p(6 * 4))
        glEnableVertexAttribArray(2)


        element_buffer_object = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, element_buffer_object)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, faces.nbytes, faces, GL_STATIC_DRAW)

        glUniformMatrix4fv(
            glGetUniformLocation(shader, "model"), 1 , GL_FALSE,
            model
        )
        glUniformMatrix4fv(
            glGetUniformLocation(shader, "view"), 1 , GL_FALSE,
            glm.value_ptr(view)
        )
        glUniformMatrix4fv(
            glGetUniformLocation(shader, "projection"), 1 , GL_FALSE,
            glm.value_ptr(projection)
        )

        diffuse = mesh.material.properties["diffuse"]

        glUniform4f(
            glGetUniformLocation(shader, "color"),
            *diffuse,
            1
        )

        glUniform4f(
            glGetUniformLocation(shader, "light"),
            camera.x * light_intensity, 0, camera.z * light_intensity, 0
        )

        glDrawElements(GL_TRIANGLES, len(faces), GL_UNSIGNED_INT, None)


    for child in node.children:
        glize(child)


camera = glm.vec3(0, 0, 40)

CAMERA_SPEED = math.pi / 12           # 15°
ZOOM = 0.5

rotation = 0

def process_input():
    global radius, rotation, light_intensity
    # global light_intensity_x, light_intensity_y, light_intensity_z

    radius = numpy.sqrt((camera.x**2 + camera.z**2))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
            return True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                rotation += CAMERA_SPEED

                camera.x = math.sin(rotation) * radius
                camera.z = math.cos(rotation) * radius

            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                rotation -= CAMERA_SPEED

                camera.x = math.sin(rotation) * radius
                camera.z = math.cos(rotation) * radius

            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if radius < 75:
                    radius += ZOOM

                    camera.x = math.sin(rotation) * radius
                    camera.z = math.cos(rotation) * radius

            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                if radius > 15:
                    radius -= ZOOM

                    camera.x = math.sin(rotation) * radius
                    camera.z = math.cos(rotation) * radius

            elif event.key == pygame.K_f:
                if camera.y < 40:
                    camera.y += ZOOM

            elif event.key == pygame.K_r:
                if camera.y > -40:
                    camera.y -= ZOOM

            elif event.key == pygame.K_j:
                if light_intensity <= 1:
                    light_intensity += 0.05

            elif event.key == pygame.K_l:
                if light_intensity > -0.8:
                    light_intensity -= 0.05

    return False


done = False
while not done:
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    view = glm.lookAt(camera, glm.vec3(6, 0, 0.5), glm.vec3(0, 1, 0))

    glize(scene.rootnode)

    done = process_input()
    clock.tick(10)
    pygame.display.flip()
