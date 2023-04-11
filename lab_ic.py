import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *

from room import Room
from axis import Axis
from door import Door
from fan import Fan
from table import Table
from chair import Chair
from board import Board

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_POSITION_X = 200
WINDOW_POSITION_Y = 100

is_fullscreen = False
current_window_width = WINDOW_WIDTH
current_window_height = WINDOW_HEIGHT
f_aspect = current_window_width/current_window_height

view_range = 500

camera_x = 20
camera_y = 10
camera_z = 30
camera_rot_vert = 0.0
camera_rot_hori = 0.0
camera_movement_velocity = 1
camera_rotation_velocity = 0.4

focal_point_x = 0
focal_point_y = 0
focal_point_z = 0

previous_mouse_x = 0
previous_mouse_y = 0

door_animation = False
door_animation_speed = 4
door_width = 10
door_height = 20
door_position_x = 10

room_width = 50
room_height = 40
room_x = 20
room_y = 0
room_z = -10

axis = Axis()
room = Room(room_x, room_y, room_z, room_width, room_height,
            door_width, door_height, door_position_x)
door = Door(room_x + door_position_x, room_y, room_z,
            door_width, door_height, door_animation_speed)
fan1 = Fan(room_x + 40, room_y + room_height - 3, room_z - 15, 1.5)
fan2 = Fan(room_x + 10, room_y + room_height - 3, room_z - 15, 1.5)
fan3 = Fan(room_x + 10, room_y + room_height - 3, room_z - 35, 1.5)
fan4 = Fan(room_x + 40, room_y + room_height - 3, room_z - 35, 1.5)
table = Table(10, 0, 10, 30, 50, 10, 1)
chair = Chair(10, 30, 10, 5, 5, 1)
board = Board(0, 0, 0, 13, 20, 0.3, 1)


def mouse_movement_handler(x, y):
    global previous_mouse_x, previous_mouse_y, camera_rot_hori, camera_rot_vert

    center_x = int(int(glutGet(GLUT_WINDOW_WIDTH))/2)
    center_y = int(int(glutGet(GLUT_WINDOW_HEIGHT))/2)

    pointer_boundery_x = center_x * 0.5
    pointer_boundery_y = center_y * 0.5

    if x >= center_x + pointer_boundery_x or x <= center_x - pointer_boundery_x:
        glutWarpPointer(center_x, center_y)
        previous_mouse_x = center_x
        previous_mouse_y = center_y
        return

    if y >= center_y + pointer_boundery_y or y <= center_y - pointer_boundery_y:
        glutWarpPointer(center_x, center_y)
        previous_mouse_x = center_x
        previous_mouse_y = center_y
        return

    mouse_dx = x - previous_mouse_x
    mouse_dy = y - previous_mouse_y

    camera_rot_hori += mouse_dx * camera_rotation_velocity
    camera_rot_vert += mouse_dy * camera_rotation_velocity

    camera_rot_vert = max(-89.0, min(89.0, camera_rot_vert))

    previous_mouse_x = x
    previous_mouse_y = y


def keyboard_handler(key, mouse_x, mouse_y):
    global camera_x, camera_y, camera_z, camera_rot_hori, camera_rot_vert
    global room, door_animation

    speed = camera_movement_velocity
    forward = [sin(radians(camera_rot_hori)), sin(
        radians(-camera_rot_vert)), -cos(radians(camera_rot_hori))]
    right = [sin(radians(camera_rot_hori - 90)), 0, -
             cos(radians(camera_rot_hori - 90))]

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


def display():
    global room, axis, door

    glClearColor(0, 0, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glEnable(GL_DEPTH_TEST)
    glEnableClientState(GL_VERTEX_ARRAY)

    set_visualization()

    # begin draw code
    axis.draw(camera_x, camera_y, camera_z, view_range)
    room.draw()
    door.draw()
    # table.draw()
    chair.draw()
    board.draw()
    # end draw code

    glutSwapBuffers()


def set_visualization():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(60, f_aspect, 0.5, view_range)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    up = [0.0, 1.0, 0.0]
    at = [camera_x + sin(radians(camera_rot_hori)) * cos(radians(camera_rot_vert)),
          camera_y + sin(radians(-camera_rot_vert)),
          camera_z - cos(radians(camera_rot_hori)) * cos(radians(camera_rot_vert))]

    gluLookAt(camera_x, camera_y, camera_z,
              at[0], at[1], at[2], up[0], up[1], up[2])


def idle_display():
    global door_animation

    if door_animation:
        door.trigger_animation()
        door_animation = False

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


def mouse_action_handler(button, state, x, y):
    global door_animation

    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        door_animation = True


def main():
    glutInit()

    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(WINDOW_POSITION_X, WINDOW_POSITION_Y)
    glutCreateWindow("Hello World")

    glutSetCursor(GLUT_CURSOR_NONE)

    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard_handler)
    glutPassiveMotionFunc(mouse_movement_handler)
    glutMouseFunc(mouse_action_handler)
    glutIdleFunc(idle_display)
    glutReshapeFunc(reshape)

    glutTimerFunc(100, fan1.animation, 1)
    glutTimerFunc(100, fan2.animation, 2)
    glutTimerFunc(100, fan3.animation, 3)
    glutTimerFunc(100, fan4.animation, 4)

    glutMainLoop()


if __name__ == "__main__":
    main()
