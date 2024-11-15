from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Obstáculos definidos
obstacles = [
    [2, 0, -10, 1],
    [-3, 0, -12, 1.5],
    [0, 0, -15, 2]
]

camera_pos = [0, 0, 0]
destination = [0, 0, -10]

def draw_obstacles():
    glColor3f(1, 0, 0)  # Rojo
    for obs in obstacles:
        x, y, z, size = obs
        glPushMatrix()
        glTranslatef(x, y, z)
        glutWireCube(size)
        glPopMatrix()

def draw_path(camera_pos, destination):
    glColor3f(0, 1, 0)  # Verde
    glBegin(GL_LINES)
    glVertex3fv(camera_pos)
    glVertex3fv(destination)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(camera_pos[0], camera_pos[1], camera_pos[2] + 5,  # Cámara
              0, 0, -10,  # Punto de enfoque
              0, 1, 0)  # Arriba
    draw_obstacles()
    draw_path(camera_pos, destination)
    glutSwapBuffers()

def keyboard(key, x, y):
    global destination
    step = 0.5
    if key == b'w':  # Adelante
        destination[2] += step
    elif key == b's':  # Atrás
        destination[2] -= step
    elif key == b'a':  # Izquierda
        destination[0] -= step
    elif key == b'd':  # Derecha
        destination[0] += step
    elif key == b'q':  # Arriba
        destination[1] += step
    elif key == b'e':  # Abajo
        destination[1] -= step
    glutPostRedisplay()

def init():
    glClearColor(0.1, 0.1, 0.1, 1)  # Fondo oscuro
    glEnable(GL_DEPTH_TEST)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow("Sistema de Guía - PyOpenGL")
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    init()
    glutMainLoop()

if __name__ == "__main__":
    main()
