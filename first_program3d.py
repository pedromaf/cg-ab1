from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import sin, cos

GL_PI = 3.1415
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 960


# this function does any needed initialization on the rendering context
def SetupRC():

    # black background
    glClearColor(0.0, 0.0, 0.0, 1.0)

    # set drawing color to green
    glColor3f(0.0, 1.0, 0.0)


def points():
    glBegin(GL_POINTS)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(50.0, 50.0, 50.0)
    glEnd()


def lines():
    glBegin(GL_LINES)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(50.0, 50.0, 50.0)
    glEnd()


def radialLines():
    # call only once for all remaining points
    glBegin(GL_LINES)

    angle = 0.0

    # all lines lie in the xy plane
    z = 0.0

    while (angle <= GL_PI):
        # top half of the circle
        x = 50.0 * sin(angle)
        y = 50.0 * cos(angle)
        glVertex3f(x, y, z)  # first endpoint of line

        # bottom half of the circle
        x = 50.0 * sin(angle + GL_PI)
        y = 50.0 * cos(angle + GL_PI)
        glVertex3f(x, y, z)  # second endpoint of line

        angle += GL_PI / 20.0

    # done drawing points
    glEnd()


def lineStrips():
    glBegin(GL_LINE_LOOP)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(50.0, 50.0, 0.0)
    glVertex3f(50.0, 100.0, 0.0)
    glEnd()


def spiral():
    angle = 0.0

    # save the matrix state and do the rotation
    glPushMatrix()
    glRotatef(45.0*GL_PI, 1.0, 0.0, 0.0)
    glRotatef(45.0*GL_PI, 0.0, 1.0, 0.0)

    # set beginning z coordinate
    z = -50.0

    while (angle <= 2.0 * GL_PI * 3.0):
        x = 50.0*sin(angle)
        y = 50.0*cos(angle)

        # specify the point and move the Z value up a little
        glBegin(GL_POINTS)
        glVertex3f(x, y, z)
        glEnd()

        angle += 0.1
        z += 0.5

    # restore transformations
    glPopMatrix()


# called to draw scene
def RenderScene():

    # clear the window with current clearing color
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # save the matrix state and do the rotation
    glPushMatrix()
    glRotatef(15.0, 1.0, 0.0, 0.0)
    glRotatef(30.0, 0.0, 1.0, 0.0)

    # seta a cor para branco
    glColor3f(1.0, 1.0, 1.0)

    # desenha as pernas
    glBegin(GL_LINES)

    # seta a cor para verde
    glColor3f(0.0, 1.0, 0.0)
    # x axis
    glVertex3f(-50.0, 0.0, 0.0)
    glVertex3f(100.0, 0.0, 0.0)

    # seta a cor para azul
    glColor3f(0.0, 0.0, 1.0)
    # y axis
    glVertex3f(0.0, -50.0, 0.0)
    glVertex3f(0.0, 100.0, 0.0)

    # seta a cor para vermelho
    glColor3f(1.0, 0.0, 0.0)
    # z axis
    glVertex3f(0.0, 0.0, -50.0)
    glVertex3f(0.0, 0.0, 100.0)

    glVertex3f(-50.0, 0.0, -50.0)
    glVertex3f(-50.0, -50.0, -50.0)

    glVertex3f(-50.0, 0.0, 50.0)
    glVertex3f(-50.0, -50.0, 50.0)

    glVertex3f(50.0, 0.0, 50.0)
    glVertex3f(50.0, -50.0, 50.0)

    glVertex3f(50.0, 0.0, -50.0)
    glVertex3f(50.0, -50.0, -50.0)
    glEnd()

    glColor3f(0.0, 1.0, 0.0)

    glBegin(GL_QUADS)
    glVertex3f(-50.0, 0.0, -50.0)
    glVertex3f(-50.0, 0.0, 50.0)
    glVertex3f(50.0, 0.0, 50.0)
    glVertex3f(50.0, 0.0, -50.0)
    glEnd()

    # Flush drawing commands
    glutSwapBuffers()


# called by GLUT library when the window has changed size
def ChangeSize(width: GLsizei, height: GLsizei):

    nRange = 100.0

    # prevent a divide by zero
    if height == 0:
        h = 1

    # set Viewport to window dimensions
    glViewport(0, 0, width, height)

    # reset projection matrix stack
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # stablish a clipping volume (left, right, bottom, top, near, far)
    aspectRatio = float(width) / float(height)

    if width <= height:
        glOrtho(-nRange, nRange, -nRange * height / width,
                nRange * height / width, nRange, -nRange)
    else:
        glOrtho(-nRange * width / height, nRange * width / height, -nRange,
                nRange, -nRange, nRange)

    # reset model view matrix stack
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


# main program entry point
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
glutCreateWindow("GLRect")
glutDisplayFunc(RenderScene)
glutReshapeFunc(ChangeSize)
SetupRC()

glutMainLoop()
