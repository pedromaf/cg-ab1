from OpenGL.GL import *
from math import sin, cos, pi
from texture_handler import load_texture

width = 2.0
radius = width * 0.3

class TableLamp:    
    #x and y refers to the center point of the base's bottom face
    def __init__(self, x, y, z, height, angle):
        self.x = x
        self.y = y
        self.z = z
        self.angle = angle
        self.base_height = height * 0.05
        self.vert_pole_height = height * 0.95
        self.base_width = width
        self.pole_width = width*0.05
        self.hori_pole_length = width
        self.book_texture_id = None


    def __draw_book(self):
        if self.book_texture_id == None:
            self.book_texture_id = load_texture("textures/book.jpeg")
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.book_texture_id)    
        
        glColor3f(1.0,1.0,1.0)
        
        #left
        glNormal3f(0, 1, 0)
        
        glBegin(GL_QUADS)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 1.0, 0.0)
        glVertex3f(1.0, 1.0, 0.0)
        glVertex3f(1.0, 0.0, 0.0)
        glEnd()
        

        #right
        glNormal3f(1, 1, 0)
        glBegin(GL_QUADS)
        glVertex3f(0.0, 0.0, -1.0)
        glVertex3f(0.0, 1.0, -1.0)
        glVertex3f(1.0, 1.0, -1.0)
        glVertex3f(1.0, 0.0, -1.0)
        glEnd()


        #left
        glNormal3f(1, 1, 0)
        glBegin(GL_QUADS)
        glTexCoord2f(0,0)
        glVertex3f(0.0, 0.0, 0.0)
        glTexCoord2f(1,0)
        glVertex3f(0.0, 1.0, 0.0)
        glTexCoord2f(1,1)
        glVertex3f(0.0, 1.0, -1.0)
        glTexCoord2f(0,1)
        glVertex3f(0.0, 0.0, -1.0)
        glEnd()

        glDisable(GL_TEXTURE_2D)

        #right
        glBegin(GL_QUADS)
        glVertex3f(1.0, 0.0, 0.0)
        glVertex3f(1.0, 1.0, 0.0)
        glVertex3f(1.0, 1.0, -1.0)
        glVertex3f(1.0, 0.0, -1.0)
        glEnd()

        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.book_texture_id)  
        #top
        glNormal3f(0, 1, 0)
        glBegin(GL_QUADS)
        glTexCoord2f(1,1)
        glVertex3f(0.0, 1.0, 0.0)
        glTexCoord2f(0,1)
        glVertex3f(0.0, 1.0, -1.0)
        glTexCoord2f(0,0)
        glVertex3f(1.0, 1.0, -1.0)
        glTexCoord2f(1,0)
        glVertex3f(1.0, 1.0, 0.0)
        glEnd()
        glDisable(GL_TEXTURE_2D)

        #bottom
        glNormal3f(0, -1, 0)
        glBegin(GL_QUADS)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, -1.0)
        glVertex3f(1.0, 0.0, -1.0)
        glVertex3f(1.0, 0.0, 0.0)
        glEnd()




    def __draw_pole(self):
        glColor3f(1.0,1.0,1.0)

        #front
        glNormal3f(0, 1, 0)
        glBegin(GL_QUADS)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 1.0, 0.0)
        glVertex3f(1.0, 1.0, 0.0)
        glVertex3f(1.0, 0.0, 0.0)
        glEnd()
        
        #back
        glNormal3f(0, 0, -1)
        glBegin(GL_QUADS)
        glVertex3f(0.0, 0.0, -1.0)
        glVertex3f(0.0, 1.0, -1.0)
        glVertex3f(1.0, 1.0, -1.0)
        glVertex3f(1.0, 0.0, -1.0)
        glEnd()

        #left
        glNormal3f(0, 0, -1)
        glBegin(GL_QUADS)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 1.0, 0.0)
        glVertex3f(0.0, 1.0, -1.0)
        glVertex3f(0.0, 0.0, -1.0)
        glEnd()

        #right
        glBegin(GL_QUADS)
        glVertex3f(1.0, 0.0, 0.0)
        glVertex3f(1.0, 1.0, 0.0)
        glVertex3f(1.0, 1.0, -1.0)
        glVertex3f(1.0, 0.0, -1.0)
        glEnd()

        #top
        glNormal3f(0, 1, 0)
        glBegin(GL_QUADS)
        glVertex3f(0.0, 1.0, 0.0)
        glVertex3f(0.0, 1.0, -1.0)
        glVertex3f(1.0, 1.0, -1.0)
        glVertex3f(1.0, 1.0, 0.0)
        glEnd()

        #bottom
        glNormal3f(0, -1, 0)
        glBegin(GL_QUADS)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, -1.0)
        glVertex3f(1.0, 0.0, -1.0)
        glVertex3f(1.0, 0.0, 0.0)
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
            glColor4f(1.0,1.0,1.0, 0.8)
            for j in range(slices, -1, -1):
                lng = 2 * pi * float(j - 1) / float(slices)
                x = cos(lng)
                y = sin(lng)

                glNormal3f(x * zr0, y * zr0, z0)
                glVertex3f(x * zr0, y * zr0, z0)

                glNormal3f(x * zr1, y * zr1, z1)
                glVertex3f(x * zr1, y * zr1, z1)
            glEnd()
    
    def __draw(self):
        glPushMatrix()
        glTranslatef(0, 0, 0)
        glScalef(self.pole_width, self.vert_pole_height, self.pole_width)
        self.__draw_pole()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0, self.vert_pole_height, 0)
        glScalef(self.hori_pole_length, self.pole_width, self.pole_width)
        self.__draw_pole()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(self.hori_pole_length,self.vert_pole_height, self.base_width/2)
        glScalef(0.4, self.pole_width, self.base_width)
        self.__draw_pole()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(self.hori_pole_length + self.base_width/2, self.vert_pole_height + self.pole_width, 0)
        glRotatef(-90, 1, 0, 0)
        self.__draw_bowl()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(self.hori_pole_length, self.vert_pole_height,self.base_width/2)
        glScalef(self.base_width, self.pole_width, self.base_width)
        self.__draw_pole()
        glPopMatrix()

        #base
        glPushMatrix()
        glTranslatef(-(self.base_width/2), 0, self.base_width/2)
        glScalef(self.base_width, self.pole_width, self.base_width)
        self.__draw_pole()
        glPopMatrix()


        glPushMatrix()
        glTranslatef(self.base_width, 0, self.base_width - 2)
        glScalef(2, 0.5, 3)


        self.__draw_book()
        glPopMatrix()

        
        
    def draw(self):
        glPushMatrix()
        glTranslate(self.x + self.base_width/2, self.y + self.pole_width/2, self.z + self.base_width/2)
        glRotatef(self.angle, 0, 1, 0)
        self.__draw()
        glPopMatrix()
