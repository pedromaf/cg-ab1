from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480


def RenderScene():
    glClear(GL_COLOR_BUFFER_BIT)
    glFlush()


def SetupRC():
    glClearColor(0.0, 0.0, 0.0, 1.0)


# main
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
glutCreateWindow("Simple")
glutDisplayFunc(RenderScene)
SetupRC()

glutMainLoop()
