from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Axis:
    
    def draw(self, camera_x, camera_y, camera_z, view_range):
        glColor3f(1, 0, 0)
        glBegin(GL_LINES)
        glVertex3f(1, 0, 0)
        glVertex3f(camera_x + view_range, 0, 0)
        glEnd()

        glColor3f(0, 1, 0)
        glBegin(GL_LINES)
        glVertex3f(0, 1, 0)
        glVertex3f(0, camera_y + view_range, 0)
        glEnd()

        glColor3f(0, 0, 1)
        glBegin(GL_LINES)
        glVertex3f(0, 0, 1)
        glVertex3f(0, 0, camera_z + view_range)
        glEnd()