from OpenGL.GL import *
from math import sqrt
from texture_handler import load_texture

class Ground:

    def __init__(self, camera_x, camera_z, view_range):
        self.camera_x = camera_x
        self.camera_z = camera_z
        self.view_range = view_range * 1.5
        self.texture_id = None
    
    def draw(self):
        texture_size = 450
        
        if self.texture_id == None:
            self.texture_id = load_texture("textures/ground.jpg")

        glColor3f(0.3, 0.3, 0.3)

        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.texture_id)

        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(self.camera_x - self.view_range, 0, self.camera_z + self.view_range*sqrt(2))

        glTexCoord2f(texture_size, 0)
        glVertex3f(self.camera_x + self.view_range, 0, self.camera_z + self.view_range*sqrt(2))

        glTexCoord2f(texture_size, texture_size)
        glVertex3f(self.camera_x + self.view_range, 0, self.camera_z - self.view_range*sqrt(2))

        glTexCoord2f(0, texture_size)
        glVertex3f(self.camera_x - self.view_range, 0, self.camera_z - self.view_range*sqrt(2))
        glEnd()

        glDisable(GL_TEXTURE_2D)