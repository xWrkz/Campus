from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random
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
    glVertex3f(13 - 0.5, 0, depth/2)  # Corte para la puerta
    glVertex3f(13 - 0.5, height, depth/2)  # Corte para la puerta
    glVertex3f(-width/2, height, depth/2)
    glEnd()

    glBegin(GL_QUADS)
    glVertex3f(15 - 1.5, 0, depth/2)  # Esquina inferior izquierda de la puerta
    glVertex3f(15, 0, 15)  # Esquina inferior derecha de la puerta
    glVertex3f(15, height, 15)  # Esquina superior derecha de la puerta
    glVertex3f(15 - 1.5, height, depth/2)  # Esquina superior izquierda de la puerta
    glEnd()

    glBegin(GL_QUADS)
    glVertex3f(15 - 3, 2, depth/2)  # Esquina inferior izquierda de la puerta
    glVertex3f(15, 2, 15)  # Esquina inferior derecha de la puerta
    glVertex3f(15, height, 15)  # Esquina superior derecha de la puerta
    glVertex3f(15 - 3, height, depth/2)  # Esquina superior izquierda de la puerta
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

def dibujar_pared(x, y, z):
    glTranslatef(x, y, z)
    glColor3f(0.5, 0.5, 0.5)  # Color de la pared
    glBegin(GL_QUADS)
    glVertex3f(-5, 0, 0.1)  # Esquina inferior izquierda
    glVertex3f(5, 0, 0.1)   # Esquina inferior derecha
    glVertex3f(5, 8, 0.1)   # Esquina superior derecha
    glVertex3f(-5, 8, 0.1)  # Esquina superior izquierda
    glEnd()


def dibujar_mesa():
    glColor3f(0.6, 0.3, 0.1)
    largo = 2.0
    ancho = 5.0
    
    # Posiciona la mesa en la esquina izquierda
    x_offset = -11  # Ajusta este valor según sea necesario
    z_offset = 10  # Ajusta este valor para colocar la mesa en la dirección correcta

    # Dibuja la parte superior de la mesa
    glBegin(GL_QUADS)
    glVertex3f(x_offset + largo / 2, 1, z_offset - ancho / 2)
    glVertex3f(x_offset - largo / 2, 1, z_offset - ancho / 2)
    glVertex3f(x_offset - largo / 2, 1, z_offset + ancho / 2)
    glVertex3f(x_offset + largo / 2, 1, z_offset + ancho / 2)
    glEnd()
    
    # Color de las patas
    glColor3f(0.4, 0.2, 0.1)
    for x in [x_offset - largo / 2 + 0.1, x_offset + largo / 2 - 0.1]:
        for z in [z_offset - ancho / 2 + 0.1, z_offset + ancho / 2 - 0.1]:
            glBegin(GL_QUADS)
            glVertex3f(x, 0, z)
            glVertex3f(x + 0.2, 0, z)
            glVertex3f(x + 0.2, 1, z)
            glVertex3f(x, 1, z)
            glEnd()



def dibujar_puerta():
    glColor3f(0.8, 0.5, 0.3)
    glBegin(GL_QUADS)
    glVertex3f(13-0.5, 0, 15)
    glVertex3f(13+0.5, 0, 15)
    glVertex3f(13+0.5, 2, 15)
    glVertex3f(13-0.5, 2, 15)
    glEnd()

def dibujar_estanteria(x, z):
    glColor3f(0.6, 0.3, 0.1)  # Color de la estantería

    # Dimensiones de la estantería
    ancho = 2
    alto = 3
    profundidad = 0.2

    # Dibuja el cuerpo de la estantería
    glBegin(GL_QUADS)
    # Parte frontal
    glVertex3f(x - ancho, 0, z + profundidad)
    glVertex3f(x + ancho, 0, z + profundidad)
    glVertex3f(x + ancho, alto, z + profundidad)
    glVertex3f(x - ancho, alto, z + profundidad)
    glEnd()

    # Lados
    glBegin(GL_QUADS)
    # Lado izquierdo
    glVertex3f(x - ancho, 0, z + profundidad)
    glVertex3f(x - ancho, 0, z - profundidad)
    glVertex3f(x - ancho, alto, z - profundidad)
    glVertex3f(x - ancho, alto, z + profundidad)
    
    # Lado derecho
    glVertex3f(x + ancho, 0, z + profundidad)
    glVertex3f(x + ancho, 0, z - profundidad)
    glVertex3f(x + ancho, alto, z - profundidad)
    glVertex3f(x + ancho, alto, z + profundidad)
    glEnd()

    # Parte trasera
    glBegin(GL_QUADS)
    glVertex3f(x - ancho, 0, z - profundidad)
    glVertex3f(x + ancho, 0, z - profundidad)
    glVertex3f(x + ancho, alto, z - profundidad)
    glVertex3f(x - ancho, alto, z - profundidad)
    glEnd()

