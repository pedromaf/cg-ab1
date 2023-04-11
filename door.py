from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


class Door:
    def __init__(self, x, y, z, width, height, door_animation_speed):
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.height = height
        self.door_rotation_angle = 0
        self.door_is_opening = False
        self.door_is_closing = False
        self.door_open = False
        self.door_animation_speed = door_animation_speed

    def __draw_object(self):

        depth = 0.5

        glColor3f(0.7, 0.7, 0.7)

        glBegin(GL_QUADS)
        glVertex3f(self.x,              self.y, self.z)
        glVertex3f(self.x + self.width, self.y, self.z)
        glVertex3f(self.x + self.width, self.y + self.height, self.z)
        glVertex3f(self.x,              self.y + self.height, self.z)
        glEnd()

        glBegin(GL_QUADS)
        glVertex3f(self.x,              self.y, self.z - depth)
        glVertex3f(self.x + self.width, self.y, self.z - depth)
        glVertex3f(self.x + self.width, self.y + self.height, self.z - depth)
        glVertex3f(self.x,              self.y + self.height, self.z - depth)
        glEnd()

        glBegin(GL_QUADS)
        glVertex3f(self.x, self.y, self.z)
        glVertex3f(self.x, self.y, self.z - depth)
        glVertex3f(self.x, self.y + self.height, self.z - depth)
        glVertex3f(self.x, self.y + self.height, self.z)
        glEnd()

        glBegin(GL_QUADS)
        glVertex3f(self.x + self.width, self.y, self.z)
        glVertex3f(self.x + self.width, self.y, self.z - depth)
        glVertex3f(self.x + self.width, self.y + self.height, self.z - depth)
        glVertex3f(self.x + self.width, self.y + self.height, self.z)
        glEnd()

        glBegin(GL_QUADS)
        glVertex3f(self.x, self.y + self.height, self.z)
        glVertex3f(self.x, self.y + self.height, self.z - depth)
        glVertex3f(self.x + self.width, self.y + self.height, self.z - depth)
        glVertex3f(self.x + self.width, self.y + self.height, self.z)
        glEnd()

        # maçaneta
        glColor3f(0.5, 0.5, 0.5)
        scale = 0.15
        radius = 0.5

        glPushMatrix()
        glTranslatef(self.width * 0.8, self.height * 0.4, 0.0)

        glBegin(GL_QUADS)
        glVertex3f(self.x,              self.y, self.z - depth - 0.01)
        glVertex3f((self.x + self.width * scale),
                   self.y, self.z - depth - 0.01)
        glVertex3f((self.x + self.width * scale), self.y +
                   self.height * scale, self.z - depth - 0.01)
        glVertex3f(self.x,              self.y +
                   self.height * scale, self.z - depth - 0.01)
        glEnd()
        glPopMatrix()

        glColor3f(0.35, 0.35, 0.35)
        glPushMatrix()
        glTranslatef(self.x + self.width * 0.9, self.y +
                     self.height * 0.48, self.z - depth - radius)
        glutSolidSphere(radius, 25, 25)
        glPopMatrix()

    def draw(self):
        if (self.door_is_opening and self.door_rotation_angle >= 90):
            self.door_is_opening = False
            self.door_open = True
        elif (self.door_is_opening and self.door_rotation_angle < 90):
            self.__rotate()
            self.door_rotation_angle += 0.1 * self.door_animation_speed
        elif (self.door_is_closing and self.door_rotation_angle <= 0):
            self.door_is_closing = False
            self.door_open = False
        elif (self.door_is_closing and self.door_rotation_angle > 0):
            self.__rotate()
            self.door_rotation_angle -= 0.1 * self.door_animation_speed
        elif (self.door_open):
            self.__rotate()
        else:
            self.__draw_object()

    def __rotate(self):
        glPushMatrix()

        glTranslate(self.x, self.y, self.z)
        glRotatef(self.door_rotation_angle, 0, 1, 0)
        glTranslate(-self.x, -self.y, -self.z)

        self.__draw_object()

        glPopMatrix()

    def trigger_animation(self):
        if self.door_open or self.door_is_opening:
            self.door_is_closing = True
            self.door_is_opening = False
        else:
            self.door_is_opening = True
            self.door_is_closing = False
