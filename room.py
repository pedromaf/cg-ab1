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
        glColor3f(1, 0, 0)
        
        glBegin(GL_QUADS)
        glVertex3f(self.x,                        self.y,               self.z)
        glVertex3f(self.x,                        self.y + self.height, self.z)
        glVertex3f(self.x + self.door_position_x, self.y + self.height, self.z)
        glVertex3f(self.x + self.door_position_x, self.y,               self.z)
        glEnd()

        glColor3f(1, 1, 0)
        glBegin(GL_QUADS)
        glVertex3f(self.x + self.door_position_x,                   self.y + self.door_height, self.z)
        glVertex3f(self.x + self.door_position_x,                   self.y + self.height,      self.z)
        glVertex3f(self.x + self.door_position_x + self.door_width, self.y + self.height,      self.z)
        glVertex3f(self.x + self.door_position_x + self.door_width, self.y + self.door_height, self.z)
        glEnd()

        glColor3f(1, 1, 1)
        glBegin(GL_QUADS)
        glVertex3f(self.x + self.door_position_x + self.door_width, self.y + self.height, self.z)
        glVertex3f(self.x + self.door_position_x + self.door_width, self.y,               self.z)
        glVertex3f(self.x + self.width,                             self.y,               self.z)
        glVertex3f(self.x + self.width,                             self.y + self.height, self.z)
        glEnd()

    def draw_room_back_wall(self):
        glColor3f(1, 0, 1)

        glBegin(GL_QUADS)
        glVertex3f(self.x,              self.y + self.height, self.z - self.width)
        glVertex3f(self.x,              self.y,               self.z - self.width)
        glVertex3f(self.x + self.width, self.y,               self.z - self.width)
        glVertex3f(self.x + self.width, self.y + self.height, self.z - self.width)
        glEnd()

    def draw_room_left_wall(self):
        glColor3f(1, 1, 0)

        glBegin(GL_QUADS)
        glVertex3f(self.x, self.y,               self.z)
        glVertex3f(self.x, self.y,               self.z - self.width)
        glVertex3f(self.x, self.y + self.height, self.z - self.width)
        glVertex3f(self.x, self.y + self.height, self.z)
        glEnd()

    def draw_room_right_wall(self):
        glColor3f(0, 1, 1)

        glBegin(GL_QUADS)
        glVertex3f(self.x + self.width, self.y,               self.z)
        glVertex3f(self.x + self.width, self.y,               self.z - self.width)
        glVertex3f(self.x + self.width, self.y + self.height, self.z - self.width)
        glVertex3f(self.x + self.width, self.y + self.height, self.z)
        glEnd()

    def draw_room_roof(self):
        glColor3f(0, 1, 0)

        glBegin(GL_QUADS)
        glVertex3f(self.x,              self.y + self.height, self.z)
        glVertex3f(self.x,              self.y + self.height, self.z - self.width)
        glVertex3f(self.x + self.width, self.y + self.height, self.z - self.width)
        glVertex3f(self.x + self.width, self.y + self.height, self.z)
        glEnd()

    def draw_room_floor(self):
        glColor3f(0, 0, 1)

        glBegin(GL_QUADS)
        glVertex3f(self.x,              self.y, self.z)
        glVertex3f(self.x,              self.y, self.z - self.width)
        glVertex3f(self.x + self.width, self.y, self.z - self.width)
        glVertex3f(self.x + self.width, self.y, self.z)
        glEnd()

    def draw(self):
        self.draw_room_front_wall()
        self.draw_room_back_wall()
        self.draw_room_left_wall()
        self.draw_room_right_wall()
        self.draw_room_roof()
        self.draw_room_floor()

    def move_to(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def translate(self, x, y, z):
        self.x += x
        self.y += y
        self.z += z

