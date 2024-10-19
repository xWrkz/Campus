from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

plane_size = 10
camera_pos = [0, -2, -15]
mouse_prev_x = 0
mouse_prev_y = 0
is_mouse_dragging = False

def draw_floor():
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_QUADS)
    glVertex3f(-plane_size, 0, -plane_size)
    glVertex3f(plane_size, 0, -plane_size)
    glVertex3f(plane_size, 0, plane_size)
    glVertex3f(-plane_size, 0, plane_size)
    glEnd()

def draw_cube():
    glColor3f(0.5, 0.5, 0.5)
    glBegin(GL_QUADS)
    glVertex3f(-2, 0, 2)
    glVertex3f(2, 0, 2)
    glVertex3f(2, 4, 2)
    glVertex3f(-2, 4, 2)
    glVertex3f(-2, 0, -2)
    glVertex3f(-2, 4, -2)
    glVertex3f(2, 4, -2)
    glVertex3f(2, 0, -2)
    glVertex3f(-2, 0, -2)
    glVertex3f(-2, 0, 2)
    glVertex3f(-2, 4, 2)
    glVertex3f(-2, 4, -2)
    glVertex3f(2, 0, -2)
    glVertex3f(2, 0, 2)
    glVertex3f(2, 4, 2)
    glVertex3f(2, 4, -2)
    glVertex3f(-2, 0, -2)
    glVertex3f(-2, 0, 2)
    glVertex3f(2, 0, 2)
    glVertex3f(2, 0, -2)
    glEnd()

def draw_door():
    glColor3f(0.8, 0.5, 0.3)
    glBegin(GL_QUADS)
    glVertex3f(-0.5, 0, 2)
    glVertex3f(0.5, 0, 2)
    glVertex3f(0.5, 2, 2)
    glVertex3f(-0.5, 2, 2)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(camera_pos[0], camera_pos[1], camera_pos[2])
    draw_floor()
    draw_cube()
    draw_door()
    glutSwapBuffers()

def reshape(width, height):
    if height == 0:
        height = 1
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, float(width) / height, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def mouse_motion(x, y):
    global mouse_prev_x, mouse_prev_y, camera_pos, is_mouse_dragging
    if is_mouse_dragging:
        dx = x - mouse_prev_x
        dy = y - mouse_prev_y
        camera_pos[0] -= dx * 0.1
        camera_pos[1] += dy * 0.1

    mouse_prev_x = x
    mouse_prev_y = y
    glutPostRedisplay()

def mouse_click(button, state, x, y):
    global is_mouse_dragging, mouse_prev_x, mouse_prev_y
    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            is_mouse_dragging = True
            mouse_prev_x = x
            mouse_prev_y = y
        else:
            is_mouse_dragging = False

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b'3D Biblioteca fachada')
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.1, 0.1, 0.1, 1)
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMotionFunc(mouse_motion)
    glutMouseFunc(mouse_click)
    glutMainLoop()

if __name__ == "__main__":
    main()
