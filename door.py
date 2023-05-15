from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from texture_handler import load_texture

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
        self.door_texture_id = None

    def __draw_object(self):

        depth = 0.5

        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.door_texture_id)

        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(self.x,              self.y, self.z)
        glTexCoord2f(1, 0)
        glVertex3f(self.x + self.width, self.y, self.z)
        glTexCoord2f(1, 1)
        glVertex3f(self.x + self.width, self.y + self.height, self.z)
        glTexCoord2f(0, 1)
        glVertex3f(self.x,              self.y + self.height, self.z)
        glEnd()


        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(self.x,              self.y, self.z - depth)
        glTexCoord2f(1, 0)
        glVertex3f(self.x + self.width, self.y, self.z - depth)
        glTexCoord2f(1, 1)
        glVertex3f(self.x + self.width, self.y + self.height, self.z - depth)
        glTexCoord2f(0, 1)
        glVertex3f(self.x,              self.y + self.height, self.z - depth)
        glEnd()

        glDisable(GL_TEXTURE_2D)

        glColor3f(0.4, 0.4, 0.4)

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
        radius = 0.5

        glColor3f(0.35, 0.35, 0.35)
        glPushMatrix()
        glTranslatef(self.x + self.width * 0.9, self.y +
                     self.height * 0.48, self.z - depth - radius)
        glutSolidSphere(radius, 25, 25)
        glPopMatrix()
        
        glPushMatrix()
        glTranslatef(self.x + self.width * 0.9, self.y +
                     self.height * 0.48, self.z + depth)
        glutSolidSphere(radius, 25, 25)
        glPopMatrix()

    def draw(self):
        if self.door_texture_id == None:
            self.door_texture_id = load_texture("textures/door.jpg")

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
