from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

def draw_circle(radius, vertices):
    theta = 0
    for _ in range(vertices):
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)
        glVertex2f(x, y)
        theta += 2 * math.pi / vertices

def draw_hexagon(radius):
    draw_circle(radius, 6)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-10, 10, -10, 10)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glColor3f(1, 0, 0)
    glBegin(GL_LINE_LOOP)
    draw_circle(5, 100)
    glEnd()
    glColor3f(0, 0, 1)  
    glBegin(GL_LINE_LOOP)
    draw_hexagon(5)
    glEnd()
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(400, 400)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"OpenGL Circle and Hexagon")
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()