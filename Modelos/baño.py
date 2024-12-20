from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Variables de control para la cámara
cam_angle_x = 0.0
cam_angle_y = 0.0
cam_radius = 20.0
last_mouse_x = 0
last_mouse_y = 0
mouse_left_down = False

def init():
    glClearColor(0.5, 0.7, 1.0, 1.0)  # Cambiar el color de fondo a celeste
    glEnable(GL_DEPTH_TEST)

def draw_floor():
    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)  # Color blanco para el suelo

    # Definir las coordenadas del suelo como un rectángulo
    glVertex3f(-15.0, 0.0, -15.0)  # Aumentar tamaño
    glVertex3f( 15.0, 0.0, -15.0)  # Aumentar tamaño
    glVertex3f( 15.0, 0.0,  15.0)  # Aumentar tamaño
    glVertex3f(-15.0, 0.0,  15.0)  # Aumentar tamaño

    glEnd()

def draw_wall(x1, z1, x2, z2, height=4.0, color=(0.6, 0.8, 1.0)):  # Cambiar a celeste
    """Dibujar una pared entre dos puntos."""
    glColor3f(*color)
    glBegin(GL_QUADS)

    # Pared
    glVertex3f(x1, 0.0, z1)
    glVertex3f(x2, 0.0, z2)
    glVertex3f(x2, height, z2)
    glVertex3f(x1, height, z1)

    glEnd()

def draw_cube_room():
    """Dibujar el cubo que representa la sala."""
    # Dibujar las paredes del cubo
    draw_wall(-3.0, -3.0, 3.0, -3.0)  # Pared frontal (con la puerta)
    draw_wall(3.0, -3.0, 3.0, 3.0)    # Pared lateral derecha
    draw_wall(-3.0, -3.0, -3.0, 3.0)  # Pared lateral izquierda
    draw_wall(-3.0, 3.0, 3.0, 3.0)    # Pared trasera
    draw_wall(-3.0, 3.0, -3.0, -3.0, 0.05, color=(0.5, 0.3, 0.2))  # Suelo del cubo

def draw_internal_divisions():
    """Dibujar las divisiones internas para separar las partes."""
    # División para separar inodoros del pasillo
    draw_wall(-3.0, 0.5, 3.0, 0.5)  # Aumentar tamaño

def draw_toilets():
    """Dibujar 3 inodoros en la primera parte del cubo como rectángulos 3D negros."""
    glColor3f(0.0, 0.0, 0.0)  # Color negro para los inodoros
    for i in range(3):
        x_offset = -2.0 + i * 2.0  # Aumentar espaciado
        glPushMatrix()
        glTranslatef(x_offset, 0.5, 2.0)  # Posicionar los inodoros (encima del suelo)
        glScalef(0.75, 1.5, 0.75)  # Aumentar tamaño
        glutSolidCube(1.0)  # Dibujar el inodoro como un cubo escalado
        glPopMatrix()

def draw_sinks():
    """Dibujar tres lavaderos en el cubo."""
    glColor3f(0.8, 0.8, 0.8)  # Color gris claro para los lavaderos
    for i in range(3):
        x_offset = -2.0 + i * 2.0  # Aumentar espaciado
        glPushMatrix()
        glTranslatef(x_offset, 0.5, -2.0)  # Posicionar los lavaderos encima del suelo
        glScalef(1.5, 0.75, 0.75)  # Aumentar tamaño
        glutSolidCube(1.0)  # Dibujar el lavadero como un cubo escalado
        glPopMatrix()

def display():
    global cam_angle_x, cam_angle_y, cam_radius
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Convertir ángulos de la cámara a coordenadas cartesianas
    cam_x = cam_radius * math.sin(math.radians(cam_angle_x)) * math.cos(math.radians(cam_angle_y))
    cam_y = cam_radius * math.sin(math.radians(cam_angle_y))
    cam_z = cam_radius * math.cos(math.radians(cam_angle_x)) * math.cos(math.radians(cam_angle_y))

    # Definir la vista de la cámara
    gluLookAt(cam_x, cam_y, cam_z,   # Posición de la cámara
              0.0, 0.0, 0.0,        # Hacia donde mira la cámara (el origen)
              0.0, 1.0, 0.0)        # Vector "arriba"

    draw_floor()           # Dibujar el suelo
    draw_cube_room()       # Dibujar el cubo principal
    draw_internal_divisions()  # Dibujar las divisiones internas
    draw_toilets()         # Dibujar los inodoros como rectángulos negros
    draw_sinks()           # Dibujar tres lavaderos en color gris claro

    glutSwapBuffers()

def reshape(w, h):
    if h == 0:
        h = 1
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, w / h, 1.0, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def mouse_motion(x, y):
    global last_mouse_x, last_mouse_y, cam_angle_x, cam_angle_y, mouse_left_down

    if mouse_left_down:
        dx = x - last_mouse_x
        dy = y - last_mouse_y
        cam_angle_x += dx * 0.2
        cam_angle_y += dy * 0.2
        cam_angle_y = max(-89.0, min(89.0, cam_angle_y))

        last_mouse_x = x
        last_mouse_y = y

    glutPostRedisplay()

def mouse_button(button, state, x, y):
    global last_mouse_x, last_mouse_y, mouse_left_down
    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            mouse_left_down = True
            last_mouse_x = x
            last_mouse_y = y
        elif state == GLUT_UP:
            mouse_left_down = False

def mouse_wheel(button, direction, x, y):
    global cam_radius
    if direction > 0:
        cam_radius -= 1.0  # Acercar
    elif direction < 0:
        cam_radius += 1.0  # Alejar
    cam_radius = max(5.0, min(cam_radius, 50.0))  # Limitar el zoom
    glutPostRedisplay()

# Iniciacion del codigo
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow("Baño Público en 3D con OpenGL")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMotionFunc(mouse_motion)
    glutMouseFunc(mouse_button)
    glutMouseWheelFunc(mouse_wheel)   # Función de la rueda del mouse
    glutMainLoop()

if __name__ == "__main__":
    main()


