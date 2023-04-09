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

camera_x = 0
camera_y = 0
camera_z = 100
camera_movement_velocity = 2
camera_rotation_velocity = 0.4

focal_point_x = 0
focal_point_y = 0
focal_point_z = 0

previous_mouse_x = None
previous_mouse_y = None

def draw_room_front_wall():
    glColor3f(1, 0, 0)
    
    glBegin(GL_QUADS)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 40, 0)
    glVertex3f(10, 40, 0)
    glVertex3f(10, 0, 0)
    glEnd()

    glBegin(GL_QUADS)
    glVertex3f(10, 20, 0)
    glVertex3f(10, 40, 0)
    glVertex3f(20, 40, 0)
    glVertex3f(20, 20, 0)
    glEnd()

    glBegin(GL_QUADS)
    glVertex3f(20, 40, 0)
    glVertex3f(20, 0, 0)
    glVertex3f(50, 0, 0)
    glVertex3f(50, 40, 0)
    glEnd()

def draw_room_back_wall():
    glColor3f(1, 0, 1)

    glBegin(GL_QUADS)
    glVertex3f(0, 40, -50)
    glVertex3f(0, 0, -50)
    glVertex3f(50, 0, -50)
    glVertex3f(50, 40, -50)
    glEnd()

def draw_room_left_wall():
    glColor3f(1, 1, 0)

    glBegin(GL_QUADS)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, -50)
    glVertex3f(0, 40, -50)
    glVertex3f(0, 40, 0)
    glEnd()

def draw_room_right_wall():
    glColor3f(0, 1, 1)

    glBegin(GL_QUADS)
    glVertex3f(50, 0, 0)
    glVertex3f(50, 0, -50)
    glVertex3f(50, 40, -50)
    glVertex3f(50, 40, 0)
    glEnd()

def draw_room_roof():
    glColor3f(0, 1, 0)

    glBegin(GL_QUADS)
    glVertex3f(0, 40, 0)
    glVertex3f(0, 40, -50)
    glVertex3f(50, 40, -50)
    glVertex3f(50, 40, 0)
    glEnd()

def draw_room_floor():
    glColor3f(0, 0, 1)

    glBegin(GL_QUADS)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, -50)
    glVertex3f(50, 0, -50)
    glVertex3f(50, 0, 0)
    glEnd()

def draw_room():
    draw_room_front_wall()
    draw_room_back_wall()
    draw_room_left_wall()
    draw_room_right_wall()
    draw_room_roof()
    draw_room_floor()


def display():
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glEnable(GL_DEPTH_TEST)
    glEnableClientState(GL_VERTEX_ARRAY)

    set_visualization()

    # begin draw code

    draw_room()
    
    # end draw code

    glutSwapBuffers()

def set_visualization():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(60, f_aspect, 0.5, 500)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt(camera_x, camera_y, camera_z, focal_point_x, focal_point_y, focal_point_z, 0, 1, 0)

def idle_display():
    glutPostRedisplay()

def screen_handler():
    global is_fullscreen
        
    if is_fullscreen:
        glutReshapeWindow(WINDOW_WIDTH, WINDOW_HEIGHT)
        glutPositionWindow(WINDOW_POSITION_X, WINDOW_POSITION_Y)
    else:
        glutFullScreen()
    
    is_fullscreen = not is_fullscreen

def move_camera_foward():
    global camera_x, camera_y, camera_z
    global focal_point_x, focal_point_y, focal_point_z

    if focal_point_x > 0:
        camera_x += camera_movement_velocity
        focal_point_x += camera_movement_velocity
    else:
        camera_x -= camera_movement_velocity
        focal_point_x -= camera_movement_velocity

    if focal_point_y > 0:  
        camera_y += camera_movement_velocity
        focal_point_y += camera_movement_velocity
    else:
        camera_y -= camera_movement_velocity
        focal_point_y -= camera_movement_velocity

    camera_z -= camera_movement_velocity
    focal_point_z -= camera_movement_velocity

def move_camera_backward():
    global camera_x, camera_y, camera_z
    global focal_point_x, focal_point_y, focal_point_z

    if focal_point_x > 0:
        camera_x -= camera_movement_velocity
        focal_point_x -= camera_movement_velocity
    else:
        camera_x += camera_movement_velocity
        focal_point_x += camera_movement_velocity

    if focal_point_y > 0:  
        camera_y -= camera_movement_velocity
        focal_point_y -= camera_movement_velocity
    else:
        camera_y += camera_movement_velocity
        focal_point_y += camera_movement_velocity

    camera_z += camera_movement_velocity
    focal_point_z += camera_movement_velocity

def keyboard_handler(key, mouse_x, mouse_y):
    global camera_x, camera_y, camera_z
    global focal_point_x, focal_point_y, focal_point_z

    if key == b'\x1b':
        glutDestroyWindow(glutGetWindow())
    elif key == b'o' or key == b'O':
        screen_handler()
    elif key == b'a' or key == b'A':
        camera_x -= camera_movement_velocity
        focal_point_x -= camera_movement_velocity
    elif key == b'd' or key == b'D':
        camera_x += camera_movement_velocity
        focal_point_x += camera_movement_velocity
    elif key == b'w' or key == b'W':
        move_camera_foward()
    elif key == b's' or key == b'S':
        move_camera_backward()

def reshape(width, height):
    global current_window_width, current_window_height, f_aspect

    current_window_height = height
    current_window_width = width
    f_aspect = width/height

    glViewport(0, 0, width, height)

def mouse_motion_handler(mouse_x, mouse_y):
    global previous_mouse_x, previous_mouse_y
    global focal_point_x, focal_point_y

    window_center_x = int(glutGet(GLUT_WINDOW_WIDTH)/2)
    window_center_y = int(glutGet(GLUT_WINDOW_HEIGHT)/2)

    cursor_cage_dx = window_center_x*0.5
    cursor_cage_dy = window_center_y*0.5


    if mouse_x > window_center_x + cursor_cage_dx or mouse_x < window_center_x - cursor_cage_dx:
        glutWarpPointer(window_center_x, window_center_y)

    if mouse_y > window_center_y + cursor_cage_dy or mouse_y < window_center_y - cursor_cage_dy:
        glutWarpPointer(window_center_x, window_center_y)

    if previous_mouse_x == None or previous_mouse_y == None:
        previous_mouse_x = mouse_x
        previous_mouse_y = mouse_y
    
    if previous_mouse_x <= mouse_x:
        focal_point_x += camera_rotation_velocity

    if previous_mouse_x >= mouse_x:
        focal_point_x -= camera_rotation_velocity 
    
    if previous_mouse_y <= mouse_y:
        focal_point_y -= camera_rotation_velocity

    if previous_mouse_y >= mouse_y:
        focal_point_y += camera_rotation_velocity

    previous_mouse_x = mouse_x
    previous_mouse_y = mouse_y

    

def main():
    glutInit()
    
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(WINDOW_POSITION_X, WINDOW_POSITION_Y)
    glutCreateWindow("Hello World")

    glutSetCursor(GLUT_CURSOR_NONE)

    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard_handler)
    glutPassiveMotionFunc(mouse_motion_handler)
    glutIdleFunc(idle_display)
    glutReshapeFunc(reshape)
    
    glutMainLoop()

if __name__ == "__main__":
    main()