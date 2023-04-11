from OpenGL.GL import *
from OpenGL.GLUT import *
from math import *


class Table:
    def __init__(self, x, y, z, height, width, depth, size):
        self.x = x
        self.y = y
        self.z = z
        self.height = height
        self.width = width
        self.depth = depth
        self.size = size

    def draw(self):
        glPushMatrix()
        glScalef(self.size, self.size, self.size)
        glTranslatef(self.x, self.y, self.z)
        self.__draw_object()
        glPopMatrix()

    def __tampo(self):
        # tampo
        glBegin(GL_QUADS)
        glVertex3f(-self.width/2, self.height, -self.depth/2)
        glVertex3f(self.width/2, self.height, -self.depth/2)
        glVertex3f(self.width/2, self.height, self.depth/2)
        glVertex3f(-self.width/2, self.height, self.depth/2)
        glEnd()

        # tampo de baixo
        glBegin(GL_QUADS)
        glVertex3f(-self.width/2, self.height * 0.95, -self.depth/2)
        glVertex3f(self.width/2, self.height * 0.95, -self.depth/2)
        glVertex3f(self.width/2, self.height * 0.95, self.depth/2)
        glVertex3f(-self.width/2, self.height * 0.95, self.depth/2)
        glEnd()

        glBegin(GL_QUADS)
        glVertex3f(-self.width/2, self.height * 0.95, -self.depth/2)
        glVertex3f(self.width/2, self.height * 0.95, -self.depth/2)
        glVertex3f(self.width/2, self.height, -self.depth/2)
        glVertex3f(-self.width/2, self.height, -self.depth/2)
        glEnd()

        glBegin(GL_QUADS)
        glVertex3f(-self.width/2, self.height * 0.95, self.depth/2)
        glVertex3f(self.width/2, self.height * 0.95, self.depth/2)
        glVertex3f(self.width/2, self.height, self.depth/2)
        glVertex3f(-self.width/2, self.height, self.depth/2)
        glEnd()

        glBegin(GL_QUADS)
        glVertex3f(-self.width/2, self.height * 0.95, -self.depth/2)
        glVertex3f(-self.width/2, self.height * 0.95, self.depth/2)
        glVertex3f(-self.width/2, self.height, self.depth/2)
        glVertex3f(-self.width/2, self.height, -self.depth/2)
        glEnd()

        glBegin(GL_QUADS)
        glVertex3f(self.width/2, self.height * 0.95, -self.depth/2)
        glVertex3f(self.width/2, self.height * 0.95, self.depth/2)
        glVertex3f(self.width/2, self.height, self.depth/2)
        glVertex3f(self.width/2, self.height, -self.depth/2)
        glEnd()

    def __perna(self):
        glColor3f(0.4, 0.20, 0.0)

        glBegin(GL_QUADS)
        glVertex3f(-0.3, 0.0, -0.3)
        glVertex3f(0.3, 0.0, -0.3)
        glVertex3f(0.3, self.height, -0.3)
        glVertex3f(-0.3, self.height, -0.3)
        glEnd()

        glBegin(GL_QUADS)
        glVertex3f(-0.3, 0.0, 0.3)
        glVertex3f(0.3, 0.0, 0.3)
        glVertex3f(0.3, self.height, 0.3)
        glVertex3f(-0.3, self.height, 0.3)
        glEnd()

        glBegin(GL_QUADS)
        glVertex3f(-0.3, 0.0, -0.3)
        glVertex3f(-0.3, 0.0, 0.3)
        glVertex3f(-0.3, self.height, 0.3)
        glVertex3f(-0.3, self.height, -0.3)
        glEnd()

        glBegin(GL_QUADS)
        glVertex3f(0.3, 0.0, -0.3)
        glVertex3f(0.3, 0.0, 0.3)
        glVertex3f(0.3, self.height, 0.3)
        glVertex3f(0.3, self.height, -0.3)
        glEnd()

    def __draw_object(self):
        glColor3f(0.5, 0.25, 0.0)

        glPushMatrix()
        glScalef(1.1, 1, 1.1)
        self.__tampo()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-self.width/2 + 0.3, 0.0, -self.depth/2 + 0.3)
        self.__perna()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-self.width/2 + 0.3, 0.0, self.depth/2 - 0.3)
        self.__perna()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(self.width/2 - 0.3, 0.0, self.depth/2 - 0.3)
        self.__perna()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(self.width/2 - 0.3, 0.0, -self.depth/2 + 0.3)
        self.__perna()
        glPopMatrix()
