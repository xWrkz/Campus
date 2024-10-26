from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

# Tamaño del suelo
tamaño_suelo = 40
# Posición inicial de la cámara
posicion_camara = [0, 2, -15]
angulo_y = 0
movimiento_adelante_atras = 0
movimiento_izquierda_derecha = 0

# Variables para el ratón
mouse_prev_x = 0
mouse_prev_y = 0
is_mouse_dragging = False

def dibujar_suelo():
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_QUADS)
    glVertex3f(-tamaño_suelo, 0, -tamaño_suelo)
    glVertex3f(tamaño_suelo, 0, -tamaño_suelo)
    glVertex3f(tamaño_suelo, 0, tamaño_suelo)
    glVertex3f(-tamaño_suelo, 0, tamaño_suelo)
    glEnd()

def dibujar_cubo_hueco():
    glColor3f(0.5, 0.5, 0.5)
    
    # Dimensiones de la habitación
    width = 30
    height = 8
    depth = 30

    # Paredes
    # Frente
    glBegin(GL_QUADS)
    glVertex3f(-width/2, 0, depth/2)
    glVertex3f(width/2, 0, depth/2)
    glVertex3f(width/2, height, depth/2)
    glVertex3f(-width/2, height, depth/2)
    glEnd()

    # Espalda
    glBegin(GL_QUADS)
    glVertex3f(-width/2, 0, -depth/2)
    glVertex3f(width/2, 0, -depth/2)
    glVertex3f(width/2, height, -depth/2)
    glVertex3f(-width/2, height, -depth/2)
    glEnd()

    # Lado izquierdo
    glBegin(GL_QUADS)
    glVertex3f(-width/2, 0, depth/2)
    glVertex3f(-width/2, 0, -depth/2)
    glVertex3f(-width/2, height, -depth/2)
    glVertex3f(-width/2, height, depth/2)
    glEnd()

    # Lado derecho
    glBegin(GL_QUADS)
    glVertex3f(width/2, 0, depth/2)
    glVertex3f(width/2, 0, -depth/2)
    glVertex3f(width/2, height, -depth/2)
    glVertex3f(width/2, height, depth/2)
    glEnd()


def dibujar_mesa():
    glColor3f(0.6, 0.3, 0.1)
    glBegin(GL_QUADS)
    glVertex3f(-1.5, 1, -1.5)
    glVertex3f(1.5, 1, -1.5)
    glVertex3f(1.5, 1, 1.5)
    glVertex3f(-1.5, 1, 1.5)
    glEnd()
    glColor3f(0.4, 0.2, 0.1)
    for x in [-1.4, 1.4]:
        for z in [-1.4, 1.4]:
            glBegin(GL_QUADS)
            glVertex3f(x, 0, z)
            glVertex3f(x + 0.2, 0, z)
            glVertex3f(x + 0.2, 1, z)
            glVertex3f(x, 1, z)
            glEnd()

def dibujar_puerta():
    glColor3f(0.8, 0.5, 0.3)
    glBegin(GL_QUADS)
    glVertex3f(-0.5, 0, 2)
    glVertex3f(0.5, 0, 2)
    glVertex3f(0.5, 2, 2)
    glVertex3f(-0.5, 2, 2)
    glEnd()

def mostrar():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Calcular la dirección de la cámara
    gluLookAt(posicion_camara[0], posicion_camara[1], posicion_camara[2],
              posicion_camara[0] + math.sin(math.radians(angulo_y)), 
              posicion_camara[1], 
              posicion_camara[2] + math.cos(math.radians(angulo_y)),
              0, 1, 0)

    dibujar_suelo()
    dibujar_cubo_hueco()
    dibujar_mesa()
    dibujar_puerta()
    glutSwapBuffers()

def cambiar_tamaño(width, height):
    if height == 0:
        height = 1
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, float(width) / height, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def manejar_teclado(tecla, x, y):
    global movimiento_adelante_atras, movimiento_izquierda_derecha

    if tecla == b"w":  # Avanzar
        movimiento_adelante_atras = 1
    elif tecla == b's':  # Retroceder
        movimiento_adelante_atras = -1
    elif tecla == b'a':  # Girar a la izquierda
        movimiento_izquierda_derecha = 1
    elif tecla == b'd':  # Girar a la derecha
        movimiento_izquierda_derecha = -1

def manejar_teclado_suelto(tecla, x, y):
    global movimiento_adelante_atras, movimiento_izquierda_derecha

    if tecla == b'w' or tecla == b's':
        movimiento_adelante_atras = 0
    elif tecla == b'a' or tecla == b'd':
        movimiento_izquierda_derecha = 0

def mouse_motion(x, y):
    global mouse_prev_x, mouse_prev_y, angulo_y, is_mouse_dragging
    if is_mouse_dragging:
        dx = x - mouse_prev_x
        angulo_y += dx * 0.1
    mouse_prev_x = x
    mouse_prev_y = y
    glutPostRedisplay()

def mouse_button(button, state, x, y):
    global is_mouse_dragging, mouse_prev_x, mouse_prev_y
    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            is_mouse_dragging = True
            mouse_prev_x = x
            mouse_prev_y = y
        else:
            is_mouse_dragging = False

def rueda_raton(button, direction, x, y):
    global posicion_camara
    if direction > 0:  # Acercar
        posicion_camara[1] += 1.0
    elif direction < 0:  # Alejar
        posicion_camara[1] -= 1.0
    glutPostRedisplay()

def actualizar_posicion():
    global posicion_camara, movimiento_adelante_atras, movimiento_izquierda_derecha

    # Movimiento adelante/atras
    if movimiento_adelante_atras == 1:
        posicion_camara[0] += math.sin(math.radians(angulo_y)) * 0.05
        posicion_camara[2] += math.cos(math.radians(angulo_y)) * 0.05
    elif movimiento_adelante_atras == -1:
        posicion_camara[0] -= math.sin(math.radians(angulo_y)) * 0.05
        posicion_camara[2] -= math.cos(math.radians(angulo_y)) * 0.05

    # Movimiento izquierda/derecha
    if movimiento_izquierda_derecha == 1:
        posicion_camara[0] += math.sin(math.radians(angulo_y + 90)) * 0.05
        posicion_camara[2] += math.cos(math.radians(angulo_y + 90)) * 0.05
    elif movimiento_izquierda_derecha == -1:
        posicion_camara[0] += math.sin(math.radians(angulo_y - 90)) * 0.05
        posicion_camara[2] += math.cos(math.radians(angulo_y - 90)) * 0.05

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b'3D Biblioteca')
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.1, 0.1, 0.1, 1)
    glutDisplayFunc(mostrar)
    glutReshapeFunc(cambiar_tamaño)
    glutKeyboardFunc(manejar_teclado)
    glutKeyboardUpFunc(manejar_teclado_suelto)
    glutMotionFunc(mouse_motion)
    glutMouseFunc(mouse_button)
    glutMouseWheelFunc(rueda_raton)
    glutIdleFunc(lambda: [actualizar_posicion(), mostrar()])
    glutMainLoop()

if __name__ == "__main__":
    main()
