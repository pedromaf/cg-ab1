from OpenGL.GL import *
from texture_handler import load_texture

from window import Window

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
        self.wall_texture_id = None
        self.roof_texture_id = None
        self.floor_texture_id = None

    
    def draw_room_front_wall(self):
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(self.x,                        self.y,               self.z)
        glTexCoord2f(6, 0)
        glVertex3f(self.x,                        self.y + self.height, self.z)
        glTexCoord2f(6, 1.5)
        glVertex3f(self.x + self.door_position_x, self.y + self.height, self.z)
        glTexCoord2f(0, 1.5)
        glVertex3f(self.x + self.door_position_x, self.y,               self.z)
        glEnd()

        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(self.x + self.door_position_x,                   self.y + self.door_height, self.z)
        glTexCoord2f(3, 0)
        glVertex3f(self.x + self.door_position_x,                   self.y + self.height,      self.z)
        glTexCoord2f(3, 1.5)
        glVertex3f(self.x + self.door_position_x + self.door_width, self.y + self.height,      self.z)
        glTexCoord2f(0, 1.5)
        glVertex3f(self.x + self.door_position_x + self.door_width, self.y + self.door_height, self.z)
        glEnd()

        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(self.x + self.door_position_x + self.door_width, self.y + self.height, self.z)
        glTexCoord2f(6, 0)
        glVertex3f(self.x + self.door_position_x + self.door_width, self.y,               self.z)
        glTexCoord2f(6, 6)
        glVertex3f(self.x + self.width,                             self.y,               self.z)
        glTexCoord2f(0, 6)
        glVertex3f(self.x + self.width,                             self.y + self.height, self.z)
        glEnd()

    def draw_room_back_wall(self):
        hole_width = self.num_of_windows * (self.window.board_width*2 + self.window.window_width)
        hole_height = self.window.window_height + 2*self.window.board_width

        window_hole_vertices = [
            [self.window.x -hole_width/2 , self.window.y + hole_height/2, self.window.y], #upper left
            [self.window.x -hole_width/2 , self.window.y - hole_height/2, self.window.y], #bottom left
            [self.window.x +hole_width/2 , self.window.y - hole_height/2, self.window.y], #bottom right
            [self.window.x +hole_width/2 , self.window.y + hole_height/2, self.window.y]  #upper right
        ]

        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(self.x,              self.y + self.height, self.z - self.width)
        glTexCoord2f(6, 0)
        glVertex3f(self.x,              self.y,               self.z - self.width)
        glTexCoord2f(6, 3)
        glVertex3f(window_hole_vertices[0][0], self.y, self.z - self.width)
        glTexCoord2f(0, 3)
        glVertex3f(window_hole_vertices[0][0], self.y + self.height, self.z - self.width)
        glEnd()


        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(window_hole_vertices[0][0],              self.y + self.height, self.z - self.width)
        glTexCoord2f(2, 0)
        glVertex3f(window_hole_vertices[0][0],  window_hole_vertices[0][1],      self.z - self.width)
        glTexCoord2f(2, 4)
        glVertex3f(window_hole_vertices[3][0], window_hole_vertices[3][1], self.z - self.width)
        glTexCoord2f(0, 4)
        glVertex3f(window_hole_vertices[3][0], self.y + self.height, self.z - self.width)
        glEnd()

        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(window_hole_vertices[1][0],  window_hole_vertices[1][1], self.z - self.width)
        glTexCoord2f(2, 0)
        glVertex3f(window_hole_vertices[1][0],  self.y,      self.z - self.width)
        glTexCoord2f(2, 4)
        glVertex3f(window_hole_vertices[2][0], self.y, self.z - self.width)
        glTexCoord2f(0, 4)
        glVertex3f(window_hole_vertices[2][0], window_hole_vertices[2][1], self.z - self.width)
        glEnd()

        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(window_hole_vertices[2][0], self.y + self.height, self.z - self.width)
        glTexCoord2f(6, 0)
        glVertex3f(window_hole_vertices[2][0], self.y,               self.z - self.width)
        glTexCoord2f(6, 3)
        glVertex3f(self.x + self.width, self.y, self.z - self.width)
        glTexCoord2f(0, 3)
        glVertex3f(self.x + self.width, self.y + self.height, self.z - self.width)
        glEnd()

    def draw_room_left_wall(self):
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(self.x, self.y,               self.z)
        glTexCoord2f(12, 0)
        glVertex3f(self.x, self.y,               self.z - self.width)
        glTexCoord2f(12, 9)
        glVertex3f(self.x, self.y + self.height, self.z - self.width)
        glTexCoord2f(0, 9)
        glVertex3f(self.x, self.y + self.height, self.z)
        glEnd()

    def draw_room_right_wall(self):
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(self.x + self.width, self.y,               self.z)
        glTexCoord2f(12, 0)
        glVertex3f(self.x + self.width, self.y,               self.z - self.width)
        glTexCoord2f(12, 9)
        glVertex3f(self.x + self.width, self.y + self.height, self.z - self.width)
        glTexCoord2f(0, 9)
        glVertex3f(self.x + self.width, self.y + self.height, self.z)
        glEnd()

    def draw_room_roof(self):
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(self.x,              self.y + self.height, self.z)
        glTexCoord2f(3, 0)
        glVertex3f(self.x,              self.y + self.height, self.z - self.width)
        glTexCoord2f(3, 3)
        glVertex3f(self.x + self.width, self.y + self.height, self.z - self.width)
        glTexCoord2f(0, 3)
        glVertex3f(self.x + self.width, self.y + self.height, self.z)
        glEnd()

    def draw_room_floor(self):
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(self.x,              self.y, self.z)
        glTexCoord2f(12, 0)
        glVertex3f(self.x,              self.y, self.z - self.width)
        glTexCoord2f(12, 9)
        glVertex3f(self.x + self.width, self.y, self.z - self.width)
        glTexCoord2f(0, 9)
        glVertex3f(self.x + self.width, self.y, self.z)
        glEnd()

    def draw(self):
        if self.wall_texture_id == None:
            self.wall_texture_id = load_texture("textures/wall.jpg")
        
        if self.roof_texture_id == None:
            self.roof_texture_id = load_texture("textures/roof.jpg")

        if self.floor_texture_id == None:
            self.floor_texture_id = load_texture("textures/floor.jpg")

        glColor3f(1, 1, 1)

        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.wall_texture_id)

        self.draw_room_front_wall()
        self.draw_room_back_wall()
        self.draw_room_left_wall()
        self.draw_room_right_wall()

        glBindTexture(GL_TEXTURE_2D, self.roof_texture_id)

        self.draw_room_roof()

        glBindTexture(GL_TEXTURE_2D, self.floor_texture_id)

        self.draw_room_floor()

        glDisable(GL_TEXTURE_2D)


