from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_POSITION_X = 200
WINDOW_POSITION_Y = 100

is_fullscreen = False
current_window_width = WINDOW_WIDTH
current_window_height = WINDOW_HEIGHT
f_aspect = current_window_width/current_window_height

def display():
    glClearColor(0, 0, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glEnable(GL_DEPTH_TEST)

    set_visualization()

    # begin draw code

    glutWireCube(50)
    
    # end draw code

    glutSwapBuffers()

def set_visualization():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    
    gluPerspective(60, f_aspect, 0.5, 500)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt(40, 60, 100, 0, 0, 0, 0, 1, 0)

def idle_display():
    glutPostRedisplay()

def keyboard_handler(key, mouse_x, mouse_y):
    global is_fullscreen

    if key == b'o' or b'O':
        if is_fullscreen:
            glutReshapeWindow(WINDOW_WIDTH, WINDOW_HEIGHT)
            glutPositionWindow(WINDOW_POSITION_X, WINDOW_POSITION_Y)
        else:
            glutFullScreen()
        
        is_fullscreen = not is_fullscreen

def reshape(width, height):
    global current_window_width, current_window_height, f_aspect

    current_window_height = height
    current_window_width = width
    f_aspect = width/height

    glViewport(0, 0, width, height)

def main():
    glutInit()
    
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(WINDOW_POSITION_X, WINDOW_POSITION_Y)
    glutCreateWindow("Hello World")

    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard_handler)
    glutIdleFunc(idle_display)
    glutReshapeFunc(reshape)
    
    glutMainLoop()

if __name__ == "__main__":
    main()