from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

# Parámetros de la ventana y el ángulo de vista
window_width, window_height = 800, 600

def init():
    glClearColor(0.53, 0.81, 0.98, 1.0)  # Color de fondo celeste
    glEnable(GL_DEPTH_TEST)

def draw_wall(x, y, z, width, height, color=(0.5, 0.5, 0.5)):
    """Función para dibujar una pared simple."""
    glColor3fv(color)
    glBegin(GL_QUADS)
    glVertex3f(x, y, z)
    glVertex3f(x + width, y, z)
    glVertex3f(x + width, y + height, z)
    glVertex3f(x, y + height, z)
    glEnd()

def draw_door(x, y, z, width, height, color=(0, 0, 1)):
    """Función para dibujar una puerta o ventana."""
    glColor3fv(color)
    glBegin(GL_QUADS)
    glVertex3f(x, y, z)
    glVertex3f(x + width, y, z)
    glVertex3f(x + width, y + height, z)
    glVertex3f(x, y + height, z)
    glEnd()

def draw_base():
    """Función para dibujar la base."""
    glColor3f(0.1, 0.1, 0.1)  # Color de la base (negra)
    glBegin(GL_QUADS)
    glVertex3f(-2, 0, -2)
    glVertex3f(2, 0, -2)
    glVertex3f(2, 0, 2)
    glVertex3f(-2, 0, 2)
    glEnd()

def draw_roof():
    """Función para dibujar el techo."""
    glColor3f(0.5, 0.2, 0.2)  # Color del techo (rojo oscuro)
    glBegin(GL_QUADS)
    glVertex3f(-1.5, 1.5, 0)
    glVertex3f(1.5, 1.5, 0)
    glVertex3f(1.5, 1.5, -1.5)
    glVertex3f(-1.5, 1.5, -1.5)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(2, 2, 5, 0, 0, 0, 0, 1, 0)

    # Dibujar la base
    draw_base()

    # Dibujar fachada frontal
    draw_wall(-1.5, 0, 0, 3, 1.5)          # Pared de la fachada principal
    draw_door(-0.9, 0, 0.01, 0.8, 1)       # Puerta izquierda centrada
    draw_door(0.1, 0, 0.01, 0.8, 1)        # Puerta derecha centrada

    # Dibujar paredes laterales
    draw_wall(-1.5, 0, -1.5, 0.1, 1.5)     # Lateral izquierdo
    draw_wall(1.4, 0, -1.5, 0.1, 1.5)      # Lateral derecho

    # Dibujar pared trasera
    draw_wall(-1.5, 0, -1.5, 3, 1.5)       # Pared trasera sin puertas

    # Dibujar techo
    draw_roof()

    glutSwapBuffers()

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, float(width) / float(height), 1, 50)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(window_width, window_height)
    glutCreateWindow(b"Cafeteria Facade 3D")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()

if __name__ == "__main__":
    main()
