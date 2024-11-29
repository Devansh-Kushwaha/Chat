from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_ellipse(x_center, y_center, a, b):
    x = 0
    y = b
    a2 = a * a
    b2 = b * b
    d1 = b2 - (a2 * b) + (0.25 * a2)
    dx = 2 * b2 * x
    dy = 2 * a2 * y

    glBegin(GL_POINTS)
    while dx < dy:
        glVertex2f(x_center + x, y_center + y)
        glVertex2f(x_center - x, y_center + y)
        glVertex2f(x_center + x, y_center - y)
        glVertex2f(x_center - x, y_center - y)

        if d1 < 0:
            x += 1
            dx += 2 * b2
            d1 += dx + b2
        else:
            x += 1
            y -= 1
            dx += 2 * b2
            dy -= 2 * a2
            d1 += dx - dy + b2

    d2 = (b2 * ((x + 0.5) ** 2)) + (a2 * ((y - 1) ** 2)) - (a2 * b2)
    while y >= 0:
        glVertex2f(x_center + x, y_center + y)
        glVertex2f(x_center - x, y_center + y)
        glVertex2f(x_center + x, y_center - y)
        glVertex2f(x_center - x, y_center - y)

        if d2 > 0:
            y -= 1
            dy -= 2 * a2
            d2 += a2 - dy
        else:
            y -= 1
            x += 1
            dx += 2 * b2
            dy -= 2 * a2
            d2 += dx - dy + a2
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_ellipse(250, 250, 150, 100)
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Midpoint Ellipse Drawing")
    gluOrtho2D(0, 500, 0, 500)
    glutDisplayFunc(display)
    glutMainLoop()

main()
