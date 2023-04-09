from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480


# called to draw scene
def RenderScene():
    step = 0.0

    # clear the window with current clearing color
    glClear(GL_COLOR_BUFFER_BIT)

    # set current drawing color to red
    glColor3f(1.0, 1.0, 0.0)

    # draw a filled rectangle with current color
    glRectf(-25.0, 25.0, 25.0, -25.0)

    # flush drawing commands
    glFlush()


# set up the rendering state
def SetupRC():

    # set clear color buffer to blue
    glClearColor(0.0, 0.0, 0.0, 1.0)


# called by GLUT library when the window has changed size
def ChangeSize(width: GLsizei, height: GLsizei):
    # prevent a divide by zero
    if height == 0:
        h = 1

    # set Viewport to window dimensions
    glViewport(0, 0, width, height)

    # reset coordinate system
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # stablish a clipping volume (left, right, bottom, top, near, far)
    aspectRatio = float(width) / float(height)

    if width <= height:
        glOrtho(-100.0, 100.0, -100.0 / aspectRatio,
                100.0 / aspectRatio, 1.0, -1.0)
    else:
        glOrtho(-100.0 * aspectRatio, 100.0 * aspectRatio, -100.0,
                100.0, 1.0, -1.0)

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
