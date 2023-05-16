from OpenGL.GL import *
from OpenGL.GLUT import *
from math import *

from texture_handler import load_texture

class Fan:
    def __init__(self, x, y, z, size):
        self.x = x
        self.y = y
        self.z = z
        self.rotation_angle = 0.0
        self.size = size
        self.blade_texture_id = None
    
    def draw(self):
        if self.blade_texture_id == None:
            self.blade_texture_id = load_texture("textures/fan_blade.jpg")

        glColor3f(1, 1, 1)

        glPushMatrix()

        glTranslate(self.x, self.y, self.z)
        glScale(self.size, self.size, self.size)
        glRotatef(self.rotation_angle, 0.0, 1.0, 0.0)

        self.__draw_object()
        
        glPopMatrix()

        glNormal3f(0,0,-1)

        glPushMatrix()
        glTranslate(self.x, self.y, self.z)
        glScale(self.size, self.size, self.size)
        
        glColor3f(0.4, 0.4, 0.4)
        self.__draw_cylinder(2.0, 0.7, 360)

        glPopMatrix()
    
    def __draw_cylinder(self, height, radius, sides):
        glBegin(GL_TRIANGLE_STRIP)
        for i in range(sides + 1):
            angle = 2 * pi * i / sides
            x = radius * cos(angle)
            z = radius * sin(angle)
            glVertex3f(x, 0, z)
            glVertex3f(x, height, z)
        glEnd()

        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(0, 0, 0)
        for i in range(sides + 1):
            angle = 2 * pi * i / sides
            x = radius * cos(angle)
            z = radius * sin(angle)
            glVertex3f(x, -0.1, z)
        glEnd()

    def animation(self, value):
        self.rotation_angle += 5.0

        if (self.rotation_angle > 360.0):
            self.rotation_angle = 0.0

        glutPostRedisplay()
        glutTimerFunc(10, self.animation, value)

    def __draw_object(self):
        glNormal3f(0, 1, 0)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.blade_texture_id)

        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(0.5, 0.0, 0.5)
        glTexCoord2f(1, 0)
        glVertex3f(5.0, 0.0, 0.5)
        glTexCoord2f(1, 1)
        glVertex3f(5.0, 0.0, -0.5)
        glTexCoord2f(0, 1)
        glVertex3f(0.5, 0.0, -0.5)
        glEnd()

        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(-0.5, 0.0, 0.5)
        glTexCoord2f(1, 0)
        glVertex3f(-5.0, 0.0, 0.5)
        glTexCoord2f(1, 1)
        glVertex3f(-5.0, 0.0, -0.5)
        glTexCoord2f(0, 1)
        glVertex3f(-0.5, 0.0, -0.5)
        glEnd()

        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(0.5, 0.0, -0.5)
        glTexCoord2f(1, 0)
        glVertex3f(0.5, 0.0, -5.0)
        glTexCoord2f(1, 1)
        glVertex3f(-0.5, 0.0, -5.0)
        glTexCoord2f(0, 1)
        glVertex3f(-0.5, 0.0, -0.5)
        glEnd()

        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(0.5, 0.0, 0.5)
        glTexCoord2f(1, 0)
        glVertex3f(0.5, 0.0, 5.0)
        glTexCoord2f(1, 1)
        glVertex3f(-0.5, 0.0, 5.0)
        glTexCoord2f(0, 1)
        glVertex3f(-0.5, 0.0, 0.5)
        glEnd()

        glDisable(GL_TEXTURE_2D)
        
