from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from typing import List

rotX = 0.0
rotY = 0.0
rotX_ini = 0.0
rotY_ini = 0.0
obsX = 0.0
obsY = 0.0
obsZ = 0.0
obsX_ini = 0.0
obsY_ini = 0.0
obsZ_ini = 0.0
angle = 0.0
fAspec = 0.0
x_ini = 0.0
y_ini = 0.0
bot = 0.0


class Vertice:

    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z


class Face:

    def __init__(self, totalDeVertices: int, v1: int, v2: int, v3: int, v4: int):
        self.totalDeVertices = totalDeVertices
        self.face = [v1, v2, v3, v4]


class Objeto:

    def __init__(self, vertices: List[Vertice], faces: List[Face], totalDeFaces: int):
        self.vertices = vertices
        self.faces = faces
        self.totalDeFaces = totalDeFaces


vertices = [
    Vertice(-1.0, 0.0, -1.0),  # 0
    Vertice(1.0, 0.0, -1.0),  # 1
    Vertice(1.0, 0.0, 1.0),   # 2
    Vertice(-1.0, 0.0, 1.0),  # 3
    Vertice(0.0, 2.0, 0.0),   # 4
]

faces = [
    Face(4, 0, 1, 2, 3),
    Face(3, 0, 1, 4, -1),
    Face(3, 0, 3, 4, -1),
    Face(3, 1, 2, 4, -1),
    Face(3, 3, 2, 4, -1),
]

piramide = Objeto(vertices, faces, 5)


# Desenha um objeto em Wireframe
def desenhaObjetoWireFrame(objeto: Objeto):

    for face in objeto.faces:
        glBegin(GL_LINE_LOOP)
        for v in face.face:
            if v != -1:
                glVertex3f(
                    objeto.vertices[v].x,
                    objeto.vertices[v].y,
                    objeto.vertices[v].z,
                )
        glEnd()


# Função de callback de redesenho da janela de visualização
def desenha():

    glClearColor(1.0, 1.0, 1.0, 0.0)

    # limpa a janela de visualização com a cor de fundo definida previamente
    glClear(GL_COLOR_BUFFER_BIT)

    # altera a cor do desenho para preto
    glColor3f(0.5, 0.5, 0.5)

    # desenha o objeto definido anteriormente: uma pirâmide
    # desenhaObjetoWireFrame(piramide)

    # glutWireCube(1)
    glut

    # executa o comando OpenGL
    glFlush()


# funcao usada para especificar a posição do observador virtual
def posicionaObservador():
    # especifica o sistema de coordenadas do modelo
    glMatrixMode(GL_MODELVIEW)

    # inicializa o sistema de coordenadas do modelo
    glLoadIdentity()

    # posiciona e orienta o observador
    glTranslatef(-obsX, -obsY, -obsZ)
    glRotatef(rotX, 1.0, 0.0, 0.0)
    glRotatef(rotY, 0.0, 1.0, 0.0)


# função usada para especificar o volume de visualização
def especificaParametrosVisualizacao():
    # especifica sistema de coordenadas de projecao
    glMatrixMode(GL_PROJECTION)

    # inicializa sistema de coordenadas de projeção
    glLoadIdentity()

    # especifica a projeção perspectiva (angulo, aspecto, zMin, zMax)
    gluPerspective(angle, fAspec, 0.1, 1200.0)

    posicionaObservador()


def alteraTamanhoJanela(w: GLsizei, h: GLsizei):
    # para previnir uma divisão por zero
    if h == 0:
        h = 1

    # especifica as dimensões da viewport
    glViewport(0, 0, w, h)

    # calcula a correção de aspecto
    global fAspec
    fAspec = w / h

    especificaParametrosVisualizacao()


