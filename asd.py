from OpenGL.GL import *
from OpenGL.GLUT import *
import math

def draw_circle(radius, x, y):
    glBegin(GL_LINE_LOOP)
    for i in range(100):
        angle = 2 * math.pi * i / 100
        glVertex2f(x + math.cos(angle) * radius, y + math.sin(angle) * radius)
    glEnd()

def draw_hexagon(radius, x, y):
    glBegin(GL_LINE_LOOP)
    for i in range(6):
        angle = 2 * math.pi * i / 6
        glVertex2f(x + math.cos(angle) * radius, y + math.sin(angle) * radius)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    draw_circle(0.5, 0, 0)
    draw_hexagon(0.4, 0, 0)
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(400, 400)
    glutCreateWindow("Circle and Hexagon")
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()