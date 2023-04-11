from OpenGL.GL import *
from OpenGL.GLUT import *
from math import *


class Board:
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

    def __mainBoard(self):

        # frente
        glBegin(GL_QUADS)
        glVertex3f(-self.width/2, -self.height/2,  -self.depth/2)
        glVertex3f(-self.width/2, self.height/2,  -self.depth/2)
        glVertex3f(self.width/2, self.height/2,  -self.depth/2)
        glVertex3f(self.width/2, -self.height/2,  -self.depth/2)
        glEnd()

        # costas
        glBegin(GL_QUADS)
        glVertex3f(-self.width/2, -self.height/2,  self.depth/2)
        glVertex3f(-self.width/2, self.height/2,  self.depth/2)
        glVertex3f(self.width/2, self.height/2,  self.depth/2)
        glVertex3f(self.width/2, -self.height/2,  self.depth/2)
        glEnd()

        glColor3f(0.6, 0.6, 0.6)

        glBegin(GL_QUADS)
        glVertex3f(-self.width/2, -self.height/2,  -self.depth/2)
        glVertex3f(-self.width/2, -self.height/2,  self.depth/2)
        glVertex3f(-self.width/2, self.height/2,  self.depth/2)
        glVertex3f(-self.width/2, self.height/2,  -self.depth/2)
        glEnd()

        glBegin(GL_QUADS)
        glVertex3f(self.width/2, -self.height/2,  -self.depth/2)
        glVertex3f(self.width/2, -self.height/2,  self.depth/2)
        glVertex3f(self.width/2, self.height/2,  self.depth/2)
        glVertex3f(self.width/2, self.height/2,  -self.depth/2)
        glEnd()

        glBegin(GL_QUADS)
        glVertex3f(-self.width/2, -self.height/2,  -self.depth/2)
        glVertex3f(-self.width/2, -self.height/2,  self.depth/2)
        glVertex3f(self.width/2, -self.height/2,  self.depth/2)
        glVertex3f(self.width/2, -self.height/2,  -self.depth/2)
        glEnd()

        glBegin(GL_QUADS)
        glVertex3f(-self.width/2, self.height/2,  -self.depth/2)
        glVertex3f(-self.width/2, self.height/2,  self.depth/2)
        glVertex3f(self.width/2, self.height/2,  self.depth/2)
        glVertex3f(self.width/2, self.height/2,  -self.depth/2)
        glEnd()

    def __support(self):
        glColor3f(0.5, 0.5, 0.5)

        glBegin(GL_QUADS)
        glVertex3f(-self.width * 0.1, 0.0,  -self.width * 0.05)
        glVertex3f(-self.width * 0.1, 0.0,  self.width * 0.05)
        glVertex3f(self.width * 0.1, 0.0,  self.width * 0.05)
        glVertex3f(self.width * 0.1, 0.0,  -self.width * 0.05)
        glEnd()

    def __edgeBottomUp(self, percent):
        # frente
        glBegin(GL_QUADS)
        glVertex3f(-self.width/2, -self.height * percent/2,  -self.depth)
        glVertex3f(-self.width/2, self.height * percent/2,  -self.depth)
        glVertex3f(self.width/2, self.height * percent/2,  -self.depth)
        glVertex3f(self.width/2, -self.height * percent/2,  -self.depth)
        glEnd()

        # costas
        glBegin(GL_QUADS)
        glVertex3f(-self.width/2, -self.height * percent/2,  self.depth)
        glVertex3f(-self.width/2, self.height * percent/2,  self.depth)
        glVertex3f(self.width/2, self.height * percent/2,  self.depth)
        glVertex3f(self.width/2, -self.height * percent/2,  self.depth)
        glEnd()

        glColor3f(0.6, 0.6, 0.6)

        glBegin(GL_QUADS)
        glVertex3f(-self.width/2, -self.height * percent/2,  -self.depth)
        glVertex3f(-self.width/2, -self.height * percent/2,  self.depth)
        glVertex3f(-self.width/2, self.height * percent/2,  self.depth)
        glVertex3f(-self.width/2, self.height * percent/2,  -self.depth)
        glEnd()

        glBegin(GL_QUADS)
        glVertex3f(self.width/2, -self.height * percent/2,  -self.depth)
        glVertex3f(self.width/2, -self.height * percent/2,  self.depth)
        glVertex3f(self.width/2, self.height * percent/2,  self.depth)
        glVertex3f(self.width/2, self.height * percent/2,  -self.depth)
        glEnd()

        glBegin(GL_QUADS)
        glVertex3f(-self.width/2, -self.height * percent/2,  -self.depth)
        glVertex3f(-self.width/2, -self.height * percent/2,  self.depth)
        glVertex3f(self.width/2, -self.height * percent/2,  self.depth)
        glVertex3f(self.width/2, -self.height * percent/2,  -self.depth)
        glEnd()

        glBegin(GL_QUADS)
        glVertex3f(-self.width/2, self.height * percent/2,  -self.depth)
        glVertex3f(-self.width/2, self.height * percent/2,  self.depth)
        glVertex3f(self.width/2, self.height * percent/2,  self.depth)
        glVertex3f(self.width/2, self.height * percent/2,  -self.depth)
        glEnd()

    def __edgeLeftRight(self, percent):
        # frente
        glBegin(GL_QUADS)
        glVertex3f(-self.width * percent/2, -self.height/2,  -self.depth)
        glVertex3f(-self.width * percent/2, self.height/2,  -self.depth)
        glVertex3f(self.width * percent/2, self.height/2,  -self.depth)
        glVertex3f(self.width * percent/2, -self.height/2,  -self.depth)
        glEnd()

        # costas
        glBegin(GL_QUADS)
        glVertex3f(-self.width * percent/2, -self.height/2,  self.depth)
        glVertex3f(-self.width * percent/2, self.height/2,  self.depth)
        glVertex3f(self.width * percent/2, self.height/2,  self.depth)
        glVertex3f(self.width * percent/2, -self.height/2,  self.depth)
        glEnd()

        glColor3f(0.6, 0.6, 0.6)

        glBegin(GL_QUADS)
        glVertex3f(-self.width * percent/2, -self.height/2,  -self.depth)
        glVertex3f(-self.width * percent/2, -self.height/2,  self.depth)
        glVertex3f(-self.width * percent/2, self.height/2,  self.depth)
        glVertex3f(-self.width * percent/2, self.height/2,  -self.depth)
        glEnd()

        glBegin(GL_QUADS)
        glVertex3f(self.width * percent/2, -self.height/2,  -self.depth)
        glVertex3f(self.width * percent/2, -self.height/2,  self.depth)
        glVertex3f(self.width * percent/2, self.height/2,  self.depth)
        glVertex3f(self.width * percent/2, self.height/2,  -self.depth)
        glEnd()

        glBegin(GL_QUADS)
        glVertex3f(-self.width * percent/2, -self.height/2,  -self.depth)
        glVertex3f(-self.width * percent/2, -self.height/2,  self.depth)
        glVertex3f(self.width * percent/2, -self.height/2,  self.depth)
        glVertex3f(self.width * percent/2, -self.height/2,  -self.depth)
        glEnd()

        glBegin(GL_QUADS)
        glVertex3f(-self.width * percent/2, self.height/2,  -self.depth)
        glVertex3f(-self.width * percent/2, self.height/2,  self.depth)
        glVertex3f(self.width * percent/2, self.height/2,  self.depth)
        glVertex3f(self.width * percent/2, self.height/2,  -self.depth)
        glEnd()

    def __draw_object(self):
        glColor3f(0.8, 0.8, 0.8)

        self.__mainBoard()
        glPushMatrix()
        glTranslatef(0, -self.height/2, 0.0)
        self.__edgeBottomUp(0.05)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0, self.height/2, 0.0)
        self.__edgeBottomUp(0.05)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-self.width/2.1, 0.0, 0.0)
        self.__edgeLeftRight(0.05)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(self.width/2.1, 0.0, 0.0)
        self.__edgeLeftRight(0.05)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-self.width/2.8, -self.height/2.15, self.width * 0.05)
        self.__support()
        glPopMatrix()
