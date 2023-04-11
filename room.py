from OpenGL.GL import *

class Room:
    def __init__ (self, x, y, z, width, height, door_width, door_height, door_position_x):
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.height = height
        self.door_width = door_width
        self.door_height = door_height
        self.door_position_x = door_position_x
    
    def draw_room_front_wall(self):
        glBegin(GL_QUADS)
        glVertex3f(self.x,                        self.y,               self.z)
        glVertex3f(self.x,                        self.y + self.height, self.z)
        glVertex3f(self.x + self.door_position_x, self.y + self.height, self.z)
        glVertex3f(self.x + self.door_position_x, self.y,               self.z)
        glEnd()

        glBegin(GL_QUADS)
        glVertex3f(self.x + self.door_position_x,                   self.y + self.door_height, self.z)
        glVertex3f(self.x + self.door_position_x,                   self.y + self.height,      self.z)
        glVertex3f(self.x + self.door_position_x + self.door_width, self.y + self.height,      self.z)
        glVertex3f(self.x + self.door_position_x + self.door_width, self.y + self.door_height, self.z)
        glEnd()

        glBegin(GL_QUADS)
        glVertex3f(self.x + self.door_position_x + self.door_width, self.y + self.height, self.z)
        glVertex3f(self.x + self.door_position_x + self.door_width, self.y,               self.z)
        glVertex3f(self.x + self.width,                             self.y,               self.z)
        glVertex3f(self.x + self.width,                             self.y + self.height, self.z)
        glEnd()

    def draw_room_back_wall(self):
        glBegin(GL_QUADS)
        glVertex3f(self.x,              self.y + self.height, self.z - self.width)
        glVertex3f(self.x,              self.y,               self.z - self.width)
        glVertex3f(self.x + self.width, self.y,               self.z - self.width)
        glVertex3f(self.x + self.width, self.y + self.height, self.z - self.width)
        glEnd()

    def draw_room_left_wall(self):
        glBegin(GL_QUADS)
        glVertex3f(self.x, self.y,               self.z)
        glVertex3f(self.x, self.y,               self.z - self.width)
        glVertex3f(self.x, self.y + self.height, self.z - self.width)
        glVertex3f(self.x, self.y + self.height, self.z)
        glEnd()

    def draw_room_right_wall(self):
        glBegin(GL_QUADS)
        glVertex3f(self.x + self.width, self.y,               self.z)
        glVertex3f(self.x + self.width, self.y,               self.z - self.width)
        glVertex3f(self.x + self.width, self.y + self.height, self.z - self.width)
        glVertex3f(self.x + self.width, self.y + self.height, self.z)
        glEnd()

    def draw_room_roof(self):
        glBegin(GL_QUADS)
        glVertex3f(self.x,              self.y + self.height, self.z)
        glVertex3f(self.x,              self.y + self.height, self.z - self.width)
        glVertex3f(self.x + self.width, self.y + self.height, self.z - self.width)
        glVertex3f(self.x + self.width, self.y + self.height, self.z)
        glEnd()

    def draw_room_floor(self):
        glBegin(GL_QUADS)
        glVertex3f(self.x,              self.y, self.z)
        glVertex3f(self.x,              self.y, self.z - self.width)
        glVertex3f(self.x + self.width, self.y, self.z - self.width)
        glVertex3f(self.x + self.width, self.y, self.z)
        glEnd()

    def draw(self):
        glColor3f(0.4, 0.4, 0.4)

        self.draw_room_front_wall()
        self.draw_room_back_wall()

        glColor3f(0.5, 0.5, 0.5)

        self.draw_room_left_wall()
        self.draw_room_right_wall()

        glColor3f(0.1, 0.1, 0.1)
        
        self.draw_room_floor()

        glColor3f(0.3, 0.3, 0.3)

        self.draw_room_roof()

