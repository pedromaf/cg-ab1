from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *

from text import *
from room import Room
from axis import Axis
from door import Door
from fan import Fan
from table import Table
from chair import Chair
from board import Board
from window import Window
from ground import Ground

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_POSITION_X = 200
WINDOW_POSITION_Y = 100

is_fullscreen = False
current_window_width = WINDOW_WIDTH
current_window_height = WINDOW_HEIGHT
f_aspect = current_window_width/current_window_height

view_range = 1000

camera_x = 50
camera_y = 25
camera_z = 50
camera_rot_vert = 0.0
camera_rot_hori = 0.0
camera_movement_velocity = 5
camera_rotation_velocity = 0.5

focal_point_x = 0
focal_point_y = 0
focal_point_z = 0

previous_mouse_x = 0
previous_mouse_y = 0

door_animation = False
door_animation_speed = 10
door_width = 10
door_height = 20
door_position_x = 10

room_width = 70
room_height = 40
room_x = 20
room_y = 0.1
room_z = -10

door_animation_speed = 10
window_animation_speed = 10

window_animation = False
number_of_windows = 3
center_window = int(number_of_windows/2)
windows = []
for i in range(-number_of_windows+1, 1):
    windows.append(Window(room_x, room_y, room_z, room_width, room_height, window_animation_speed, i))

axis_enabled = True

light_on = True
day_light = True

axis = Axis()

ground = Ground(camera_x, camera_z, view_range)

room = Room(room_x, room_y, room_z, room_width, room_height, door_width, door_height, door_position_x, windows[center_window], number_of_windows)

door = Door(room_x + door_position_x, room_y, room_z, door_width, door_height, door_animation_speed)

left_fan = Fan(room_x + room_width * 0.30,  room_y + room_height - 3, room_z - room_width * 0.5, 1.5)
right_fan = Fan(room_x + room_width * 0.70, room_y + room_height - 3, room_z - room_width * 0.5, 1.5)

left_table = Table(room_x + 4,               room_y, room_z - room_width * 0.70, 8, 6, room_width * 0.5279, 1)
right_table = Table(room_x + room_width - 4, room_y, room_z - room_width * 0.70, 8, 6, room_width * 0.5279, 1)
back_table = Table(room_x + room_width/2,    room_y, room_z - room_width + 4, 8,       room_width * 0.73, 6, 1)

right_chair = Chair(room_x + room_width - 10, room_y, room_z - room_width + 25, 5, 6, 1, 0)
left_chair = Chair(room_x + 10,               room_y, room_z - room_width + 25, 5, 6, 1, 180)

back_chair1 = Chair(room_x + room_width - 20, room_y, room_z - room_width + 15, 5, 6, 1, 90)
back_chair2 = Chair(room_x + 20, room_y, room_z - room_width + 15, 5, 6, 1, 90)
back_chair3 = Chair(room_x + room_width/2, room_y, room_z - room_width + 15, 5, 6, 1, 90)

board = Board(room_x + 45, room_y + 15, room_z - 0.4, 15, 25, 0.3, 1, 180)

def display():
    global room, axis, door
    global camera_movement_velocity, current_window_width, current_window_height
    global day_light

    if day_light:
        glClearColor(0.5, 0.8, 1, 1)
    else:
        glClearColor(0.08, 0.08, 0.2, 1)
         
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glEnable(GL_DEPTH_TEST)
    glEnableClientState(GL_VERTEX_ARRAY)

    set_visualization()

    ground.draw()

    # begin draw code
    if axis_enabled:
        axis.draw(camera_x, camera_y, camera_z, view_range)

    room.draw()

    for window in windows:
        window.draw()

    door.draw()

    left_fan.draw()
    right_fan.draw()

    left_table.draw()
    right_table.draw()
    back_table.draw()

    right_chair.draw()
    left_chair.draw()

    back_chair1.draw()
    back_chair2.draw()
    back_chair3.draw()

    board.draw()

    draw_text(f"[Mouse Left] Control door", [0, current_window_height], current_window_width, current_window_height)
    draw_text(f"[W, A, S, D] Navigate", [0, current_window_height - 25], current_window_width, current_window_height)
    draw_text(f"[Z] Control windows", [0, current_window_height - 50], current_window_width, current_window_height)
    draw_text(f"[N] Decrease speed", [0, current_window_height - 75], current_window_width, current_window_height)
    draw_text(f"[M] Increase speed", [0, current_window_height - 100], current_window_width, current_window_height)
    draw_text(f"[L] Light ON/OFF", [0, current_window_height - 125], current_window_width, current_window_height)
    draw_text(f"[O] Fullscreen", [0, current_window_height - 150], current_window_width, current_window_height)
    draw_text(f"[X] Show axis", [0, current_window_height - 175], current_window_width, current_window_height)
    draw_text(f"[K] Day/Night", [0, current_window_height - 200], current_window_width, current_window_height)
    
    draw_text(f"Camera speed: {camera_movement_velocity} | Camera coordinates {round(camera_x), round(camera_y), round(camera_z)}", [0, 25], current_window_width, current_window_height)
    # end draw code

    glutSwapBuffers()

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
    global camera_x, camera_y, camera_z, camera_rot_hori, camera_rot_vert, camera_movement_velocity
    global room, door_animation, axis_enabled, window_animation, light_on, day_light

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
    elif key == b'z' or key == b'Z':
        window_animation = True
    elif key == b'm' or key == b'M':
        if (camera_movement_velocity < 10):
            camera_movement_velocity += 0.5
    elif key == b'n' or key == b'N':
        if (camera_movement_velocity > 0.5):
            camera_movement_velocity -= 0.5
    elif key == b'x' or key == b'X':
        axis_enabled = not axis_enabled
    elif key == b'l' or key == b'L':
        if light_on:
            glDisable(GL_LIGHT0)
        else:
            glEnable(GL_LIGHT0)
        light_on = not light_on
    elif key == b'k' or key == b'K':
        day_light = not day_light

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
    global door_animation, window_animation

    if door_animation:
        door.trigger_animation()
        door_animation = False

    if window_animation:
        for window in windows:
            window.trigger_animation()
        window_animation = False

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

def mouse_action_handler(button, state, mouse_x, mouse_y):
    global door_animation

    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        door_animation = True

def main():
    glutInit()

    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(WINDOW_POSITION_X, WINDOW_POSITION_Y)
    glutCreateWindow("Laboratorio de Controle")

    glutSetCursor(GLUT_CURSOR_NONE)
    glEnable(GL_DEPTH_TEST)

    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard_handler)
    glutPassiveMotionFunc(mouse_movement_handler)
    glutMouseFunc(mouse_action_handler)
    glutIdleFunc(idle_display)
    glutReshapeFunc(reshape)

    glutTimerFunc(100, left_fan.animation, 1)
    glutTimerFunc(100, right_fan.animation, 2)

    glutMainLoop()


if __name__ == "__main__":
    main()
