from OpenGL.GL import *
from OpenGL.GLUT import *
from math import sin, cos, pi

height = 0.3
radius = 1.0
segments = 32
base_radius = radius + 0.5

class CeilingLamp:
    def __init__(self, x, y, z, room_height, room_width) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.final_position_x = x + room_width/2
        self.final_position_y = y + room_height
        self.final_position_z = z - room_width/2

    def __draw_base(self):
        num_slices = 20

        glBegin(GL_TRIANGLE_STRIP)
        for i in range(num_slices + 1):
            angle = 2.0 * pi * i / num_slices
            x = base_radius * cos(angle)
            y = base_radius * sin(angle)

            glVertex3f(x, y, 0.0)
            glVertex3f(x, y, height)
        glEnd()

        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(0.0, 0.0, height)
        for i in range(num_slices + 1):
            angle = 2.0 * pi * i / num_slices
            x = base_radius * cos(angle)
            y = base_radius * sin(angle)

            glVertex3f(x, y, height)
        glEnd()

    def __draw_bowl(self):
        stacks = 15
        slices = 25

        for i in range(stacks//2):
            lat0 = pi * (-0.5 + float(i - 1) / float(stacks - 1))
            z0 = sin(lat0) * radius
            zr0 = cos(lat0) * radius

            lat1 = pi * (-0.5 + float(i) / float(stacks - 1))
            z1 = sin(lat1) * radius
            zr1 = cos(lat1) * radius

            glBegin(GL_TRIANGLE_STRIP)
            glColor4f(1.0,1.0,1.0, 0.7)

            for j in range(slices, -1, -1):
                lng = 2 * pi * float(j - 1) / float(slices)
                x = cos(lng)
                y = sin(lng)

                glNormal3f(self.x, 0, self.z)
                glVertex3f(x * zr0, y * zr0, z0)

                glNormal3f(self.x, 0, self.z)
                glVertex3f(x * zr1, y * zr1, z1)
            glEnd()

    def draw(self):
        glPushMatrix()
        
        glTranslate(self.final_position_x, self.final_position_y, self.final_position_z)
        glRotatef(90, 1, 0, 0)

        glColor3f(0.5, 0.4, 0.4)

        self.__draw_base()

        glPopMatrix()

        glPushMatrix()

        glTranslate(self.final_position_x, self.final_position_y, self.final_position_z)
        glRotatef(-90, 1, 0, 0)

        self.__draw_bowl()

        glPopMatrix()
        
  



