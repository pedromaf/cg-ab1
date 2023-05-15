from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Window:
    def __init__(self, room_x=0, room_y=0, room_z=0, room_width=1, room_height = 1, animation_speed = 4, displacement = 0):
        self.window_width = 8
        self.window_height = 12
        self.window_depth = 0.1
        self.board_width = 0.2
        self.total_width = self.board_width * 2 + self.window_width
        self.animation_speed = animation_speed
        self.x = room_x + room_width/2 + displacement * self.total_width
        self.y = room_y + room_height/2
        self.z = room_z - room_width

        self.vertices = [
            [self.x - self.window_width/2 - self.board_width, self.y + self.window_height/2, self.z], #upper left
            [self.x - self.window_width/2 - self.board_width, self.y - self.window_height/2, self.z], #bottom left
            [self.x - self.window_width/2 + self.board_width, self.y - self.window_height/2, self.z], #bottom right
            [self.x - self.window_width/2 + self.board_width, self.y + self.window_height/2, self.z] #upper right
        ]

        self.is_open = False
        self.is_opening = False
        self.is_closing = False
        self.rotation_angle = 0

    def draw_cube(self, vertices):
        glBegin(GL_QUADS)
        glColor3f(0.5, 0.5, 0.5)
        # front face
        for vertex in vertices:
            glVertex3f(*vertex)
        
        #left face
        glVertex3f(*vertices[0])
        glVertex3f(*vertices[1])
        glVertex3f(vertices[2][0], vertices[2][1], vertices[2][2]-self.window_depth)
        glVertex3f(vertices[3][0], vertices[3][1], vertices[3][2]-self.window_depth)

        #upper face
        glVertex3f(vertices[0][0], vertices[0][1], vertices[0][2] - self.window_depth)
        glVertex3f(*vertices[1])
        glVertex3f(*vertices[2])
        glVertex3f(vertices[3][0], vertices[3][1], vertices[3][2] - self.window_depth)

        #right face
        glVertex3f(vertices[0][0], vertices[0][1], vertices[0][2] - self.window_depth)
        glVertex3f(vertices[1][0], vertices[1][1], vertices[1][2] - self.window_depth)
        glVertex3f(*vertices[2])
        glVertex3f(*vertices[3])


        # back face
        for vertex in vertices:
            glVertex3f(vertex[0], vertex[1], vertex[2] - self.window_depth)    
        

        #bottom face
        glVertex3f(*vertices[0])
        glVertex3f(vertices[1][0], vertices[1][1], vertices[1][2] - self.window_depth)
        glVertex3f(vertices[2][0], vertices[2][1], vertices[2][2] - self.window_depth)
        glVertex3f(*vertices[3])

        glEnd()


    
    def __drawVerticalBoardPieces(self):

        self.draw_cube(self.vertices)
        glPushMatrix()
        glTranslate(self.window_width,0, 0)
        self.draw_cube(self.vertices)
        glPopMatrix()
        glPushMatrix()
        glTranslate(self.window_width/2,0, 0)
        self.draw_cube(self.vertices)
        glPopMatrix()



    def __drawHorizontalBoardPieces(self):
        
        glPushMatrix() #borda inferior
        glTranslate(self.x, self.y, self.z)  # move o objeto para o centro de sua posição
        glRotate(90, 0, 0, 1)  # rotaciona o objeto em torno do eixo y
        glScale(1, (self.window_width+2*self.board_width)/self.window_height, 1) # escala a borda da moldura para a largura da janela
        glTranslate(-self.x - 9*self.board_width, -self.y, -self.z)  # move o objeto de volta à sua posição original
     
        self.draw_cube(self.vertices)
        glPopMatrix()

        glPushMatrix() #borda superior
        glTranslate(self.x, self.y, self.z)  # move o objeto para o centro de sua posição
        glRotate(90, 0, 0, 1)  # rotaciona o objeto em torno do eixo y
        glScale(1, (self.window_width+2*self.board_width)/self.window_height, 1)
        glTranslate(-self.x - 9*self.board_width + self.window_height, -self.y, -self.z)  # move o objeto de volta à sua posição original
        
        self.draw_cube(self.vertices)
        glPopMatrix()

        glPushMatrix() #borda do meio
        glTranslate(self.x, self.y, self.z)  # move o objeto para o centro de sua posição
        glRotate(90, 0, 0, 1)  # rotaciona o objeto em torno do eixo y
        glScale(1, (self.window_width+2*self.board_width)/self.window_height, 1)
        glTranslate(-self.x - 9*self.board_width + self.window_height/2, -self.y, -self.z)  # move o objeto de volta à sua posição original
        self.draw_cube(self.vertices)
        glPopMatrix()
    

   
    def draw(self):
        if (self.is_opening and self.rotation_angle >= 90):
            self.is_opening = False
            self.is_open = True
        elif (self.is_opening and self.rotation_angle < 90):
            self.__rotate()
            self.rotation_angle += (0.1 * self.animation_speed)
        elif (self.is_closing and self.rotation_angle <= 0):
            self.is_closing = False
            self.is_open = False
        elif (self.is_closing and self.rotation_angle > 0):
            self.__rotate()
            self.rotation_angle -= 0.1 * self.animation_speed
        elif (self.is_open):
            self.__rotate()
        else:
            self.__draw_closed__window()


    def __draw_closed__window(self):
        self.__drawVerticalBoardPieces()
        self.__drawHorizontalBoardPieces()

     
    # def open(self):
    #     glPushMatrix()  # salva a matriz de modelo atual
    #     glTranslate(self.x, self.y, self.z)  # move o objeto para o centro de sua posição
    #     glRotate(90, 0, 1, 0)  # rotaciona o objeto em torno do eixo y
    #     glTranslate(-self.x, -self.y, -self.z)
    #     self.__drawVerticalBoardPieces()
    #     self.__drawHorizontalBoardPieces()  # move o objeto de volta à sua posição original
    #     glPopMatrix()  # restaura a matriz de modelo original


    def __rotate(self):
        glPushMatrix()
        glTranslate(self.x, self.y, self.z)
        glRotatef(self.rotation_angle, 0, 1, 0)
        glTranslate(-self.x, -self.y, -self.z)
        self.__draw_closed__window()
        glPopMatrix()


    def trigger_animation(self):
        if self.is_open or self.is_opening:
            self.is_closing = True
            self.is_opening = False
        else:
            self.is_opening = True
            self.is_closing = False    




    