colores_libros = [
    (0.8, 0.0, 0.0),  # Rojo
    (0.0, 0.8, 0.0),  # Verde
    (0.0, 0.0, 0.8),  # Azul
    (0.8, 0.8, 0.0),  # Amarillo
    (0.8, 0.5, 0.5),  # Rosa
]

def dibujar_libro(x, y, z, color):
    glColor3f(*color)  # Color del libro
    glBegin(GL_QUADS)
    glVertex3f(x - 0.1, y, z)
    glVertex3f(x + 0.1, y, z)
    glVertex3f(x + 0.1, y + 0.3, z)
    glVertex3f(x - 0.1, y + 0.3, z)
    glEnd()

posiciones_libros = []
# Generar posiciones aleatorias solo una vez
def generar_posiciones_libros(x, y, z):
    global posiciones_libros
    posiciones_libros = []  # Limpiar la lista de posiciones
    offset = 0.26  # Espacio entre libros
    for i in range(5):  # Supongamos que queremos 5 libros
        color = random.choice(colores_libros)
        libro_x = x + random.uniform(-1.25, 1.25)  # Genera una posición aleatoria
        posiciones_libros.append((libro_x, y + 0.2 + i * offset, z - 0.1, color))

def dibujar_libros_en_estanteria():
    for libro_x, libro_y, libro_z, color in posiciones_libros:
        dibujar_libro(libro_x, libro_y, libro_z, color)

def dibujar_silla(x, z):
    glColor3f(0.4, 0.2, 0.1)
    
    # Dibuja el asiento de la silla
    glBegin(GL_QUADS)
    glVertex3f(x - 0.3, 1, z - 0.3)  # Asiento
    glVertex3f(x + 0.3, 1, z - 0.3)
    glVertex3f(x + 0.3, 1, z + 0.3)
    glVertex3f(x - 0.3, 1, z + 0.3)
    glEnd()
    
    # Dibuja las patas de la silla
    glBegin(GL_QUADS)
    # Parte frontal izquierda
    glVertex3f(x - 0.3, 0, z - 0.3)
    glVertex3f(x - 0.2, 0, z - 0.3)
    glVertex3f(x - 0.2, 1, z - 0.3)
    glVertex3f(x - 0.3, 1, z - 0.3)
    
    # Parte frontal derecha
    glVertex3f(x + 0.3, 0, z - 0.3)
    glVertex3f(x + 0.2, 0, z - 0.3)
    glVertex3f(x + 0.2, 1, z - 0.3)
    glVertex3f(x + 0.3, 1, z - 0.3)

    # Parte trasera izquierda
    glVertex3f(x - 0.3, 0, z + 0.3)
    glVertex3f(x - 0.2, 0, z + 0.3)
    glVertex3f(x - 0.2, 1, z + 0.3)
    glVertex3f(x - 0.3, 1, z + 0.3)

    # Parte trasera derecha
    glVertex3f(x + 0.3, 0, z + 0.3)
    glVertex3f(x + 0.2, 0, z + 0.3)
    glVertex3f(x + 0.2, 1, z + 0.3)
    glVertex3f(x + 0.3, 1, z + 0.3)
    glEnd()

    # Dibuja el respaldo, orientado hacia la mesa
    glBegin(GL_QUADS)
    glColor3f(0.5, 0.3, 0.1)  # Color del respaldo
    glVertex3f(x - 0.3, 1, z + 0.3)  # Inferior izquierda
    glVertex3f(x + 0.3, 1, z + 0.3)  # Inferior derecha
    glVertex3f(x + 0.3, 2, z + 0.3)  # Superior derecha
    glVertex3f(x - 0.3, 2, z + 0.3)  # Superior izquierda
    glEnd()


