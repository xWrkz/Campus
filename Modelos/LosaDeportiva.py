from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

camera_angle_x = 0
camera_angle_y = 0
camera_distance = 40
mouse_x, mouse_y = 0, 0
mouse_left_down = False

def init():
    glClearColor(0.5, 0.7, 0.9, 1.0)  # Fondo azul claro
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

def draw_half_circle(radius, segments):
    glLineWidth(2.0)  # Grosor de 3 píxeles para el contorno
    # Dibujar el contorno del medio círculo cortado horizontalmente
    glColor3f(1.0, 1.0, 1.0)  # Color negro para el contorno
    glBegin(GL_LINE_STRIP)  # Usar LINE_STRIP para un medio círculo
    for i in range(segments + 1):  # +1 para cerrar el arco
        angle = math.pi * i / segments  # Medio círculo (180 grados)
        x = radius * math.sin(angle)  # Usar seno para el corte horizontal
        y = radius * math.cos(angle)  # Usar coseno para el corte horizontal
        glVertex2f(x, y)
    glEnd()

def draw_circle(radius, segments):
    glLineWidth(3.0)  # Grosor de 3 píxeles para el contorno
    glBegin(GL_LINE_LOOP)  # Usar LINE_LOOP para el contorno
    for i in range(segments):
        angle = 2 * math.pi * i / segments  # Calcular el ángulo
        x = radius * math.cos(angle)  # Coordenada X
        y = radius * math.sin(angle)  # Coordenada Y
        glVertex2f(x, y)  # Añadir vértice
    glEnd()

def draw_basket():
    # Dibujar el soporte de la canasta
    glColor3f(1.0, 1.0, 0.0)  # Color amarillo para el soporte
    glPushMatrix()
    glTranslatef(0.0, 1.5, 0.0)  # Altura del soporte
    glScalef(0.1, 3.0, 0.1)  # Escalar el soporte (ancho, alto, profundo)
    glutSolidCube(1)  # Dibuja un cubo (que se ha escalado a un prisma)
    glPopMatrix()

    # Dibujar el aro de la canasta
    glColor3f(1.0, 1.0, 0.0)  # Color amarillo para el aro
    glPushMatrix()
    glTranslatef(0.0, 3.5, 0.0)  # Altura del aro
    glTranslatef(0.5, 0.0, 0.0)  # Mueve el aro hacia adelante (ajusta el valor según sea necesario)
    glRotatef(90, 1, 0, 0)  # Girar para hacer un círculo
    glutSolidTorus(0.1, 0.3, 20, 20)  # Aro
    glPopMatrix()


    # Dibujar el cubo y prisma negros
    draw_black_cubes_and_pyramid()  # Llama a la función para dibujar el cubo y prisma

def draw_backboard(x_position):
    # Dibujar un cuadrado blanco detrás del aro
    glColor3f(1.0, 1.0, 1.0)  # Color blanco
    glPushMatrix()
    glTranslatef(x_position, 4.0, 0.0)  # Ajustar la posición detrás del aro
    glRotatef(90, 0.0, 1.0, 0.0)  # Rotar 90 grados alrededor del eje Y
    glScalef(1.5, 1.0, 0.1)  # Tamaño del cuadrado
    glutSolidCube(1)  # Dibujar el cuadrado
    glPopMatrix()

def draw_walls():
    # Color azul medio grisáceo para las paredes
    glColor3f(0.5, 0.6, 0.7)

    # Actualizar posiciones y escalas de las paredes
    wall_positions = [
        (0.0, 1.0, -15.0),  # Pared trasera
        (0.0, 1.0, 8.0),    # Pared delantera (ajustada para coincidir con el piso)
        (-18.0, 1.0, -3.5),  # Pared izquierda (ajustada a la mitad de la altura del piso)
        (18.0, 1.0, -5)    # Pared derecha (ajustada a la mitad de la altura del piso)
    ]
    wall_scales = [
        (36.0, 2.0, 0.4),   # Pared trasera
        (36.0, 2.0, 0.4),   # Pared delantera (ajustada)
        (0.4, 2.0, 23.0),   # Pared izquierda
        (0.4, 2.0, 20.0)    # Pared derecha
    ]
    
    for position, scale in zip(wall_positions, wall_scales):
        glPushMatrix()
        glTranslatef(*position)
        glScalef(*scale)
        glutSolidCube(1)
        glPopMatrix()


def draw_lines():
    glLineWidth(3.0)  # Grosor de 3 píxeles para el contorno
    glColor3f(1.0, 1.0, 1.0)  # Color blanco para las líneas
    glBegin(GL_LINES)

    # Líneas desde los extremos del contorno hacia el lado opuesto de las canastas
    glVertex3f(0, 0.0, 7.0)  # Punto inicial en el lado izquierdo del rectángulo
    glVertex3f(0, 0.0, 2.0)  # Extensión hacia abajo, lejos del rectángulo

    glVertex3f(0, 0.0, -2.0)   # Punto inicial en el lado derecho del rectángulo
    glVertex3f(0, 0.0, -7.0)  # Extensión hacia abajo, lejos del rectángulo

    glEnd()

