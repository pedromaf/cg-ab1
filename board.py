from OpenGL.GL import *
from OpenGL.GLUT import *
from math import *
from texture_handler import load_texture


class Board:
    def __init__(self, x, y, z, height, width, depth, size, rotation_angle):
        self.x = x
        self.y = y
        self.z = z
        self.height = height
        self.width = width
        self.depth = depth
        self.size = size
        self.rotation_angle = rotation_angle
        self.content_texture_id = None
        self.border_texture_id = None

    def draw(self):
        glPushMatrix()
        glScalef(self.size, self.size, self.size)
        glTranslate(self.x, self.y, self.z)
        glRotate(self.rotation_angle, 0, 1, 0)
        self.__draw_object()
        glPopMatrix()

    def __mainBoard(self):
        glColor3f(0.8, 0.8, 0.8)     

        # frente
        glBegin(GL_QUADS)
        glVertex3f(-self.width/2, -self.height/2,  -self.depth/2)
        glVertex3f(-self.width/2, self.height/2,  -self.depth/2)
        glVertex3f(self.width/2, self.height/2,  -self.depth/2)
        glVertex3f(self.width/2, -self.height/2,  -self.depth/2)
        glEnd()

        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.content_texture_id)

        # costas
        glBegin(GL_QUADS)
        glTexCoord2f(1, 1)
        glNormal3f(-self.width/2, self.height/2, -self.depth/2)
        glVertex3f(-self.width/2, -self.height/2,  self.depth/2)
        glTexCoord2f(1, 0)
        glNormal3f(-self.width/2, self.height/2, -self.depth/2)
        glVertex3f(-self.width/2, self.height/2,  self.depth/2)
        glTexCoord2f(0, 0)
        glNormal3f(-self.width/2, self.height/2, -self.depth/2)
        glVertex3f(self.width/2, self.height/2,  self.depth/2)
        glTexCoord2f(0, 1)
        glNormal3f(-self.width/2, self.height/2, -self.depth/2)
        glVertex3f(self.width/2, -self.height/2,  self.depth/2)
        glEnd()

        glDisable(GL_TEXTURE_2D)

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
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.border_texture_id)

        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(-self.width * 0.1, 0.0,  -self.width * 0.05)
        glTexCoord2f(1, 0)
        glVertex3f(-self.width * 0.1, 0.0,  self.width * 0.05)
        glTexCoord2f(1, 1)
        glVertex3f(self.width * 0.1, 0.0,  self.width * 0.05)
        glTexCoord2f(0, 1)
        glVertex3f(self.width * 0.1, 0.0,  -self.width * 0.05)
        glEnd()

        glDisable(GL_TEXTURE_2D)

    def __edgeBottomUp(self, percent):
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.border_texture_id)

        # frente
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(-self.width/2, -self.height * percent/2,  -self.depth)
        glTexCoord2f(1, 0)
        glVertex3f(-self.width/2, self.height * percent/2,  -self.depth)
        glTexCoord2f(1, 1)
        glVertex3f(self.width/2, self.height * percent/2,  -self.depth)
        glTexCoord2f(0, 1)
        glVertex3f(self.width/2, -self.height * percent/2,  -self.depth)
        glEnd()

        # costas
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(-self.width/2, -self.height * percent/2,  self.depth)
        glTexCoord2f(1, 0)
        glVertex3f(-self.width/2, self.height * percent/2,  self.depth)
        glTexCoord2f(1, 1)
        glVertex3f(self.width/2, self.height * percent/2,  self.depth)
        glTexCoord2f(0, 1)
        glVertex3f(self.width/2, -self.height * percent/2,  self.depth)
        glEnd()

        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(-self.width/2, -self.height * percent/2,  -self.depth)
        glTexCoord2f(1, 0)
        glVertex3f(-self.width/2, -self.height * percent/2,  self.depth)
        glTexCoord2f(1, 1)
        glVertex3f(-self.width/2, self.height * percent/2,  self.depth)
        glTexCoord2f(0, 1)
        glVertex3f(-self.width/2, self.height * percent/2,  -self.depth)
        glEnd()

        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(self.width/2, -self.height * percent/2,  -self.depth)
        glTexCoord2f(1, 0)
        glVertex3f(self.width/2, -self.height * percent/2,  self.depth)
        glTexCoord2f(1, 1)
        glVertex3f(self.width/2, self.height * percent/2,  self.depth)
        glTexCoord2f(0, 1)
        glVertex3f(self.width/2, self.height * percent/2,  -self.depth)
        glEnd()

        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(-self.width/2, -self.height * percent/2,  -self.depth)
        glTexCoord2f(1, 0)
        glVertex3f(-self.width/2, -self.height * percent/2,  self.depth)
        glTexCoord2f(1, 1)
        glVertex3f(self.width/2, -self.height * percent/2,  self.depth)
        glTexCoord2f(0, 1)
        glVertex3f(self.width/2, -self.height * percent/2,  -self.depth)
        glEnd()

        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(-self.width/2, self.height * percent/2,  -self.depth)
        glTexCoord2f(1, 0)
        glVertex3f(-self.width/2, self.height * percent/2,  self.depth)
        glTexCoord2f(1, 1)
        glVertex3f(self.width/2, self.height * percent/2,  self.depth)
        glTexCoord2f(0, 1)
        glVertex3f(self.width/2, self.height * percent/2,  -self.depth)
        glEnd()

        glDisable(GL_TEXTURE_2D)

    def __edgeLeftRight(self, percent):
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.border_texture_id)

        # frente
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(-self.width * percent/2, -self.height/2,  -self.depth)
        glTexCoord2f(1, 0)
        glVertex3f(-self.width * percent/2, self.height/2,  -self.depth)
        glTexCoord2f(1, 1)
        glVertex3f(self.width * percent/2, self.height/2,  -self.depth)
        glTexCoord2f(0, 1)
        glVertex3f(self.width * percent/2, -self.height/2,  -self.depth)
        glEnd()

        # costas
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(-self.width * percent/2, -self.height/2,  self.depth)
        glTexCoord2f(1, 0)
        glVertex3f(-self.width * percent/2, self.height/2,  self.depth)
        glTexCoord2f(1, 1)
        glVertex3f(self.width * percent/2, self.height/2,  self.depth)
        glTexCoord2f(0, 1)
        glVertex3f(self.width * percent/2, -self.height/2,  self.depth)
        glEnd()

        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(-self.width * percent/2, -self.height/2,  -self.depth)
        glTexCoord2f(1, 0)
        glVertex3f(-self.width * percent/2, -self.height/2,  self.depth)
        glTexCoord2f(1, 1)
        glVertex3f(-self.width * percent/2, self.height/2,  self.depth)
        glTexCoord2f(0, 1)
        glVertex3f(-self.width * percent/2, self.height/2,  -self.depth)
        glEnd()

        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(self.width * percent/2, -self.height/2,  -self.depth)
        glTexCoord2f(1, 0)
        glVertex3f(self.width * percent/2, -self.height/2,  self.depth)
        glTexCoord2f(1, 1)
        glVertex3f(self.width * percent/2, self.height/2,  self.depth)
        glTexCoord2f(0, 1)
        glVertex3f(self.width * percent/2, self.height/2,  -self.depth)
        glEnd()

        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(-self.width * percent/2, -self.height/2,  -self.depth)
        glTexCoord2f(1, 0)
        glVertex3f(-self.width * percent/2, -self.height/2,  self.depth)
        glTexCoord2f(1, 1)
        glVertex3f(self.width * percent/2, -self.height/2,  self.depth)
        glTexCoord2f(0, 1)
        glVertex3f(self.width * percent/2, -self.height/2,  -self.depth)
        glEnd()

        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(-self.width * percent/2, self.height/2,  -self.depth)
        glTexCoord2f(1, 0)
        glVertex3f(-self.width * percent/2, self.height/2,  self.depth)
        glTexCoord2f(1, 1)
        glVertex3f(self.width * percent/2, self.height/2,  self.depth)
        glTexCoord2f(0, 1)
        glVertex3f(self.width * percent/2, self.height/2,  -self.depth)
        glEnd()

        glDisable(GL_TEXTURE_2D)

    def __draw_object(self):
        if self.content_texture_id == None:
            self.content_texture_id = load_texture("textures/board_content.png")

        if self.border_texture_id == None:
            self.border_texture_id = load_texture("textures/aluminium.jpg")

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
