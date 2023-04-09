from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_POSITION_X = 200
WINDOW_POSITION_Y = 100

is_fullscreen = False
current_window_width = WINDOW_WIDTH
current_window_height = WINDOW_HEIGHT
f_aspect = current_window_width/current_window_height

VIEW_RANGE = 500

camera_x = 0
camera_y = 0
camera_z = 100

camera_rot_vert = 0.0
camera_rot_hori = 0.0

camera_movement_velocity = 2
camera_rotation_velocity = 0.4

focal_point_x = 0
focal_point_y = 0
focal_point_z = 0

previous_mouse_x = 0
previous_mouse_y = 0

# -------------------
def on_mouse_move(x, y):
    global previous_mouse_x, previous_mouse_y, camera_rot_hori, camera_rot_vert

    # Calculate the mouse movement
    mouse_dx = x - previous_mouse_x
    mouse_dy = y - previous_mouse_y

    # Update the camera orientation
    camera_rot_hori += mouse_dx * camera_rotation_velocity
    camera_rot_vert += mouse_dy * camera_rotation_velocity

    # Clamp the pitch to prevent the camera from flipping over
    camera_rot_vert = max(-90.0, min(90.0, camera_rot_vert))

    # Update the last mouse position
    previous_mouse_x = x
    previous_mouse_y = y

def on_key_press(key, x, y):
    global camera_x, camera_y, camera_z, camera_rot_hori, camera_rot_vert

    # Calculate the movement direction
    speed = camera_movement_velocity
    forward = [sin(radians(camera_rot_hori)), sin(radians(-camera_rot_vert)), -cos(radians(camera_rot_hori))]
    right = [sin(radians(camera_rot_hori - 90)), 0, -cos(radians(camera_rot_hori - 90))]
    
    if key == b'\x1b':
        glutDestroyWindow(glutGetWindow())
    elif key == b'o' or key == b'O':
        screen_handler()
    elif key == b'w' or key == b'W':
        camera_x += forward[0] * speed
        camera_y += forward[1] * speed
        camera_z += forward[2] * speed
    elif key == b's' or key == b'S':
        camera_x -= forward[0] * speed
        camera_y -= forward[1] * speed
        camera_z -= forward[2] * speed
    elif key == b'a' or key == b'A':
        camera_x += right[0] * speed
        camera_y += right[1] * speed
        camera_z += right[2] * speed
    elif key == b'd' or key == b'D':
        camera_x -= right[0] * speed
        camera_y -= right[1] * speed
        camera_z -= right[2] * speed
# -------------------

def draw_axis():
    glColor3f(1, 0, 0)
    glBegin(GL_LINES)
    glVertex3f(1, 0, 0)
    glVertex3f(camera_x + VIEW_RANGE, 0, 0)
    glEnd()

    glColor3f(0, 1, 0)
    glBegin(GL_LINES)
    glVertex3f(0, 1, 0)
    glVertex3f(0, camera_y + VIEW_RANGE, 0)
    glEnd()

    glColor3f(0, 0, 1)
    glBegin(GL_LINES)
    glVertex3f(0, 0, 1)
    glVertex3f(0, 0, camera_z + VIEW_RANGE)
    glEnd()

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
    draw_axis()
    draw_room()
    
    # end draw code

    glutSwapBuffers()

def set_visualization():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(60, f_aspect, 0.5, VIEW_RANGE)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    up = [0.0, 1.0, 0.0]
    at = [camera_x + sin(radians(camera_rot_hori)) * cos(radians(camera_rot_vert)),
          camera_y + sin(radians(-camera_rot_vert)),
          camera_z - cos(radians(camera_rot_hori)) * cos(radians(camera_rot_vert))]
    
    gluLookAt(camera_x, camera_y, camera_z, at[0], at[1], at[2], up[0], up[1], up[2])

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

    #glutSetCursor(GLUT_CURSOR_NONE)

    glutDisplayFunc(display)
    glutKeyboardFunc(on_key_press)
    glutPassiveMotionFunc(on_mouse_move)
    glutIdleFunc(idle_display)
    glutReshapeFunc(reshape)
    
    glutMainLoop()

if __name__ == "__main__":
    main()