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
    glClearColor(0.5, 0.7, 0.9, 1.0)  # Color de fondo
    glEnable(GL_DEPTH_TEST)

def draw_walls():
    glColor3f(0.0, 0.0, 0.0)  # Color de las paredes
    wall_positions = [
        (0.0, 1.0, -75.0),  # Pared frontal
        (20.0, 1.0, 40.0),  # Pared trasera
        (-70.0, 3.6, 40.0),  # Pared inclinada hacia arriba
        (-90.0, 6.2, -17.5), # Pared izquierda
        (90.0, 1.0, -17.5)   # Pared derecha
    ]
    wall_scales = [
        (180.0, 1.0, 1.0),   # Pared frontal
        (140.0, 1.0, 1.0),   # Pared trasera
        (40.0, 1.0, 1.0),    # Pared inclinada
        (1.0, 1.0, 116.0),   # Pared izquierda
        (1.0, 1.0, 116.0)    # Pared derecha
    ]
    
    for i, (position, scale) in enumerate(zip(wall_positions, wall_scales)):
        glPushMatrix()
        glTranslatef(*position)  # Posicionar la pared
        # Inclinación hacia arriba en el eje X solo para la pared en (-60.0, 1.0, 40.0)
        if position == (-70.0, 3.6, 40.0):
            glRotatef(-7.5, 0, 0, 1)  # Inclina 20 grados hacia arriba en el eje X 
        glScalef(*scale)         # Escalar la pared
        glutSolidCube(1)         # Dibujar el cubo que representa la pared
        glPopMatrix()

def draw_contorno_structure():
    glColor3f(0.0, 0.0, 0.0)  # Color del contorno negro

    # Posiciones y escalas de los segmentos del contorno del rectángulo
    contorno_positions = [
        (0.0, 0.1, -4.0),   # Segmento inferior
        (0.0, 0.1, 4.0),    # Segmento superior
        (-15.0, 0.1, 0.0),  # Segmento izquierdo
        (15.0, 0.1, 0.0)    # Segmento derecho
    ]
    contorno_scales = [
        (30.0, 0.7, 0.5),   # Escala del segmento inferior
        (30.0, 0.7, 0.5),   # Escala del segmento superior
        (0.5, 0.7, 8.5),    # Escala del segmento izquierdo
        (0.5, 0.7, 8.5)     # Escala del segmento derecho
    ]
    
    # Dibuja cada segmento del contorno
    for position, scale in zip(contorno_positions, contorno_scales):
        glPushMatrix()
        glTranslatef(*position)
        glScalef(*scale)
        glutSolidCube(1)  # Dibuja el cubo como segmento del contorno
        glPopMatrix()

def draw_centro_structure():
    glColor3f(0.0, 0.0, 0.0)  # Color negro

    # Definir posiciones y escalas para los segmentos del rectángulo central
    centro_positions = [
        (0.0, 0.1, -4.0),   # Segmento inferior
        (0.0, 0.1, 4.0),    # Segmento superior
        (-1.5, 0.1, 0.0),   # Segmento izquierdo
        (1.5, 0.1, 0.0)     # Segmento derecho
    ]
    centro_scales = [
        (3.0, 0.7, 0.5),    # Escala del segmento inferior
        (3.0, 0.7, 0.5),    # Escala del segmento superior
        (0.5, 0.7, 8.0),    # Escala del segmento izquierdo
        (0.5, 0.7, 8.0)     # Escala del segmento derecho
    ]

    # Dibuja cada segmento del rectángulo central
    for position, scale in zip(centro_positions, centro_scales):
        glPushMatrix()
        glTranslatef(*position)
        glScalef(*scale)
        glutSolidCube(1)  # Dibuja un cubo como segmento del rectángulo central
        glPopMatrix()

def draw_Soporte(height):
    glColor3f(0.0, 0.0, 0.0)  # Color del soporte
    glPushMatrix()
    glTranslatef(0.0, height / 1.5, 0.0)  # Posicionar el soporte
    glScalef(0.1, height, 0.1)  # Escalar el soporte en base a la altura
    glutSolidCube(1)  # Dibuja un cubo sólido como soporte
    glPopMatrix()

def draw_multiple_soportes(count, separation, height):
    for i in range(count):
        glPushMatrix()  # Guardar la matriz de transformación actual
        glTranslatef(i * separation, 0.0, 0.0)  # Separar cada soporte en el eje X
        draw_Soporte(height)  # Llamar a la función que dibuja un solo soporte con altura personalizada
        glPopMatrix()  # Restaurar la matriz de transformación

