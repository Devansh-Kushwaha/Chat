from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

def draw_ellipse(rx, ry, xc, yc):
    x = 0
    y = ry
    d1 = (ry ** 2) - (rx ** 2 * ry) + (0.25 * rx ** 2)
    dx = 2 * (ry ** 2) * x
    dy = 2 * (rx ** 2) * y
    
    while dx < dy:
        plot_ellipse_points(xc, yc, x, y)
        
        if d1 < 0:
            x += 1
            dx = dx + (2 * (ry ** 2))
            d1 = d1 + dx + (ry ** 2)
        else:
            x += 1
            y -= 1
            dx = dx + (2 * (ry ** 2))
            dy = dy - (2 * (rx ** 2))
            d1 = d1 + dx - dy + (ry ** 2)
    
    d2 = ((ry ** 2) * ((x + 0.5) ** 2)) + ((rx ** 2) * ((y - 1) ** 2)) - (rx ** 2 * ry ** 2)
    
    while y >= 0:
        plot_ellipse_points(xc, yc, x, y)
        
        if d2 > 0:
            y -= 1
            dy = dy - (2 * (rx ** 2))
            d2 = d2 + (rx ** 2) - dy
        else:
            y -= 1
            x += 1
            dx = dx + (2 * (ry ** 2))
            dy = dy - (2 * (rx ** 2))
            d2 = d2 + dx - dy + (rx ** 2)
            
def plot_ellipse_points(xc, yc, x, y):
    glBegin(GL_POINTS)
    glVertex2f(xc + x, yc + y) 
    glVertex2f(xc - x, yc + y) 
    glVertex2f(xc + x, yc - y) 
    glVertex2f(xc - x, yc - y) 
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    

    glColor3f(1, 0, 0)  
   
    draw_ellipse(200, 100, 250, 250)
    
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("Bresenham Ellipse")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()