def draw_floor():
    # Dibujar el piso rectangular
    glColor3f(0.5, 0.5, 0.5)  # Color gris
    glBegin(GL_QUADS)
    glVertex3f(-18.0, 0.0, -15.0)  # Ajusta estos valores para el tamaño rectangular
    glVertex3f(18.0, 0.0, -15.0)
    glVertex3f(18.0, 0.0, 8.0)
    glVertex3f(-18.0, 0.0, 8.0)
    glEnd()

def draw_rectangle_outline():
    glLineWidth(3.0)  # Grosor de 3 píxeles para el contorno
    glColor3f(1.0, 1.0, 0.0)  # Color blanco para el contorno
    glBegin(GL_LINE_LOOP)  # Usar LINE_LOOP para cerrar el contorno
    glVertex3f(-12.0, 0.0, -4.0)  # Esquina inferior izquierda
    glVertex3f(12.0, 0.0, -4.0)   # Esquina inferior derecha
    glVertex3f(12.0, 0.0, 4.0)    # Esquina superior derecha
    glVertex3f(-12.0, 0.0, 4.0)   # Esquina superior izquierda
    glEnd()

def draw_rectangle_outline2():
    glLineWidth(4.0)  # Grosor de 3 píxeles para el contorno
    glColor3f(1.0, 1.0, 1.0)  # Color blanco para el contorno
    glBegin(GL_LINE_LOOP)  # Usar LINE_LOOP para cerrar el contorno
    glVertex3f(-14.5, 0.0, -7.0)  # Esquina inferior izquierda
    glVertex3f(14.5, 0.0, -7.0)   # Esquina inferior derecha
    glVertex3f(14.5, 0.0, 7.0)    # Esquina superior derecha
    glVertex3f(-14.5, 0.0, 7.0)   # Esquina superior izquierda
    glEnd()

def draw_black_cubes_and_pyramid():
    # Color negro para el cubo y la pirámide
    glColor3f(0.0, 0.0, 0.0)  # Color negro

    # Dibuja el cubo en la base del soporte del aro
    glPushMatrix()
    glTranslatef(0.0, 0.5, 0.0)  # Posición del cubo (ajusta según sea necesario)
    glutSolidCube(1.0)  # Tamaño del cubo
    glPopMatrix()

    # Dibuja una pirámide encima del cubo
    glBegin(GL_TRIANGLES)

    # Cara frontal
    glVertex3f(0.0, 2.0, 0.0)  # Punta de la pirámide (ajustada a la altura del cubo más la altura de la pirámide)
    glVertex3f(-0.5, 1.0, -0.5)  # Esquina inferior izquierda
    glVertex3f(0.5, 1.0, -0.5)  # Esquina inferior derecha

    # Cara derecha
    glVertex3f(0.0, 2.0, 0.0)
    glVertex3f(0.5, 1.0, -0.5)
    glVertex3f(0.5, 1.0, 0.5)  # Esquina inferior derecha

    # Cara trasera
    glVertex3f(0.0, 2.0, 0.0)
    glVertex3f(0.5, 1.0, 0.5)
    glVertex3f(-0.5, 1.0, 0.5)  # Esquina inferior izquierda

    # Cara izquierda
    glVertex3f(0.0, 2.0, 0.0)
    glVertex3f(-0.5, 1.0, 0.5)
    glVertex3f(-0.5, 1.0, -0.5)  # Esquina inferior izquierda

    glEnd()

    # Dibuja un cubo pequeño en la punta de la pirámide
    glColor3f(0.0, 0.0, 0.0)  # Color negro
    glPushMatrix()
    glTranslatef(0.0, 1.8, 0.0)  # Posición en la punta de la pirámide
    glutSolidCube(0.3)  # Tamaño del cubo pequeño, ajustado a 0.3
    glPopMatrix()

def draw_yellow_squares():
    # Color amarillo para los cuadrados
    square_size = 4.0  # Tamaño del cuadrado

    # Dibujar cuadrado a la izquierda
    glColor3f(1.0, 1.0, 0.0)  # Color amarillo
    glPushMatrix()
    glTranslatef(-12.5, 0.0, 0.0)  # Ajustar la posición de manera independiente
    glScalef(square_size, 0.1, square_size)  # Tamaño del cuadrado
    glutSolidCube(1)  # Dibujar el cuadrado
    glPopMatrix()

    # Dibujar cuadrado a la derecha
    glColor3f(1.0, 1.0, 0.0)  # Color amarillo
    glPushMatrix()
    glTranslatef(12.5, 0.0, 0.0)  # Ajustar la posición de manera independiente
    glScalef(square_size, 0.1, square_size)  # Tamaño del cuadrado
    glutSolidCube(1)  # Dibujar el cuadrado
    glPopMatrix()

