from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

width, height = 800, 600
camera_angle_x = 0  # Ángulo de rotación en el eje X
camera_angle_y = 0  # Ángulo de rotación en el eje Y
camera_distance = 5  # Distancia de la cámara al objeto

def init():
    glClearColor(0.53, 0.81, 0.98, 1)  # Cielo azul claro
    glEnable(GL_DEPTH_TEST)

def draw_building():
    # Estructura principal del edificio
    glPushMatrix()
    glTranslatef(0, 0, 0)  # Posición base
    glScalef(3, 1.5, 1)  # Escalar a las proporciones del edificio
    glColor3f(0.8, 0.8, 0.8)  # Color gris claro para el edificio
    glutSolidCube(1)
    glPopMatrix()

    # Cartel amarillo
    glPushMatrix()
    glTranslatef(0, 0.75, 0.52)  # Posicionar el cartel frente al edificio
    glScalef(2, 0.3, 0.1)  # Escalar el cartel amarillo
    glColor3f(1, 1, 0)  # Color amarillo para el cartel
    glutSolidCube(1)
    glPopMatrix()

    # Dibujar las ventanas (pequeños cubos en filas)
    for i in range(-2, 3):  # 5 columnas
        for j in range(0, 2):  # 2 filas
            glPushMatrix()
            glTranslatef(i * 0.6, j * 0.5 - 0.25, 0.51)  # Posicionar cada ventana
            glScalef(0.5, 0.25, 0.05)  # Escalar a tamaño de ventana
            glColor3f(0.3, 0.3, 0.3)  # Color gris oscuro para ventanas
            glutSolidCube(1)
            glPopMatrix()

    # Dibujar las rejas de entrada
    for i in range(-3, 4):  # 7 barras
        glPushMatrix()
        glTranslatef(i * 0.15, -0.65, 0.51)  # Espaciado entre barras
        glScalef(0.05, 0.5, 0.05)  # Barras verticales finas
        glColor3f(0, 0, 0)  # Color negro para las rejas
        glutSolidCube(1)
        glPopMatrix()

    # Escaleras a la derecha del edificio
    for i in range(5):  # 5 escalones
        glPushMatrix()
        glTranslatef(1.5, -0.75 + (i * 0.2), 0)  # Apilar escalones
        glScalef(0.5, 0.05, 0.3)  # Escalones largos y delgados
        glColor3f(0.7, 0.7, 0.7)  # Color gris metálico para las escaleras
        glutSolidCube(1)
        glPopMatrix()

    # Pasamanos de las escaleras
    glPushMatrix()
    glTranslatef(1.5, 0.25, 0)  # Pasamanos sobre las escaleras
    glScalef(0.05, 1, 0.05)  # Cilindro delgado y largo
    glColor3f(0.5, 0.5, 0.5)  # Color gris metálico
    glRotatef(90, 1, 0, 0)  # Rotar para orientarlo correctamente
    glutSolidCylinder(0.1, 1, 10, 10)
    glPopMatrix()

    # Elevador de vidrio
    glPushMatrix()
    glTranslatef(1.7, 0.5, 0)  # Posicionar el elevador a la derecha
    glScalef(0.2, 1, 0.2)  # Escalar a proporciones de elevador
    glColor4f(0.8, 0.8, 0.9, 0.6)  # Color gris claro con un poco de transparencia
    glutSolidCube(1)
    glPopMatrix()

def display():
    global camera_angle_x, camera_angle_y, camera_distance

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Calcular la posición de la cámara en base a los ángulos y la distancia
    camera_x = camera_distance * math.sin(math.radians(camera_angle_x)) * math.cos(math.radians(camera_angle_y))
    camera_y = camera_distance * math.sin(math.radians(camera_angle_y))
    camera_z = camera_distance * math.cos(math.radians(camera_angle_x)) * math.cos(math.radians(camera_angle_y))

    # Establecer la posición de la cámara
    gluLookAt(camera_x, camera_y, camera_z, 0, 0, 0, 0, 1, 0)

    draw_building()  # Dibujar el edificio

    glutSwapBuffers()

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, w/h, 0.1, 50)
    glMatrixMode(GL_MODELVIEW)

def keyboard(key, x, y):
    global camera_distance
    if key == b'\x1b':  # Tecla Escape
        glutLeaveMainLoop()
    elif key == b'w':  # Acercar (zoom in)
        camera_distance -= 0.5
    elif key == b's':  # Alejar (zoom out)
        camera_distance += 0.5

def special_keys(key, x, y):
    global camera_angle_x, camera_angle_y
    if key == GLUT_KEY_RIGHT:  # Rotar a la derecha
        camera_angle_x += 5
    elif key == GLUT_KEY_LEFT:  # Rotar a la izquierda
        camera_angle_x -= 5
    elif key == GLUT_KEY_UP:  # Rotar hacia arriba
        camera_angle_y += 5
        if camera_angle_y > 90:  # Limitar la rotación vertical
            camera_angle_y = 90
    elif key == GLUT_KEY_DOWN:  # Rotar hacia abajo
        camera_angle_y -= 5
        if camera_angle_y < -90:  # Limitar la rotación vertical
            camera_angle_y = -90

# Inicializar GLUT
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(width, height)
glutCreateWindow(b"3D Model - UPN Building with Camera Control")

# Inicializar OpenGL
init()

# Configurar funciones de visualización, redimensionamiento y teclado
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutKeyboardFunc(keyboard)
glutSpecialFunc(special_keys)
glutIdleFunc(display)

# Iniciar el bucle principal
glutMainLoop()