# função de callback para eventos de botões do mouse
def gerenciaMouse(button: int, state: int, x: int, y: int):
    global x_ini, y_ini, obsX_ini, obsY_ini, obsZ_ini, rotX_ini, rotY_ini, bot
    if state == GLUT_DOWN:
        # salva os parametros atuais
        x_ini = x
        y_ini = y
        obsX_ini = obsX
        obsY_ini = obsY
        obsZ_ini = obsZ
        rotX_ini = rotX
        rotY_ini = rotY
        bot = button
    else:
        bot = -1


SENS_ROT = 5.0
SENS_OBS = 15.0
SENS_TRANSL = 30.0


# função de callback para eventos de movimento do mouse
def gerenciaMovimento(x: int, y: int):
    global rotX, rotY, obsZ, obsX, obsY
    # botao esquerdo
    if bot == GLUT_LEFT_BUTTON:
        # calcula as diferenças
        deltaX = x_ini - x
        deltaY = y_ini - y

        # modifica ângulos
        rotY = rotY_ini - deltaX/SENS_ROT
        rotX = rotX_ini - deltaY/SENS_ROT

    # botao direito
    elif bot == GLUT_RIGHT_BUTTON:
        # calcula a diferença
        deltaZ = y_ini - y

        # modifica distância do observador
        obsZ = obsZ_ini + deltaZ / SENS_OBS

    # botao do meio
    elif bot == GLUT_MIDDLE_BUTTON:
        # calcula diferenças
        deltaX = x_ini - x
        deltaY = y_ini - y

        # modifica posições
        obsX = obsX_ini + deltaX / SENS_TRANSL
        obsY = obsY_ini - deltaY / SENS_TRANSL

    posicionaObservador()
    glutPostRedisplay()


# função callback chamada para gerenciar eventos de teclas normais (ESC)
def teclado(tecla: int, x: int, y: int):
    if tecla == 27:
        exit(0)


# função de callback para tratar eventos de teclas especiais
def teclasEspeciais(tecla: int, x: int, y: int):
    global angle
    if tecla == GLUT_KEY_HOME:
        if angle >= 10.0:
            angle -= 5.0
    elif tecla == GLUT_KEY_END:
        if angle <= 150:
            angle += 5.0
    elif tecla == 27:
        exit(0)

    especificaParametrosVisualizacao()
    glutPostRedisplay()


# função responsável por inicializar parâmetros e variáveis
def init():
    # define a cor de fundo da janela de visualização como branca
    glClearColor(1.0, 1.0, 1.0, 1.0)

    # inicializa a variavel que especifica o ângulo de projeção / perspectiva
    global angle
    angle = 54

    # inicializa as variáveis usadas para alterar a posição do observador virtual
    global rotX, rotY, obsX, obsY, obsZ
    rotX = 0
    rotY = 0
    obsX = 0
    obsY = 0
    obsZ = 10


# programa principal
def main():

    glutInit()

    # define do modo de operação da GLUT
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

    # especifica a posição inicial da janela GLUT
    glutInitWindowPosition(5, 5)

    # especifica o tamanho inicial em pixels da janela GLUT
    glutInitWindowSize(450, 450)

    # cria a janela passando como argumento o título da mesma
    glutCreateWindow("Wireframe Pirâmide 3D")

    # registra a função de callback de redesenho da janela de visualização
    glutDisplayFunc(desenha)

    # registra a função de callback de redimensionamento da janela de visualização
    glutReshapeFunc(alteraTamanhoJanela)

    # registra a função de callback para tratamento das teclas normais
    glutKeyboardFunc(teclado)

    # registra a função de callback de tratamento das teclas especiais
    glutSpecialFunc(teclasEspeciais)

    # registra a função de callback para eventos de botoes do mouse
    glutMouseFunc(gerenciaMouse)

    # registra a função de callback para eventos de movimento do mouse
    glutMotionFunc(gerenciaMovimento)

    # chama a função responsável por fazer as inicializações
    init()

    # inicia o processamento e aguarda interações do usuário
    glutMainLoop()


main()
