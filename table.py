from OpenGL.GL import *
from OpenGL.GLUT import *
from math import *

from texture_handler import load_texture


class Table:
    def __init__(self, x, y, z, height, width, depth, size):
        self.x = x
        self.y = y
        self.z = z
        self.height = height
        self.width = width
        self.depth = depth
        self.size = size
        self.table_texture_id = None
        self.table_foot_texture_id = None

    def draw(self):
        if self.table_texture_id == None:
            self.table_texture_id = load_texture("textures/table.jpg")
            
        if self.table_foot_texture_id == None:
            self.table_foot_texture_id = load_texture("textures/aluminium.jpg")

        glPushMatrix()
        glScalef(self.size, self.size, self.size)
        glTranslatef(self.x, self.y, self.z)
        self.__draw_object()
        glPopMatrix()

    def __tampo(self):
        # tampo
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.table_texture_id)

        glColor3f(1, 1, 1)

        glNormal3f(0, 1, 0)
        glBegin(GL_QUADS)
        glTexCoord2f(1, 0)
        glVertex3f(-self.width/2, self.height, -self.depth/2)
        glTexCoord2f(0, 1)
        glVertex3f(self.width/2, self.height, -self.depth/2)
        glTexCoord2f(1, 1)
        glVertex3f(self.width/2, self.height, self.depth/2)
        glTexCoord2f(0, 0)
        glVertex3f(-self.width/2, self.height, self.depth/2)
        glEnd()

        # tampo de baixo
        glNormal3f(0, -1, 0)
        glBegin(GL_QUADS)
        glTexCoord2f(1, 0)
        glVertex3f(-self.width/2, self.height * 0.95, -self.depth/2)
        glTexCoord2f(0, 1)
        glVertex3f(self.width/2, self.height * 0.95, -self.depth/2)
        glTexCoord2f(1, 1)
        glVertex3f(self.width/2, self.height * 0.95, self.depth/2)
        glTexCoord2f(0, 0)
        glVertex3f(-self.width/2, self.height * 0.95, self.depth/2)
        glEnd()

        glNormal3f(1, 0, 0)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(-self.width/2, self.height * 0.95, -self.depth/2)
        glTexCoord2f(1, 0)
        glVertex3f(self.width/2, self.height * 0.95, -self.depth/2)
        glTexCoord2f(1, 1)
        glVertex3f(self.width/2, self.height, -self.depth/2)
        glTexCoord2f(0, 1)
        glVertex3f(-self.width/2, self.height, -self.depth/2)
        glEnd()

        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(-self.width/2, self.height * 0.95, self.depth/2)
        glTexCoord2f(1, 0)
        glVertex3f(self.width/2, self.height * 0.95, self.depth/2)
        glTexCoord2f(1, 1)
        glVertex3f(self.width/2, self.height, self.depth/2)
        glTexCoord2f(0, 1)
        glVertex3f(-self.width/2, self.height, self.depth/2)
        glEnd()

        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(-self.width/2, self.height * 0.95, -self.depth/2)
        glTexCoord2f(1, 0)
        glVertex3f(-self.width/2, self.height * 0.95, self.depth/2)
        glTexCoord2f(1, 1)
        glVertex3f(-self.width/2, self.height, self.depth/2)
        glTexCoord2f(0, 1)
        glVertex3f(-self.width/2, self.height, -self.depth/2)
        glEnd()

        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(self.width/2, self.height * 0.95, -self.depth/2)
        glTexCoord2f(1, 0)
        glVertex3f(self.width/2, self.height * 0.95, self.depth/2)
        glTexCoord2f(1, 1)
        glVertex3f(self.width/2, self.height, self.depth/2)
        glTexCoord2f(0, 1)
        glVertex3f(self.width/2, self.height, -self.depth/2)
        glEnd()

        glDisable(GL_TEXTURE_2D)

    def __perna(self):
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.table_foot_texture_id)

        glBegin(GL_QUADS)
        glTexCoord2f(1, 0)
        glVertex3f(-0.3, 0.0, -0.3)
        glTexCoord2f(0, 0) 
        glVertex3f(0.3, 0.0, -0.3)
        glTexCoord2f(0, 1)
        glVertex3f(0.3, self.height, -0.3)
        glTexCoord2f(1, 1)
        glVertex3f(-0.3, self.height, -0.3)
        glEnd()

        glBegin(GL_QUADS)
        glTexCoord2f(1, 0)
        glVertex3f(-0.3, 0.0, 0.3)
        glTexCoord2f(0, 0)
        glVertex3f(0.3, 0.0, 0.3)
        glTexCoord2f(0, 1)
        glVertex3f(0.3, self.height, 0.3)
        glTexCoord2f(1, 1)
        glVertex3f(-0.3, self.height, 0.3)
        glEnd()

        glBegin(GL_QUADS)
        glTexCoord2f(1, 0)
        glVertex3f(-0.3, 0.0, -0.3)
        glTexCoord2f(0, 0)
        glVertex3f(-0.3, 0.0, 0.3)
        glTexCoord2f(0, 1)
        glVertex3f(-0.3, self.height, 0.3)
        glTexCoord2f(1, 1)
        glVertex3f(-0.3, self.height, -0.3)
        glEnd()

        glBegin(GL_QUADS)
        glTexCoord2f(1, 0)
        glVertex3f(0.3, 0.0, -0.3)
        glTexCoord2f(0, 0)
        glVertex3f(0.3, 0.0, 0.3)
        glTexCoord2f(0, 1)
        glVertex3f(0.3, self.height, 0.3)
        glTexCoord2f(1, 1)
        glVertex3f(0.3, self.height, -0.3)
        glEnd()

        glDisable(GL_TEXTURE_2D)

    def __draw_object(self):
        
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