def draw_block(position, scale, color=(1.0, 1.0, 1.0)):  # Color blanco por defecto
    glColor3f(*color)  # Aplicar el color del bloque
    glPushMatrix()
    glTranslatef(*position)  # Posicionar el bloque
    glScalef(*scale)         # Escalar el bloque
    glutSolidCube(1)         # Dibuja un cubo sólido
    glPopMatrix()

def draw_rectangular_plane(position, scale):
    glColor3f(0.5, 0.5, 0.5)  # Color gris
    glPushMatrix()
    glTranslatef(*position)    # Posicionar el plano
    glScalef(*scale)           # Escalar el plano en X y Z
    glBegin(GL_QUADS)
    glVertex3f(-1.0, 0.0, -1.0)  # Esquina inferior izquierda
    glVertex3f(1.0, 0.0, -1.0)   # Esquina inferior derecha
    glVertex3f(1.0, 0.0, 1.0)    # Esquina superior derecha
    glVertex3f(-1.0, 0.0, 1.0)   # Esquina superior izquierda
    glEnd()
    glPopMatrix()

    
def draw_scene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -camera_distance)
    glRotatef(camera_angle_x, 1.0, 0.0, 0.0)
    glRotatef(camera_angle_y, 0.0, 1.0, 0.0)

    draw_walls()  # Dibuja las paredes
    # Bloques blancos
    draw_block((-90, 9.5, -40.0), (0.5, 6.0, 30.0))
    draw_block((-90.0, 9.5, 20.0), (0.5, 6.0, 40.0))
    draw_block((-87.7, 10.3, -25.0), (5, 9, 0.5))
    draw_block((-87.7, 10.3, 0.0), (5, 9, 0.5))
    draw_block((-90, 15.5, -40.0), (0.5, 2, 30.0))
    draw_block((-90.0, 15.5, 20.0), (0.5, 2, 40.0))
    draw_block((-90, 11.5, -65.0), (0.5, 10, 20.0))
    draw_block((90.0, 7, -17.0), (0.5, 13, 116.0))
    draw_block((0.0, 9, -75.0), (180, 15, 0.5))

    # Bloque amarillo
    draw_block((-90.0, 17.5, -12.5), (0.5,6.0, 25.5), (1.0, 1.0, 0.0))  # Color amarillo

    draw_rectangular_plane((-87.5, 6.5, -12.5), (2.5, 1.0, 13))  # Escala para ajustar el tamaño deseado

    glPushMatrix()
    glTranslatef(0, 5, 39.5) 
    glRotatef(90,1,0,0)
    draw_contorno_structure()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, 5, 39.5) 
    glRotatef(90,1,0,0)
    draw_centro_structure()
    glPopMatrix()

    # Dibuja los soportes
    glPushMatrix()
    glTranslatef(10, 0.0, 40) 
    draw_multiple_soportes(160, 0.5, 6.0)  # Dibuja 5 soportes con separación de 1.5 unidades
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(-50, 0.0, 40) 
    draw_multiple_soportes(80, 0.5, 6.0)  # Dibuja 5 soportes con separación de 1.5 unidades
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-90, 5.5, 40)
    glRotatef(-7.5,0,0,1)
    draw_multiple_soportes(80, 0.5, 6.0)  # Dibuja 5 soportes con separación de 1.5 unidades
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-1, 0, 40)
    draw_multiple_soportes(5, 0.5, 7.5)  # Dibuja 5 soportes con separación de 0.5 y altura de 6.0
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
    gluPerspective(45, width / height, 1, 1200)
    glMatrixMode(GL_MODELVIEW)

def keyboard(key, x, y):
    global camera_distance, camera_angle_x, camera_angle_y
    if key == b'w':
        camera_distance -= 1  # Mover hacia adelante
    elif key == b's':
        camera_distance += 1  # Mover hacia atrás
    elif key == b'a':
        camera_angle_y -= 5  # Rotar a la izquierda
    elif key == b'd':
        camera_angle_y += 5  # Rotar a la derecha
    elif key == b'q':
        camera_angle_x -= 5  # Rotar hacia arriba
    elif key == b'e':
        camera_angle_x += 5  # Rotar hacia abajo
    glutPostRedisplay()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(1400, 600)
    glutCreateWindow("Entorno Simple")
    init()
    glutDisplayFunc(draw_scene)
    glutReshapeFunc(reshape)
    glutMouseFunc(mouse_button)
    glutMotionFunc(mouse_motion)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

if __name__ == "__main__":
    main()
