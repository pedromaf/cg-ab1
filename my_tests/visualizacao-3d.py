from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


fAspect = 450 / 450


def desenha():

    glClearColor(1.0, 1.0, 1.0, 1.0)

    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(0.0, 0.0, 0.0)

    glutWireCube(50)

    glFlush()


def especificaParametrosVisualizacao():
    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()

    global fAspect

    gluPerspective(60, fAspect, 0.5, 500)

    glMatrixMode(GL_MODELVIEW)

    glLoadIdentity()

    gluLookAt(40, 60, 100, 0, 0, 0, 0, 1, 0)


# programa principal
def main():

    glutInit()

    # define do modo de operação da GLUT
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

    # especifica o tamanho inicial em pixels da janela GLUT
    glutInitWindowSize(450, 450)

    # cria a janela passando como argumento o título da mesma
    glutCreateWindow("Wireframe Pirâmide 3D")

    # registra a função de callback de redesenho da janela de visualização
    glutDisplayFunc(desenha)

    # inicia o processamento e aguarda interações do usuário
    glutMainLoop()


main()
