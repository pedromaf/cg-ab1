from OpenGL.GL import *

from Window import Window

class Room:
    def __init__ (self, x, y, z, width, height, door_width, door_height, door_position_x, window:Window, num_of_windows):
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.height = height
        self.door_width = door_width
        self.door_height = door_height
        self.door_position_x = door_position_x
        self.window = window
        self.num_of_windows = num_of_windows

    
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
        hole_width = self.num_of_windows * (self.window.board_width*2 + self.window.window_width)
        hole_height = self.window.window_height + 2*self.window.board_width

        window_hole_vertices = [
            [self.window.x -hole_width/2 , self.window.y + hole_height/2, self.window.y], #upper left
            [self.window.x -hole_width/2 , self.window.y - hole_height/2, self.window.y], #bottom left
            [self.window.x +hole_width/2 , self.window.y - hole_height/2, self.window.y], #bottom right
            [self.window.x +hole_width/2 , self.window.y + hole_height/2, self.window.y] #upper right
        ]

        glBegin(GL_QUADS)

        glVertex3f(self.x,              self.y + self.height, self.z - self.width)
        glVertex3f(self.x,              self.y,               self.z - self.width)
        glVertex3f(window_hole_vertices[0][0], self.y, self.z - self.width)
        glVertex3f(window_hole_vertices[0][0], self.y + self.height, self.z - self.width)
        glEnd()


        glBegin(GL_QUADS)
        glVertex3f(window_hole_vertices[0][0],              self.y + self.height, self.z - self.width)
        glVertex3f(window_hole_vertices[0][0],  window_hole_vertices[0][1],      self.z - self.width)
        glVertex3f(window_hole_vertices[3][0], window_hole_vertices[3][1], self.z - self.width)
        glVertex3f(window_hole_vertices[3][0], self.y + self.height, self.z - self.width)
        glEnd()

        glBegin(GL_QUADS)
        glVertex3f(window_hole_vertices[1][0],  window_hole_vertices[1][1], self.z - self.width)
        glVertex3f(window_hole_vertices[1][0],  self.y,      self.z - self.width)
        glVertex3f(window_hole_vertices[2][0], self.y, self.z - self.width)
        glVertex3f(window_hole_vertices[2][0], window_hole_vertices[2][1], self.z - self.width)
        glEnd()

        glBegin(GL_QUADS)
        glVertex3f(window_hole_vertices[2][0], self.y + self.height, self.z - self.width)
        glVertex3f(window_hole_vertices[2][0], self.y,               self.z - self.width)
        glVertex3f(self.x + self.width, self.y, self.z - self.width)
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

