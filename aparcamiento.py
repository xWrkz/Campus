from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

camera_angle_x = 0
camera_angle_y = 0
camera_distance = 40
mouse_x, mouse_y = 0, 0
mouse_left_down = False

def init():
    glClearColor(0.5, 0.7, 0.9, 1.0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

def draw_parking_lot():
    # Ground (gray color)
    glColor3f(0.6, 0.6, 0.6)
    glPushMatrix()
    glTranslatef(0.0, -0.05, 0.0)
    glScalef(20.0, 0.1, 10.0)
    glutSolidCube(1)
    glPopMatrix()

    # Parking lines (white lines)
    glColor3f(1.0, 1.0, 1.0)
    glLineWidth(2)
    for i in range(-9, 10, 2):
        glPushMatrix()
        glBegin(GL_LINES)
        glVertex3f(i, 0.01, -4.5)
        glVertex3f(i, 0.01, 4.5)
        glEnd()
        glPopMatrix()

    # Draw green areas (grass) on the sides
    glColor3f(0.0, 0.8, 0.0)  # Green for grass
    glPushMatrix()
    glTranslatef(-12.0, -0.04, 0.0)  # Left side green area
    glScalef(2.0, 0.02, 10.0)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(12.0, -0.04, 0.0)  # Right side green area
    glScalef(2.0, 0.02, 10.0)
    glutSolidCube(1)
    glPopMatrix()

    # Trees (green with brown trunks)
    glColor3f(0.3, 0.8, 0.3)  # Green leaves
    for i in [-8, -4, 0, 4, 8]:
        glPushMatrix()
        glTranslatef(i, 0.1, -5.0)
        glutSolidSphere(0.5, 20, 20)
        glPopMatrix()

        glColor3f(0.4, 0.2, 0.1)  # Brown trunk
        glPushMatrix()
        glTranslatef(i, -0.25, -5.0)
        glScalef(0.1, 0.5, 0.1)
        glutSolidCube(1)
        glPopMatrix()

    # Lamp posts
    glColor3f(0.1, 0.1, 0.1)
    for i in [-9, -3, 3, 9]:
        glPushMatrix()
        glTranslatef(i, 1.0, 5.0)
        glScalef(0.1, 3.0, 0.1)
        glutSolidCube(1)
        glPopMatrix()

        # Lamp light
        glColor3f(1.0, 1.0, 0.8)
        glPushMatrix()
        glTranslatef(i, 2.0, 5.0)
        glutSolidSphere(0.3, 20, 20)
        glPopMatrix()

def draw_scene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Apply camera transformations
    glTranslatef(0.0, 0.0, -camera_distance)
    glRotatef(camera_angle_x, 1.0, 0.0, 0.0)
    glRotatef(camera_angle_y, 0.0, 1.0, 0.0)

    # Draw the parking lot
    glPushMatrix()
    draw_parking_lot()  # No extra transformations, directly draw parking lot
    glPopMatrix()

    glutSwapBuffers()

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
    glutCreateWindow(b"Parking Lot Scene")
    init()
    glutDisplayFunc(draw_scene)
    glutReshapeFunc(reshape)
    glutMouseFunc(mouse_button)
    glutMotionFunc(mouse_motion)
    glutMainLoop()

if __name__ == "__main__":
    main()
