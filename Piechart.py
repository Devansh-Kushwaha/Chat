import OpenGL.GL as gl
import OpenGL.GLUT as glut
import math

slices = [3, 2, 5, 2, 1]   
colors = [
    (1, 0, 0),  
    (0, 1, 0),  
    (0, 0, 1),  
    (1, 1, 0),  
    (0, 1, 1),  
]

def draw_pie_chart():
    total = sum(slices)
    angle_start = 0.0

    for i, slice_value in enumerate(slices):
        slice_percentage = slice_value / total
        angle_end = angle_start + slice_percentage * 360
        

        gl.glColor3f(*colors[i])


        gl.glBegin(gl.GL_TRIANGLE_FAN)
        gl.glVertex2f(0.0, 0.0) 


        for angle in range(int(angle_start), int(angle_end) + 1):
            radian = math.radians(angle)
            x = math.cos(radian)
            y = math.sin(radian)
            gl.glVertex2f(x, y)

        gl.glEnd()


        angle_start = angle_end

def display():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    gl.glLoadIdentity()

    draw_pie_chart()

    glut.glutSwapBuffers()

def setup():
    gl.glClearColor(1.0, 1.0, 1.0, 1.0)  
    gl.glOrtho(-1.5, 1.5, -1.5, 1.5, -1.0, 1.0)  

def main():
    glut.glutInit()
    glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB)
    glut.glutInitWindowSize(500, 500)
    glut.glutCreateWindow(b"Pie Chart with OpenGL")

    setup()

    glut.glutDisplayFunc(display)
    glut.glutMainLoop()

if __name__ == "__main__":
    main()