def dibujar_sillas():
    # Posiciones de las sillas alrededor de la mesa
    posiciones = [
        (-9, 2.5, 11),  # Izquierda frontal
        (-9, 2.5, 9),   # Izquierda trasera
        (-13, 2.5, 11),   # Derecha frontal
        (-13, 2.5, 9),    # Derecha trasera
        (-11, 2.5, 13),      # Frente
        (-11, 2.5, 6)      # Espalda
    ]

    for (x, y, z) in posiciones:
        dibujar_silla(x, z)

def mostrar():
    global posiciones_libros
    

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
    dibujar_sillas()
    # Agregar la estantería de libros
    glPushMatrix() 
    glRotatef(90, 0, 1, 0)
    dibujar_estanteria(-9, 10.80)  # Ubicación de la estantería
    generar_posiciones_libros(-9, 0, 10.68)
    dibujar_libros_en_estanteria()
    glPopMatrix()
    #------------------------------
    glPushMatrix() 
    glRotatef(90, 0, 1, 0)
    dibujar_estanteria(-9, 6.3)  # Ubicación de la estantería
    generar_posiciones_libros(-9, 0, 6.18)
    dibujar_libros_en_estanteria()
    glPopMatrix()
    #--------------------------
    glPushMatrix() 
    glRotatef(90, 0, 1, 0)
    dibujar_estanteria(-9, 1.7)  # Ubicación de la estantería
    generar_posiciones_libros(-9, 0, 1.58)
    dibujar_libros_en_estanteria()
    glPopMatrix()
    #----------------------------
    glPushMatrix() 
    glRotatef(90, 0, 1, 0)
    dibujar_estanteria(-9, -2.8)  # Ubicación de la estantería
    generar_posiciones_libros(-9, 0, -2.92)
    dibujar_libros_en_estanteria()
    glPopMatrix()
    #----------------------------
    glPushMatrix() 
    glRotatef(270, 0, 1, 0)
    dibujar_estanteria(9, 6.80)  # Ubicación de la estantería
    generar_posiciones_libros(9, 0, 6.68)
    dibujar_libros_en_estanteria()
    glPopMatrix()
    #----------------------------
    glPushMatrix() 
    glRotatef(270, 0, 1, 0)
    dibujar_estanteria(9, 2.30)  # Ubicación de la estantería
    generar_posiciones_libros(9, 0, 2.18)
    dibujar_libros_en_estanteria()
    glPopMatrix()
    #----------------------------
    glPushMatrix() 
    glRotatef(270, 0, 1, 0)
    dibujar_estanteria(9, -2.30)  # Ubicación de la estantería
    generar_posiciones_libros(9, 0, -2.42)
    dibujar_libros_en_estanteria()
    glPopMatrix()
    #--------------------------
    glPushMatrix() 
    glRotatef(270, 0, 1, 0)
    dibujar_estanteria(9, -6.80)  # Ubicación de la estantería
    generar_posiciones_libros(9, 0, -6.92)
    dibujar_libros_en_estanteria()
    glPopMatrix()
    #-------------------
    glPushMatrix() 
    glRotatef(90, 0, 1, 0)
    dibujar_pared(-10,0,11)
    glPopMatrix()
    #---------------------
    glPushMatrix() 
    glRotatef(90, 0, 1, 0)
    dibujar_pared(-10,0,6.45)
    glPopMatrix()
    #-------------------
    glPushMatrix() 
    glRotatef(90, 0, 1, 0)
    dibujar_pared(-10,0,1.90)
    glPopMatrix()
    #------------------
    glPushMatrix() 
    glRotatef(90, 0, 1, 0)
    dibujar_pared(-10,0,-2.65)
    glPopMatrix()
    #---------------------
    glPushMatrix() 
    glRotatef(90, 0, 1, 0)
    dibujar_pared(-10,0,-7.2)
    glPopMatrix()
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
