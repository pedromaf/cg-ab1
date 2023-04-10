from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def desenha():
    glClearColor(1.0, 1.0, 1.0, 0.0)

    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1.0, 0.0, 0.0)

    glBegin(GL_TRIANGLES)
    glVertex3f(-0.5, -0.5, 0.0)
    glVertex3f(0.0, 0.5, 0.0)
    glVertex3f(0.5, -0.5, 0.0)
    glEnd()

    glFlush()


def teclado(key: int, x: int, y: int):
    if key == 27:
        exit(0)


def init():
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)


def main():

    glutInit()

    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

    glutInitWindowSize(400, 400)

    glutCreateWindow("Primeiro Programa")

    glutDisplayFunc(desenha)

    glutKeyboardFunc(teclado)

    init()

    glutMainLoop()


main()
