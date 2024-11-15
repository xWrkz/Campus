from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

camera_angle_x = 0
camera_angle_y = 0
camera_distance = 40
mouse_x, mouse_y = 0, 0
mouse_left_down = False
student_position = 0.0  # Student's position along the path

def init():
    glClearColor(0.5, 0.7, 0.9, 1.0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

def draw_parking_lot():
    # Parking lot base
    glColor3f(0.6, 0.6, 0.6)
    glPushMatrix()
    glTranslatef(0.0, -0.05, 0.0)
    glScalef(20.0, 0.1, 10.0)
    glutSolidCube(1)
    glPopMatrix()

    # Parking lines
    glColor3f(1.0, 1.0, 1.0)
    glLineWidth(2)
    for i in range(-9, 10, 2):
        glPushMatrix()
        glBegin(GL_LINES)
        glVertex3f(i, 0.01, -4.5)
        glVertex3f(i, 0.01, 4.5)
        glEnd()
        glPopMatrix()

    # Grass areas on the sides
    glColor3f(0.0, 0.8, 0.0)
    glPushMatrix()
    glTranslatef(-12.0, -0.04, 0.0)
    glScalef(2.0, 0.02, 10.0)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(12.0, -0.04, 0.0)
    glScalef(2.0, 0.02, 10.0)
    glutSolidCube(1)
    glPopMatrix()

    # Trees along the parking lot
    for i in [-8, -4, 0, 4, 8]:
        glColor3f(0.2, 0.6, 0.2)
        for dx in [-0.2, 0.2]:
            for dz in [-0.2, 0.2]:
                glPushMatrix()
                glTranslatef(i + dx, 0.6, -5.0 + dz)
                glutSolidSphere(0.4, 20, 20)
                glPopMatrix()

        glColor3f(0.4, 0.2, 0.1) 
        glPushMatrix()
        glTranslatef(i, 0.1, -5.0)
        glScalef(0.15, 0.7, 0.15)
        glutSolidCube(1)
        glPopMatrix()

    # Light poles
    for i in [-9, -3, 3, 9]:
        glColor3f(0.1, 0.1, 0.1)
        glPushMatrix()
        glTranslatef(i, 1.5, 5.0)
        glScalef(0.1, 3.5, 0.1)
        glutSolidCube(1)
        glPopMatrix()

        glColor3f(1.0, 1.0, 0.7)
        glPushMatrix()
        glTranslatef(i, 2.5, 5.0)
        glutSolidSphere(0.3, 20, 20)  
        glPopMatrix()

        glColor4f(1.0, 1.0, 0.7, 0.3) 
        glPushMatrix()
        glTranslatef(i, 2.5, 5.0)
        glutSolidSphere(0.5, 20, 20)  
        glPopMatrix()
    
    # Sidewalk and path line
    glColor3f(0.7, 0.7, 0.7)  # Grey color for the sidewalk
    glPushMatrix()
    glTranslatef(-10.0, -0.04, 0.0)
    glScalef(1.5, 0.02, 10.0)
    glutSolidCube(1)
    glPopMatrix()

    # Dotted line on the sidewalk
    glColor3f(0.0, 0.0, 0.0)
    glLineWidth(2)
    for i in range(-5, 6):
        glPushMatrix()
        glTranslatef(-10.0, 0.01, i)
        glBegin(GL_LINES)
        glVertex3f(0, 0, 0)
        glVertex3f(0, 0, 0.5)
        glEnd()
        glPopMatrix()

def draw_student():
    global student_position
    glColor3f(1.0, 0.0, 0.0)  # Red color for the student
    glPushMatrix()
    glTranslatef(-10.0, 0.1, student_position)
    glutSolidSphere(0.3, 20, 20)
    glPopMatrix()

def draw_mini_map():
    # Set viewport for mini-map
    glViewport(10, 10, 150, 150)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1, 1, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    # Mini-map parking lot and sidewalk
    glColor3f(0.6, 0.6, 0.6)
    glBegin(GL_QUADS)
    glVertex2f(-0.5, -0.8)
    glVertex2f(0.5, -0.8)
    glVertex2f(0.5, 0.8)
    glVertex2f(-0.5, 0.8)
    glEnd()
    
    glColor3f(0.7, 0.7, 0.7)
    glBegin(GL_QUADS)
    glVertex2f(-0.8, -0.8)
    glVertex2f(-0.5, -0.8)
    glVertex2f(-0.5, 0.8)
    glVertex2f(-0.8, 0.8)
    glEnd()

    # Student position in mini-map
    glColor3f(1.0, 0.0, 0.0)
    glPushMatrix()
    glTranslatef(-0.65, student_position / 10, 0)
    glutSolidSphere(0.05, 10, 10)
    glPopMatrix()

    # Reset viewport back to full window after mini-map
    glViewport(0, 0, 1600, 900)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1600 / 900, 1, 200)
    glMatrixMode(GL_MODELVIEW)

def draw_scene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glTranslatef(0.0, 0.0, -camera_distance)
    glRotatef(camera_angle_x, 1.0, 0.0, 0.0)
    glRotatef(camera_angle_y, 0.0, 1.0, 0.0)

    glPushMatrix()
    draw_parking_lot()
    draw_student()
    glPopMatrix()

    draw_mini_map()

    glutSwapBuffers()

def keyboard(key, x, y):
    global student_position
    if key == b'w' and student_position < 5:
        student_position += 0.2
    elif key == b's' and student_position > -5:
        student_position -= 0.2
    glutPostRedisplay()

def mouse_motion(x, y):
    global camera_angle_x, camera_angle_y, mouse_x, mouse_y
    if mouse_left_down:
        delta_x = x - mouse_x
        delta_y = y - mouse_y
        camera_angle_x += delta_y * 0.2
        camera_angle_y += delta_x * 0.2
        glutPostRedisplay()
    mouse_x = x
    mouse_y = y

def mouse_button(button, state, x, y):
    global mouse_left_down
    if button == GLUT_LEFT_BUTTON:
        mouse_left_down = (state == GLUT_DOWN)

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, width / height, 1, 200)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(1600, 900)
    glutCreateWindow(b"Parking Lot Scene with Student Path and 3D Navigation")
    init()
    glutDisplayFunc(draw_scene)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutMouseFunc(mouse_button)
    glutMotionFunc(mouse_motion)
    glutMainLoop()

if __name__ == "__main__":
    main()
