import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

polygon = [(100, 100), (300, 100), (300, 300), (200, 200), (100, 300)]
point = (200, 150)  


def cross_product(v1, v2):
    return v1[0] * v2[1] - v1[1] * v2[0]


def winding_number(point, polygon):
    wn = 0  
    px, py = point

    for i in range(len(polygon)):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % len(polygon)]

        if y1 <= py:  
            if y2 > py:  
                if cross_product((x2 - x1, y2 - y1), (px - x1, py - y1)) > 0:
                    wn += 1
        else:  
            if y2 <= py:  
                if cross_product((x2 - x1, y2 - y1), (px - x1, py - y1)) < 0:
                    wn -= 1

    return wn


def display():
    glClear(GL_COLOR_BUFFER_BIT)


    glColor3f(1.0, 1.0, 1.0) 
    glBegin(GL_LINE_LOOP)
    for vertex in polygon:
        glVertex2f(*vertex)
    glEnd()

    glColor3f(1.0, 0.0, 0.0)
    glPointSize(8)
    glBegin(GL_POINTS)
    glVertex2f(*point)
    glEnd()


    wn = winding_number(point, polygon)
    print(f"Winding number: {wn}")

    glutSwapBuffers()


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(0, 400, 0, 400)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(400, 400)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Non-Zero Winding Number")
    init()
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
