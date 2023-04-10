from OpenGL.GL import *

class Room:
    def __init__ (self):
        self.x = 0
        self.y = 0
        self.z = 0
    
    def draw_room_front_wall(self):
        glColor3f(1, 0, 0)
        
        glBegin(GL_QUADS)
        glVertex3f(self.x,      self.y,      self.z)
        glVertex3f(self.x,      self.y + 40, self.z)
        glVertex3f(self.x + 10, self.y + 40, self.z)
        glVertex3f(self.x + 10, self.y,      self.z)
        glEnd()

        glBegin(GL_QUADS)
        glVertex3f(self.x + 10, self.y + 20, self.z)
        glVertex3f(self.x + 10, self.y + 40, self.z)
        glVertex3f(self.x + 20, self.y + 40, self.z)
        glVertex3f(self.x + 20, self.y + 20, self.z)
        glEnd()

        glBegin(GL_QUADS)
        glVertex3f(self.x + 20, self.y + 40, self.z)
        glVertex3f(self.x + 20, self.y,      self.z)
        glVertex3f(self.x + 50, self.y,      self.z)
        glVertex3f(self.x + 50, self.y + 40, self.z)
        glEnd()

    def draw_room_back_wall(self):
        glColor3f(1, 0, 1)

        glBegin(GL_QUADS)
        glVertex3f(self.x,      self.y + 40, self.z - 50)
        glVertex3f(self.x,      self.y,      self.z - 50)
        glVertex3f(self.x + 50, self.y,      self.z - 50)
        glVertex3f(self.x + 50, self.y + 40, self.z - 50)
        glEnd()

    def draw_room_left_wall(self):
        glColor3f(1, 1, 0)

        glBegin(GL_QUADS)
        glVertex3f(self.x, self.y,      self.z)
        glVertex3f(self.x, self.y,      self.z - 50)
        glVertex3f(self.x, self.y + 40, self.z - 50)
        glVertex3f(self.x, self.y + 40, self.z)
        glEnd()

    def draw_room_right_wall(self):
        glColor3f(0, 1, 1)

        glBegin(GL_QUADS)
        glVertex3f(self.x + 50, self.y,      self.z)
        glVertex3f(self.x + 50, self.y,      self.z - 50)
        glVertex3f(self.x + 50, self.y + 40, self.z - 50)
        glVertex3f(self.x + 50, self.y + 40, self.z)
        glEnd()

    def draw_room_roof(self):
        glColor3f(0, 1, 0)

        glBegin(GL_QUADS)
        glVertex3f(self.x,      self.y + 40, self.z)
        glVertex3f(self.x,      self.y + 40, self.z - 50)
        glVertex3f(self.x + 50, self.y + 40, self.z - 50)
        glVertex3f(self.x + 50, self.y + 40, self.z)
        glEnd()

    def draw_room_floor(self):
        glColor3f(0, 0, 1)

        glBegin(GL_QUADS)
        glVertex3f(self.x,      self.y, self.z)
        glVertex3f(self.x,      self.y, self.z - 50)
        glVertex3f(self.x + 50, self.y, self.z - 50)
        glVertex3f(self.x + 50, self.y, self.z)
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

