from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
from table_lamp import TableLamp

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
from ceiling_lamp import CeilingLamp

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

axis_enabled = True

room_light_on = True
lamp_left_on = False
lamp_center_on = False
lamp_right_on = False
day_light_on = True
ambient_light_value = [0.7, 0.7, 0.7, 1.0]

door_animation_speed = 10
window_animation_speed = 10

window_animation = False
number_of_windows = 3
center_window = int(number_of_windows/2)
windows = []

for i in range(-number_of_windows+1, 1):
    windows.append(Window(room_x, room_y, room_z, room_width, room_height, window_animation_speed, i))

axis = Axis()

ground = Ground(camera_x, camera_z, view_range)

room = Room(room_x, room_y, room_z, room_width, room_height, door_width, door_height, door_position_x, windows[center_window], number_of_windows)

door = Door(room_x + door_position_x, room_y, room_z, door_width, door_height, door_animation_speed)

left_fan = Fan(room_x + room_width * 0.30,  room_y + room_height - 3, room_z - room_width * 0.5, 1.5)
right_fan = Fan(room_x + room_width * 0.70, room_y + room_height - 3, room_z - room_width * 0.5, 1.5)

left_table = Table(room_x + 4,               room_y, room_z - room_width * 0.70, 8, 6, room_width * 0.5279, 1)
right_table = Table(room_x + room_width - 4, room_y, room_z - room_width * 0.70, 8, 6, room_width * 0.5279, 1)
back_table = Table(room_x + room_width/2,    room_y, room_z - room_width + 4, 8,       room_width * 0.73, 6, 1)

right_chair = Chair(room_x + room_width - 10, room_y, room_z - room_width + 35, 5, 6, 1, 0)
left_chair = Chair(room_x + 10,               room_y, room_z - room_width + 25, 5, 6, 1, 180)

back_chair1 = Chair(room_x + room_width - 20, room_y, room_z - room_width + 15, 5, 6, 1, 90)
back_chair2 = Chair(room_x + 20, room_y, room_z - room_width + 15, 5, 6, 1, 90)
back_chair3 = Chair(room_x + room_width/2, room_y, room_z - room_width + 15, 5, 6, 1, 90)

board = Board(room_x + 45, room_y + 15, room_z - 0.4, 15, 25, 0.3, 1, 180)

ceiling_lamp = CeilingLamp(room_x, room_y, room_z, room_height, room_width)

table_lamp_r = TableLamp(87, 8, -45,  5.0, -180)
table_lamp_c = TableLamp(56, 8, -79,  5.0, -90)
table_lamp_l = TableLamp(21, 8, -45,  5.0, 0)

def display():
    global room, axis, door
    global camera_movement_velocity, current_window_width, current_window_height
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    set_visualization()

    lighting()

    # begin draw code
    ground.draw()

    if axis_enabled:
        axis.draw(camera_x, camera_y, camera_z, view_range)

    room.draw()

    left_table.draw()
    right_table.draw()
    back_table.draw()


    table_lamp_l.draw()
    table_lamp_r.draw()
    table_lamp_c.draw()

    door.draw()
    
    board.draw()
    
    for window in windows:
        window.draw()
    
    right_chair.draw()
    left_chair.draw()

    back_chair1.draw()
    back_chair2.draw()
    back_chair3.draw()

    left_fan.draw()
    right_fan.draw()

    ceiling_lamp.draw()

    draw_text(f"[Mouse Left] Control door", [0, current_window_height], current_window_width, current_window_height)
    draw_text(f"[W, A, S, D] Navigate", [0, current_window_height - 25], current_window_width, current_window_height)
    draw_text(f"[1, 2, 3] Lamp ON/OFF", [0, current_window_height - 50], current_window_width, current_window_height)
    draw_text(f"[Z] Control windows", [0, current_window_height - 75], current_window_width, current_window_height)
    draw_text(f"[N] Decrease speed", [0, current_window_height - 100], current_window_width, current_window_height)
    draw_text(f"[M] Increase speed", [0, current_window_height - 125], current_window_width, current_window_height)
    draw_text(f"[L] Light ON/OFF", [0, current_window_height - 150], current_window_width, current_window_height)
    draw_text(f"[O] Fullscreen", [0, current_window_height - 175], current_window_width, current_window_height)
    draw_text(f"[X] Show axis", [0, current_window_height - 200], current_window_width, current_window_height)
    draw_text(f"[K] Day/Night", [0, current_window_height - 225], current_window_width, current_window_height)
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
    global room, door_animation, axis_enabled, window_animation, room_light_on, day_light_on, lamp_left_on, lamp_center_on, lamp_right_on

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
        if room_light_on:
            glDisable(GL_LIGHT0)
            glDisable(GL_LIGHT1)
        else:
            glEnable(GL_LIGHT0)
            glEnable(GL_LIGHT1)
        room_light_on = not room_light_on
    elif key == b'k' or key == b'K':
        day_light_on = not day_light_on
    elif key == b'1':
        if lamp_left_on:
            glDisable(GL_LIGHT4)
        else:
            glEnable(GL_LIGHT4)
        lamp_left_on = not lamp_left_on
    elif key == b'2':
        if lamp_center_on:
            glDisable(GL_LIGHT3)
        else:
            glEnable(GL_LIGHT3)
        lamp_center_on = not lamp_center_on
    elif key == b'3':
        if lamp_right_on:
            glDisable(GL_LIGHT2)
        else:
            glEnable(GL_LIGHT2)
        lamp_right_on = not lamp_right_on        
        

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

