from OpenGL.GL import *

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
        glColor3f(0.5, 0.3, 0.8)
        glBegin(GL_QUADS)
        glVertex3f(self.x,              self.y, self.z)
        glVertex3f(self.x + self.width, self.y, self.z)
        glVertex3f(self.x + self.width, self.y + self.height, self.z)
        glVertex3f(self.x,              self.y + self.height, self.z)
        glEnd()

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