def draw_stairs():
    # Dibujar la banqueta en forma de escalera del lado derecho
    stair_width = 7.5
    stair_depth = 0.5
    stair_height = 0.2
    num_steps = 5
    
    # Color de la banqueta
    glColor3f(1.0, 0.8, 0.0)  # Color amarillo

    for i in range(num_steps):
        glPushMatrix()
        # Ajustar la posición para que esté pegada a la pared derecha
        glTranslatef(0.0, 0.1+(i * stair_height),-12.7 -(i * stair_depth))  # Posición de cada escalón
        glScalef(stair_width, stair_height, stair_depth)  # Tamaño de cada escalón
        glutSolidCube(1)  # Dibujar el escalón
        glPopMatrix()

def draw_scene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Mover cámara
    glTranslatef(0.0, 0.0, -camera_distance)
    glRotatef(camera_angle_x, 1.0, 0.0, 0.0)
    glRotatef(camera_angle_y, 0.0, 1.0, 0.0)

    # Dibujar el piso
    draw_floor()

    # Dibujar paredes
    draw_walls()

    draw_rectangle_outline()
    draw_rectangle_outline2()
    draw_lines()

    glPushMatrix()
    glTranslatef(-16, 0.0, 0.0)  # Canasta izquierda
    draw_basket()
    draw_backboard(-0.1)  # Cuadrado blanco detrás
    glPopMatrix()

    glPushMatrix()
    glTranslatef(16, 0.0, 0.0)  # Canasta derecha
    draw_basket()
    draw_backboard(1)  # Cuadrado blanco detrás
    glPopMatrix()

    # Dibujar cuadrados amarillos debajo de los postes
    draw_yellow_squares()

    # Dibujar la banqueta
    draw_stairs()

    # Dibujar los medio círculos
    glPushMatrix()
    glTranslatef(10.5, 0.0, 0.0)  # Mover a la derecha
    glRotatef(90, 1.0, 0.0, 0.0)  # Poner el medio círculo en el plano horizontal 
    glRotatef(180, 0.0, 0.0, 1.0)
    draw_half_circle(1.5, 100)  # Dibujar el primer medio círculo
    glPopMatrix()

    # Segundo medio círculo en el centro
    glPushMatrix()
    glTranslatef(14.5, 0.1, 0.0)  # Mantener en el centro
    glRotatef(90, 1.0, 0.0, 0.0)  # Poner el medio círculo en el plano horizontal  
    glRotatef(180, 0.0, 0.0, 1.0)
    draw_half_circle(0.7, 100)  # Dibujar el segundo medio círculo
    glPopMatrix()

    # Tercer medio círculo a la izquierda
    glPushMatrix()
    glTranslatef(14.5, 0.0, 0.0)  # Mover a la izquierda
    glRotatef(90, 1.0, 0.0, 0.0)  # Poner el medio círculo en el plano horizontal
    glRotatef(180, 0.0, 0.0, 1.0)
    draw_half_circle(6, 100)  # Dibujar el tercer medio círculo
    glPopMatrix()
    
    # Dibujar los medio círculos
    glPushMatrix()
    glTranslatef(-10.5, 0.0, 0.0)  # Mover a la derecha
    glRotatef(90, 1.0, 0.0, 0.0)  # Poner el medio círculo en el plano horizontal 
    glRotatef(0, 0.0, 0.0, 1.0)
    draw_half_circle(1.5, 100)  # Dibujar el primer medio círculo
    glPopMatrix()

    # Segundo medio círculo en el centro
    glPushMatrix()
    glTranslatef(-14.5, 0.1, 0.0)  # Mantener en el centro
    glRotatef(90, 1.0, 0.0, 0.0)  # Poner el medio círculo en el plano horizontal  
    glRotatef(0, 0.0, 0.0, 1.0)
    draw_half_circle(0.7, 100)  # Dibujar el segundo medio círculo
    glPopMatrix()

    # Tercer medio círculo a la izquierda
    glPushMatrix()
    glTranslatef(-14.5, 0.0, 0.0)  # Mover a la izquierda
    glRotatef(90, 1.0, 0.0, 0.0)  # Poner el medio círculo en el plano horizontal
    glRotatef(0, 0.0, 0.0, 1.0)
    draw_half_circle(6, 100)  # Dibujar el tercer medio círculo
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0, 0.0, 0.0)  # Posición del círculo
    glRotatef(90, 1.0, 0.0, 0.0)
    glColor3f(1.0, 1.0, 1.0)  # Color rojo para el círculo
    draw_circle(2.0, 100)  # Dibujar un círculo con radio 2.0 y 100 segmentos
    glPopMatrix()

    glutSwapBuffers()  # Mostrar la escena

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

def keyboard(key, x, y):
    global camera_distance
    if key == b'w':
        camera_distance -= 1  # Mover hacia adelante
    elif key == b's':
        camera_distance += 1  # Mover hacia atrás
    glutPostRedisplay()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow("Cancha de Baloncesto")
    init()
    glutDisplayFunc(draw_scene)
    glutReshapeFunc(reshape)
    glutMouseFunc(mouse_button)
    glutMotionFunc(mouse_motion)
    glutKeyboardFunc(keyboard)  # Capturar entradas del teclado
    glutMainLoop()

if __name__ == "__main__":
    main()