def lighting():
    global day_light_on, ambient_light_value
    global camera_x, camera_y, camera_z

    luzEspecular = [0.3, 0.3, 0.3, 0]
    luzDifusa=[1, 1, 1, 1.0]
    posicaoLuz = [55.0, 39, -45.0, 0.0]
    material_specular = (0.2, 0.2, 0.2, 0.5)
    material_shininess = 36.0  

    luzDifusaSpot = [1, 1.0, 1.0, 1.0]  
    luzEspecSpot = [1, 0.3, 0.3, 1]  
    dirLuzSpot_lr = [0,-1,0]
    dirLuzSpot_c = [1,-1,0] 
    posLuzSpotRight =  [86, 12.00, -44, 1.0]
    posLuzSpotCenter =  [58, 12.00, -76, 1.0]
    posLuzSpotLeft =  [22, 12.00, -44, 1.0]


    if day_light_on:
        ambient_light_value = [0.7, 0.7, 0.7, 1.0]
        glClearColor(0.5, 0.8, 1, 1)
    else:
        ambient_light_value = [0.2, 0.2, 0.2, 1.0]
        glClearColor(0.08, 0.08, 0.2, 1)
    
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient_light_value)

    glLightfv(GL_LIGHT0, GL_SPOT_CUTOFF, 180)
    glLightfv(GL_LIGHT0, GL_POSITION, posicaoLuz)
    glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, [55.0, 0.0, -45.0])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, luzDifusa)

    glLightfv(GL_LIGHT1, GL_POSITION, [camera_x, camera_y, camera_z])
    glLightfv(GL_LIGHT1, GL_SPECULAR, luzEspecular)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, luzEspecular)

    # right
    glLightfv( GL_LIGHT2, GL_SPOT_CUTOFF, 70)
    glLightfv( GL_LIGHT2, GL_SPOT_EXPONENT, 1)
    glLightfv( GL_LIGHT2, GL_POSITION,  posLuzSpotRight)
    glLightfv( GL_LIGHT2, GL_SPOT_DIRECTION, dirLuzSpot_lr)
    glLightfv( GL_LIGHT2, GL_DIFFUSE, luzDifusaSpot )
    glLightfv( GL_LIGHT2, GL_SPECULAR, luzEspecSpot )

    
    #center
    glLightfv( GL_LIGHT3, GL_SPOT_CUTOFF, 75)
    glLightfv( GL_LIGHT3, GL_SPOT_EXPONENT, 1)
    glLightfv( GL_LIGHT3, GL_POSITION,  posLuzSpotCenter)
    glLightfv( GL_LIGHT3, GL_SPOT_DIRECTION, dirLuzSpot_c)
    glLightfv( GL_LIGHT3, GL_DIFFUSE, luzDifusaSpot )
    glLightfv( GL_LIGHT3, GL_SPECULAR, luzEspecSpot )

    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, material_specular)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, material_shininess)

    #left
    glLightfv( GL_LIGHT4, GL_SPOT_CUTOFF, 60)
    glLightfv( GL_LIGHT4, GL_SPOT_EXPONENT, 1)
    glLightfv( GL_LIGHT4, GL_POSITION,  posLuzSpotLeft)
    glLightfv( GL_LIGHT4, GL_SPOT_DIRECTION, dirLuzSpot_lr)
    glLightfv( GL_LIGHT4, GL_DIFFUSE, luzDifusaSpot )
    glLightfv( GL_LIGHT4, GL_SPECULAR, luzEspecSpot )

    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, material_specular)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, material_shininess)

def init_light():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_NORMALIZE)

def main():
    glutInit()

    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(WINDOW_POSITION_X, WINDOW_POSITION_Y)
    glutCreateWindow("Laboratorio de Controle")

    init_light()

    glutSetCursor(GLUT_CURSOR_NONE)
    glEnable(GL_DEPTH_TEST)
    glEnableClientState(GL_VERTEX_ARRAY)

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
