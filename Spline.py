import sys
import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


control_points = [
    [-0.8, -0.8],
    [-0.5, 0.2],
    [0.0, 0.8],
    [0.5, -0.2],
    [0.8, 0.8],
]


num_steps = 100

def bezier_curve(points, t):
    """Calculate a point on a Bezier curve using the De Casteljau algorithm."""
    n = len(points) - 1
    temp_points = np.array(points, dtype=float)
    for r in range(1, n + 1):
        for i in range(n - r + 1):
            temp_points[i] = (1 - t) * temp_points[i] + t * temp_points[i + 1]
    return temp_points[0]

def generate_curve():
    """Generate the spline curve points."""
    curve = []
    for i in range(num_steps + 1):
        t = i / num_steps
        point = bezier_curve(control_points, t)
        curve.append(point)
    return curve

def display():
    """Display callback function for OpenGL."""
    glClear(GL_COLOR_BUFFER_BIT)
    
  
    glPointSize(5)
    glColor3f(1.0, 0.0, 0.0) 
    glBegin(GL_POINTS)
    for point in control_points:
        glVertex2f(point[0], point[1])
    glEnd()
    
  
    glColor3f(0.0, 1.0, 0.0) 
    glBegin(GL_LINE_STRIP)
    for point in control_points:
        glVertex2f(point[0], point[1])
    glEnd()
    
   
    curve_points = generate_curve()
    glColor3f(0.0, 0.0, 1.0)  
    glBegin(GL_LINE_STRIP)
    for point in curve_points:
        glVertex2f(point[0], point[1])
    glEnd()
    
    glFlush()

def main():
    """Main function to initialize OpenGL and create the window."""
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(800, 800)
    glutCreateWindow(b"Spline Curve Generation")
    glutDisplayFunc(display)
    glClearColor(1.0, 1.0, 1.0, 1.0)  
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)  
    glutMainLoop()

if __name__ == "__main__":
    main()
