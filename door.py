from OpenGL.GL import *

class Door:
    def __init__(self, x, y, z, width, height):
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.height = height
    
    def draw(self):
        glColor3f(0.5, 0.3, 0.8)
        glBegin(GL_QUADS)
        glVertex3f(self.x,              self.y, self.z)
        glVertex3f(self.x + self.width, self.y, self.z)
        glVertex3f(self.x + self.width, self.y + self.height, self.z)
        glVertex3f(self.x,              self.y + self.height, self.z)
        glEnd()

    def rotate(self, angle):
        glPushMatrix()
        glTranslate(self.x, self.y, self.z)
        glRotatef(angle, 0, 1, 0)
        glTranslate(-self.x, -self.y, -self.z)
        self.draw()
        glPopMatrix()