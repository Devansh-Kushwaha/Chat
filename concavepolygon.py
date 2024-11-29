from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw():
    glBegin(GL_LINE_LOOP)
    glVertex2f(100,200)
    glVertex2f(350,150)
    glVertex2f(300,400)
    glVertex2f(400,100)
    glEnd()
    
def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    glLoadIdentity()
    iterate()
    glColor3f(1, 0, 0)
    draw()
    glutSwapBuffers()
    

glutInit()
glutInitDisplayMode(GLUT_RGBA) 
glutInitWindowSize(500, 500) 
glutInitWindowPosition(0, 0)  
wind = glutCreateWindow("OpenGL Coding Practice")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)   
glutMainLoop()