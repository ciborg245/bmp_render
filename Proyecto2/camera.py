import pygame
from OpenGL.GL import *

pygame.init()
pygame.display.set_mode((800, 600), pygame.OPENGL | pygame.DOUBLEBUF)
clock = pygame.time.Clock()
pygame.key.set_repeat(1, 10)


glClearColor(0.18, 0.18, 0.18, 1.0)
glEnable(GL_DEPTH_TEST)
glEnable(GL_TEXTURE_2D)

# shaders

vertex_shader = """
#version 330
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
#version 330
layout (location = 0) out vec4 diffuseColor;
in vec4 vertexColor;
in vec2 vertexTexcoords;
uniform sampler2D tex;
void main()
{
    diffuseColor = vertexColor * texture(tex, vertexTexcoords);
}
"""

shader = shaders.compileProgram(
    shaders.compileShader(vertex_shader, GL_VERTEX_SHADER),
    shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER),
)
glUseProgram(shader)
