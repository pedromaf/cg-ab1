from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from PIL import Image, ImageDraw, ImageFont

def draw_text(text, position, window_width, window_height):
    font = ImageFont.truetype('arial.ttf', 24)
    size = font.getsize(text)
    image = Image.new('RGBA', size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), text, font=font, fill=(255, 255, 255, 0))
    texture_data = image.tobytes('raw', 'RGBA')
    texture_id = glGenTextures(1)

    glColor3f(1, 1, 1)
    
    glBindTexture(GL_TEXTURE_2D, texture_id)

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, size[0], size[1], 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data)
    
    glEnable(GL_TEXTURE_2D)
    glMatrixMode(GL_PROJECTION)
    
    glPushMatrix()
    
    glLoadIdentity()
    
    glOrtho(0, window_width, 0, window_height, -1, 1)
    
    glMatrixMode(GL_MODELVIEW)
    
    glPushMatrix()
    
    glLoadIdentity()
    
    glTranslatef(position[0], position[1], 0)
    glScalef(1.0, -1.0, 1.0)
    
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex2f(0, 0)
    glTexCoord2f(1.0, 0.0)
    glVertex2f(size[0], 0)
    glTexCoord2f(1.0, 1.0)
    glVertex2f(size[0], size[1])
    glTexCoord2f(0.0, 1.0)
    glVertex2f(0, size[1])
    glEnd()
    
    glPopMatrix()
    
    glDisable(GL_TEXTURE_2D)
    
    glMatrixMode(GL_PROJECTION)
    
    glPopMatrix()