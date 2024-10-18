from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

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

def draw_basket():
    # Dibujar el aro de la canasta
    glColor3f(1.0, 0.0, 0.0)  # Color rojo para el aro
    glPushMatrix()
    glTranslatef(0.0, 3.5, 0.0)  # Altura del aro
    glRotatef(90, 1, 0, 0)  # Girar para hacer un círculo
    glutSolidTorus(0.1, 0.3, 20, 20)  # Aro
    glPopMatrix()

    # Dibujar el soporte de la canasta
    glColor3f(0.3, 0.3, 0.3)  # Color gris para el soporte
    glPushMatrix()
    glTranslatef(0.0, 1.5, 0.0)  # Altura del soporte
    glScalef(0.1, 3.0, 0.1)  # Soporte
    glutSolidCube(1)
    glPopMatrix()

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
    wall_positions = [(0.0, 1.0, -10.0), (0.0, 1.0, 10.0), (-10.0, 1.0, 0.0), (10.0, 1.0, 0.0)]
    wall_scales = [(20.0, 2.0, 0.1), (20.0, 2.0, 0.1), (0.1, 2.0, 20.0), (0.1, 2.0, 20.0)]
    
    for position, scale in zip(wall_positions, wall_scales):
        glPushMatrix()
        glTranslatef(*position)
        glScalef(*scale)
        glutSolidCube(1)
        glPopMatrix()

def draw_floor():
    # Dibujar el piso
    glColor3f(0.5, 0.5, 0.5)  # Color gris
    glBegin(GL_QUADS)
    glVertex3f(-10.0, 0.0, -10.0)
    glVertex3f(10.0, 0.0, -10.0)
    glVertex3f(10.0, 0.0, 10.0)
    glVertex3f(-10.0, 0.0, 10.0)
    glEnd()

def draw_yellow_squares():
    # Color amarillo para los cuadrados
    glColor3f(1.0, 1.0, 0.0)  # Color amarillo
    square_size = 4.0  # Tamaño del cuadrado
    
    # Dibujar cuadrado a la izquierda
    glPushMatrix()
    glTranslatef(-5.5, 0.0, 1.7 - square_size / 2)  # Ajustar la posición debajo de la canasta
    glScalef(square_size, 0.1, square_size)  # Tamaño del cuadrado
    glutSolidCube(1)  # Dibujar el cuadrado
    glPopMatrix()

    # Dibujar cuadrado a la derecha
    glPushMatrix()
    glTranslatef(5.5, 0.0, 1.7 - square_size / 2)  # Ajustar la posición debajo de la canasta
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
        glTranslatef(0.0, 0.1+(i * stair_height),-7.7 -(i * stair_depth))  # Posición de cada escalón
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

    # Dibujar canastas en los extremos
    glPushMatrix()
    glTranslatef(-8.5, 0.0, 0.0)  # Canasta izquierda
    draw_basket()
    draw_backboard(-1)  # Cuadrado blanco detrás
    glPopMatrix()

    glPushMatrix()
    glTranslatef(8.5, 0.0, 0.0)  # Canasta derecha
    draw_basket()
    draw_backboard(1)  # Cuadrado blanco detrás
    glPopMatrix()

    # Dibujar cuadrados amarillos debajo de los postes
    draw_yellow_squares()

    # Dibujar la banqueta
    draw_stairs()

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
