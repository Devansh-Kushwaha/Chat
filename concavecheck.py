import sys
import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


polygon_vertices = [
    (0, 0),
    (4, 0),
    (4, 4),
    (2, 2),
    (0, 4)
]


scaled_vertices = [(x / 5.0, y / 5.0) for x, y in polygon_vertices]

def is_polygon_concave(vertices):

    n = len(vertices)
    if n < 3:
        raise ValueError("A polygon must have at least 3 vertices.")


    edges = [(vertices[(i + 1) % n][0] - vertices[i][0], 
              vertices[(i + 1) % n][1] - vertices[i][1]) for i in range(n)]
    

    cross_signs = []
    for i in range(n):
        x1, y1 = edges[i]
        x2, y2 = edges[(i + 1) % n]
        cross_product = x1 * y2 - y1 * x2  
        cross_signs.append(np.sign(cross_product))
    

    is_concave = not all(sign == cross_signs[0] for sign in cross_signs if sign != 0)
    return is_concave

def display():
    """OpenGL display callback."""
    glClear(GL_COLOR_BUFFER_BIT)
    

    glColor3f(0.0, 0.0, 0.0)  
    glBegin(GL_LINE_LOOP)
    for x, y in scaled_vertices:
        glVertex2f(x, y)
    glEnd()

    
    glPointSize(5)
    glColor3f(1.0, 0.0, 0.0)  
    glBegin(GL_POINTS)
    for x, y in scaled_vertices:
        glVertex2f(x, y)
    glEnd()

    glFlush()

def main():
    """Main function to initialize OpenGL and run the display loop."""
    
    if is_polygon_concave(polygon_vertices):
        print("The polygon is concave.")
    else:
        print("The polygon is convex.")

    
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(800, 800)
    glutCreateWindow(b"Polygon Concavity Check")
    glutDisplayFunc(display)
    glClearColor(1.0, 1.0, 1.0, 1.0)  
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)  
    glutMainLoop()

if __name__ == "__main__":
    main()
