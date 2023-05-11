from OpenGL.GL import *
from math import sqrt

class Ground:

    def __init__(self, camera_x, camera_z, view_range):
        self.camera_x = camera_x
        self.camera_z = camera_z
        self.view_range = view_range
    
    def draw(self):
        glColor3f(0.3, 0.5, 0.3)

        glBegin(GL_QUADS)
        glVertex3f(self.camera_x - self.view_range, 0, self.camera_z + self.view_range*sqrt(2))
        glVertex3f(self.camera_x + self.view_range, 0, self.camera_z + self.view_range*sqrt(2))
        glVertex3f(self.camera_x + self.view_range, 0, self.camera_z - self.view_range*sqrt(2))
        glVertex3f(self.camera_x - self.view_range, 0, self.camera_z - self.view_range*sqrt(2))
        glEnd()