import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def bresenham_line(x0, y0, x1, y1):
    points = []
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    
    while True:
        points.append((x0, y0))
        if x0 == x1 and y0 == y1:
            break
        e2 = err * 2
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy
    
    return points


def init_gl():
    glClearColor(1.0, 1.0, 1.0, 1.0) 
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)  
    glPointSize(1.0)


def draw_line():
    glBegin(GL_POINTS)
    for point in bresenham_line(10, 10, 300, 200):
        glVertex2f(point[0]+100, point[1]+100)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_line()
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(600, 400)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Bresenham's Line Drawing Algorithm")
    
    glOrtho(0, 600, 0, 400, -1, 1)
    init_gl()
    
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
