import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


characters = {
    'A': [
        (-0.9, -0.5, -0.8, 0.5),  
        (-0.8, 0.5, -0.7, -0.5),  
        (-0.85, 0.0, -0.75, 0.0), 
    ],
    'B': [
        (-0.6, -0.5, -0.6, 0.5),  
        (-0.6, 0.5, -0.4, 0.3),   
        (-0.4, 0.3, -0.6, 0.0),   
        (-0.6, 0.0, -0.4, -0.2),  
        (-0.4, -0.2, -0.6, -0.5), 
    ],
    'C': [
        (-0.3, 0.3, -0.1, 0.5),   
        (-0.3, 0.3, -0.3, -0.3),  
        (-0.3, -0.3, -0.1, -0.5), 
    ],
    'D': [
        (0.1, -0.5, 0.1, 0.5),    
        (0.1, 0.5, 0.3, 0.3),     
        (0.3, 0.3, 0.3, -0.3),    
        (0.3, -0.3, 0.1, -0.5),   
    ],
}

def draw_character(strokes):
    glBegin(GL_LINES)
    for stroke in strokes:
        x1, y1, x2, y2 = stroke
        glVertex2f(x1, y1)
        glVertex2f(x2, y2)
    glEnd()

def display():

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0) 


    for character, strokes in characters.items():
        draw_character(strokes)
    
    glFlush()

def main():

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(800, 800)
    glutCreateWindow(b"Character Generation by Stroke Method")
    glutDisplayFunc(display)
    glClearColor(1.0, 1.0, 1.0, 1.0)  
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)  
    glutMainLoop()

if __name__ == "__main__":
    main()
