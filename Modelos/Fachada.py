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

def draw_paredes():
    glColor3f(0.0, 0.0, 0.0)  # Color de las paredes
    wall_positions = [
        (0.0, 1.0, -75.0),  # Pared frontal
        (20.0, 1.0, 40.0),  # Pared trasera
        (-70.0, 3.6, 40.0),  # Pared inclinada hacia arriba
        (-90.0, 3.5, -17.5), # Pared izquierda
        (90.0, 1.0, -17.5)   # Pared derecha
    ]
    wall_scales = [
        (180.0, 1.0, 1.0),   # Pared frontal
        (140.0, 1.0, 1.0),   # Pared trasera
        (40.0, 1.0, 1.0),    # Pared inclinada
        (1.0, 6.0, 116.0),   # Pared izquierda
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
    for position, scale in zip(contorno_positions, contorno_scales):
        glPushMatrix()
        glTranslatef(*position)
        glScalef(*scale)
        glutSolidCube(1)  # Dibuja el cubo como segmento del contorno
        glPopMatrix()

def draw_centro_structure():
    glColor3f(0.0, 0.0, 0.0)  # Color negro
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

def draw_piso_entrada(position, scale):
    glColor3f(0.75, 0.75, 0.75)  # Color gris
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

def draw_piso_general(position, scale):
    glColor3f(0.75, 0.75, 0.75)  # Color gris
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

def draw_postes():
    glColor3f(0.0, 0.0, 0.0)  # Color de los postes
    # Listas de posiciones y escalas para los postes
    positions = [
        (-85.0, 11.5, -7.0),
        (-84.0, 11.5, -17.0),  # Cambiado para posicionar un poco a la derecha
        (-84.5, 11.5, -12.0),  # Cambiado para posicionar un poco más a la derecha
        (-84.5, 13, -13.0),
        (-90.0, 13.5, 10.0),
        (-90.0, 13.5, 20.0),   # Cambiado para posicionar un poco a la derecha
        (-90.0, 13.5, 30.0),   # Cambiado para posicionar un poco más a la derecha
        (-90.0, 13.5, 39.5),
        (-90.0, 13.5, -50.0),   # Cambiado para posicionar un poco a la izquierda
        (-90.0, 13.5, -45.0),  # Cambiado para posicionar un poco más a la izquierda
        (-90.0, 13.5, -40.0),
        (-90.0, 13.5, -35.0),   # Cambiado para posicionar un poco a la izquierda
        (-90.0, 13.5, -30.0)   # Cambiado para posicionar un poco más a la izquierda
    ]
    scales = [
        (0.5, 10.0, 1.0),
        (0.5, 10.0, 1.0),
        (0.5, 10.0, 1.0),
        (0.5, 1.0, 24.5),
        (0.2, 2.0, 1.0),
        (0.2, 2.0, 1.0),
        (0.2, 2.0, 1.0),
        (0.2, 2.0, 1.0),
        (0.2, 2.0, 1.0),
        (0.2, 2.0, 1.0),
        (0.2, 2.0, 1.0),
        (0.2, 2.0, 1.0),
        (0.2, 2.0, 1.0)
    ]
    # Dibujar cada poste
    for pos, scale in zip(positions, scales):
        glPushMatrix()
        glTranslatef(*pos)  # Posicionar el poste
        glScalef(*scale)    # Escalar el poste
        glutSolidCube(1)     # Dibujar el cubo que representa el poste
        glPopMatrix()

def draw_stairs():
    stair_width = 25
    stair_depth = 1
    stair_height = 0.6  # Escalones más altos
    num_steps = 10   # Menos escalones necesarios
    glColor3f(0.85, 0.85, 0.85) 

    for i in range(num_steps):
        glPushMatrix()
        glRotatef(90,0,1,0)
        glTranslatef(12.5, 1 + (i * stair_height), -72.7 - (i * stair_depth))
        glScalef(stair_width, stair_height, stair_depth)
        glutSolidCube(1) 
        glPopMatrix()


def draw_scene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -camera_distance)
    glRotatef(camera_angle_x, 1.0, 0.0, 0.0)
    glRotatef(camera_angle_y, 0.0, 1.0, 0.0)

    draw_paredes()  # Dibuja las paredes
    draw_postes()
    draw_stairs()

    draw_block((-90, 9.5, -40.0), (0.5, 6.0, 30.0))
    draw_block((-90.0, 9.5, 20.0), (0.5, 6.0, 40.0))
    draw_block((-86.2, 8.5, -25.0), (8, 16, 0.5))
    draw_block((-86.2, 8.5, 0.0), (8, 16, 0.5))
    draw_block((-90, 15.5, -40.0), (0.5, 2, 30.0))
    draw_block((-90.0, 15.5, 20.0), (0.5, 2, 40.0))
    draw_block((-90, 11.5, -65.0), (0.5, 10, 20.0))
    draw_block((90.0, 7, -17.0), (0.5, 13, 116.0))
    draw_block((0.0, 9, -75.0), (180, 15, 0.5))
    draw_block((-90.0, 17.5, -12.5), (0.5,6.0, 25.5), (1.0, 1.0, 0.0))  # Color amarillo
    draw_block((-86.2, 16.5, -12.5), (7, 0.5, 25)) #techo de puerta principal

    draw_piso_entrada((-86.2, 6.5, -12.5), (4, 1.0, 13))
    draw_piso_general((0, 0.5, -17.5), (90, 1.0, 58))

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
    