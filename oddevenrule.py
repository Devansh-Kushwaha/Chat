from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

user_point = None  # Global variable for storing the clicked point
window_width, window_height = 1000, 1000  # Window dimensions

def is_point_in_polygon(user_point, polygon):
    # Set a point far outside the polygon for ray-casting
    outpoint = (-1000, -1000)
    
    # Define vertices and lines of the polygon
    Vertices = {
        "A": (232, 259), "B": (418, 179), "C": (378, 400), "D": (302, 444),
        "E": (443, 62), "F": (481, 157), "G": (578, 115), "H": (672, 422),
        "I": (362, 479), "K": (543, 303), "L": (343, 564), "M": (318, 486), "N": (218, 499)
    }
    Lines = ["AB", "BC", "CD", "DA", "BF", "BE", "FE", "FG", "GH", "HK", "KF", "HI", "IC", "CK", "IL", "LM", "MI", "DM", "MN", "ND"]

    intersections = 0
    for line in Lines:
        p1 = Vertices[line[0]]
        p2 = Vertices[line[1]]

        # Check if the ray intersects the line segment (p1, p2)
        if ((p1[1] > user_point[1]) != (p2[1] > user_point[1])):
            x_intersect = p1[0] + (user_point[1] - p1[1]) * (p2[0] - p1[0]) / (p2[1] - p1[1])
            if x_intersect > user_point[0]:  
                intersections += 1

    return intersections % 2 == 1  # Inside if odd, outside if even

def draw():
    glBegin(GL_POLYGON)
    glVertex2f(232, 259)
    glVertex2f(418, 179)
    glVertex2f(378, 400)
    glVertex2f(302, 444)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(443, 62)
    glVertex2f(481, 157)
    glVertex2f(418, 179)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(481, 157)
    glVertex2f(578, 115)
    glVertex2f(672, 422)
    glVertex2f(543, 303)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(543, 303)
    glVertex2f(672, 422)
    glVertex2f(362, 479)
    glVertex2f(378, 400)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(362, 479)
    glVertex2f(343, 564)
    glVertex2f(318, 486)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(318, 486)
    glVertex2f(218, 499)
    glVertex2f(302, 444)
    glEnd()

    if user_point:
        glColor3f(0, 1, 0)
        glPointSize(10)
        glBegin(GL_POINTS)
        glVertex2f(user_point[0], user_point[1])
        glEnd()

        if is_point_in_polygon(user_point, None):
            print("Point is inside the polygon.")
        else:
            print("Point is outside the polygon.")

def iterate():
    glViewport(0, 0, window_width, window_height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 700, 0.0, 700, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def show_screen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1, 0, 0)  # Red color for the polygons
    draw()
    glutSwapBuffers()

def mouse_click(button, state, x, y):
    global user_point
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        user_point = (x-100,700-y)  
        print(f"User point set to: {user_point}")
        glutPostRedisplay()  

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(window_width, window_height)
glutInitWindowPosition(0, 0)
glutCreateWindow("OpenGL Point-in-Polygon Test")
glutMouseFunc(mouse_click)
glutDisplayFunc(show_screen)
glutIdleFunc(show_screen)
glutMainLoop()
