from OpenGL.GL import *
from OpenGL.GLUT import *
from math import *

class Fan:
    def __init__(self, x, y, z, size):
        self.x = x
        self.y = y
        self.z = z
        self.rotation_angle = 0.0
        self.size = size
    
    def draw(self):
        glPushMatrix()

        glTranslate(self.x, self.y, self.z)
        glScale(self.size, self.size, self.size)
        glRotatef(self.rotation_angle, 0.0, 1.0, 0.0)

        self.__draw_object()
        
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
        glVertex3f(0, height, 0)
        for i in range(sides + 1):
            angle = 2 * pi * i / sides
            x = radius * cos(angle)
            z = radius * sin(angle)
            glVertex3f(x, height, z)
        glEnd()

        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(0, 0, 0)
        for i in range(sides + 1):
            angle = 2 * pi * i / sides
            x = radius * cos(angle)
            z = radius * sin(angle)
            glVertex3f(x, 0, z)
        glEnd()

    def animation(self, value):
        self.rotation_angle += 5.0

        if (self.rotation_angle > 360.0):
            self.rotation_angle = 0.0

        glutPostRedisplay()
        glutTimerFunc(10, self.animation, value)

    def __draw_object(self):
        glColor3f(0.8, 0.8, 0.8)

        glBegin(GL_QUADS)
        glVertex3f(0.5, 0.0, 0.5)
        glVertex3f(5.0, 0.0, 0.5)
        glVertex3f(5.0, 0.0, -0.5)
        glVertex3f(0.5, 0.0, -0.5)
        glEnd()

        glBegin(GL_QUADS)
        glVertex3f(-0.5, 0.0, 0.5)
        glVertex3f(-5.0, 0.0, 0.5)
        glVertex3f(-5.0, 0.0, -0.5)
        glVertex3f(-0.5, 0.0, -0.5)
        glEnd()

        glBegin(GL_QUADS)
        glVertex3f(0.5, 0.0, -0.5)
        glVertex3f(0.5, 0.0, -5.0)
        glVertex3f(-0.5, 0.0, -5.0)
        glVertex3f(-0.5, 0.0, -0.5)
        glEnd()

        glBegin(GL_QUADS)
        glVertex3f(0.5, 0.0, 0.5)
        glVertex3f(0.5, 0.0, 5.0)
        glVertex3f(-0.5, 0.0, 5.0)
        glVertex3f(-0.5, 0.0, 0.5)
        glEnd()

        self.__draw_cylinder(2.0, 0.7, 360)
