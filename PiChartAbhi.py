from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

def draw_circle_points(xc, yc, x, y):
    glBegin(GL_POINTS)
    glVertex2i(xc + x, yc + y)
    glVertex2i(xc - x, yc + y)
    glVertex2i(xc + x, yc - y)
    glVertex2i(xc - x, yc - y)
    glVertex2i(xc + y, yc + x)
    glVertex2i(xc - y, yc + x)
    glVertex2i(xc + y, yc - x)
    glVertex2i(xc - y, yc - x)
    glEnd()

# Midpoint Circle Drawing Algorithm
def circle_midpoint(xc, yc, r):
    x = 0
    y = r
    p = 1 - r
    draw_circle_points(xc, yc, x, y)

    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        draw_circle_points(xc, yc, x, y)
    glFlush()

# DDA Line Drawing Algorithm
def DDA(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    x_increment = dx / steps
    y_increment = dy / steps

    x = x1
    y = y1

    glBegin(GL_POINTS)
    for _ in range(steps + 1):
        glVertex2i(round(x), round(y))
        x += x_increment
        y += y_increment
    glEnd()
    glFlush()

# Find the coordinates on the circle for the given angle
def find_coordinates(xc, yc, r, m):
    coords = []
    x = xc + math.sqrt(r*2 / (1 + m*2))
    y = yc + m * math.sqrt(r*2 / (1 + m*2))
    coords.append((int(round(x)), int(round(y))))

    x = xc - math.sqrt(r*2 / (1 + m*2))
    y = yc - m * math.sqrt(r*2 / (1 + m*2))
    coords.append((int(round(x)), int(round(y))))

    return coords

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    xc, yc, r = 250, 250, 100

    glColor3f(1.0, 0.0, 0.0)

    # Draw the circle
    circle_midpoint(xc, yc, r)

    # Prompt user for input
    n = 3
    deg=[0,45,90]
    c=0
    for _ in range(n):
        angle_degree = float(deg[c])
        c+=1 
        angle_radians = math.radians(angle_degree)
        coords = find_coordinates(xc, yc, r, math.tan(angle_radians))

        # Draw the line
        DDA(coords[0][0], coords[0][1], coords[1][0], coords[1][1])

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Circle Divided by Lines at Different Angles")

    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(0.0, 500.0, 0.0, 500.0)

    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()