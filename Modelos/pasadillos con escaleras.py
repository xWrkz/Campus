from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

camera_angle_x = 0
camera_angle_y = 0
camera_distance = 40
mouse_x, mouse_y = 0, 0
mouse_left_down = False

def init():
    glClearColor(0.5, 0.7, 0.9, 1.0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

def draw_walls():
    glColor3f(1.0, 1.0, 1.0)  # Color de las paredes
    wall_data = [
        {'pos': (-5, 2.5, -7.5), 'scale': (79.0, 5.0, 0.4)}, # pared larga
        {'pos': (0.0, 2.5, 7.5), 'scale': (79.0, 5.0, 0.4)}, # pared larga
        {'pos': (-45, 2.5, 0), 'scale': (10.0, 5.0, 0.4)},   # división
        {'pos': (45, 2.5, 0), 'scale': (10.0, 5.0, 0.4)},    # división
        {'pos': (-50.0, 2.5, 3.8), 'scale': (0.4, 5.0, 7.8)}, # pared ancha
        {'pos': (50.0, 2.5, 0), 'scale': (0.4, 5.0, 15.4)}   # pared ancha
    ]
    for data in wall_data:
        glPushMatrix()
        glTranslatef(*data['pos'])
        glScalef(*data['scale'])
        glutSolidCube(1)
        glPopMatrix()

def draw_floor1(position=(0, 0, 0)):
    glColor3f(0.98, 0.92, 0.84)
    glPushMatrix()
    glTranslatef(*position)  # Mover el piso a la posición deseada
    glBegin(GL_QUADS)
    glVertex3f(-50.1, 0.0, -3.8)
    glVertex3f(40, 0.0, -3.8)
    glVertex3f(40, 0.0, 3.8)
    glVertex3f(-50.1, 0.0, 3.8)
    glEnd()
    glPopMatrix()


def draw_floor2(position=(0, 0, 0)):
    glColor3f(0.98, 0.92, 0.84)
    glPushMatrix()
    glTranslatef(*position)  # Mover el piso a la posición deseada
    glBegin(GL_QUADS)
    glVertex3f(-40, 0.0, -3.8)
    glVertex3f(40, 0.0, -3.8)
    glVertex3f(40, 0.0, 3.8)
    glVertex3f(-40, 0.0, 3.8)
    glEnd()
    glPopMatrix()

def draw_Soporte_horizontal(length, axis='x'):
    glColor3f(0.0, 0.0, 0.0)  # Color del soporte
    glPushMatrix()
    
    if axis == 'x':
        glTranslatef(length / 2.0, 0.0, 0.0)  # Posicionar en el eje X
        glScalef(length, 0.1, 0.1)  # Escalar para que sea horizontal en el eje X
    elif axis == 'z':
        glTranslatef(0.0, 0.0, length / 2.0)  # Posicionar en el eje Z
        glScalef(0.1, 0.1, length)  # Escalar para que sea horizontal en el eje Z

    glutSolidCube(1)  # Dibuja un cubo sólido como soporte
    glPopMatrix()

def draw_multiple_soportes_apilados(count, separation, length, axis='x'):
    for i in range(count):
        glPushMatrix()  # Guardar la matriz de transformación actual
        glTranslatef(0.0, i * separation, 0.0)  # Apilar cada soporte en el eje Y
        draw_Soporte_horizontal(length, axis=axis)  # Dibuja un soporte en el eje elegido
        glPopMatrix()  # Restaurar la matriz de transformación

def draw_stairs(position, steps=5, reverse=False, step_width=5.0, step_depth=2.0):
    glColor3f(0.5, 0.5, 0.5)  # Color gris para las escaleras
    step_direction = -1.5 if reverse else 1.5  # Dirección de los escalones
    for i in range(steps):
        glPushMatrix()
        glTranslatef(position[0], position[1] + i * 0.3, position[2] + i * step_direction)
        glScalef(step_width, 0.3, step_depth)  # Tamaño de los escalones
        glutSolidCube(1)
        glPopMatrix()

def draw_scene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -camera_distance)
    glRotatef(camera_angle_x, 1.0, 0.0, 0.0)
    glRotatef(camera_angle_y, 0.0, 1.0, 0.0)

    draw_floor1(position=(0, 0, -3.8))
    draw_floor2(position=(0, 0, 3.8))
    draw_walls()
    draw_stairs(position=(-47.5, -5.1, 1), steps=10)  # Escaleras a la izquierda
    draw_stairs(position=(47.5, -5.1, 1), steps=10)   # Escaleras a la derecha
    draw_stairs(position=(-42.5, -2.5, 14.5), steps=10, reverse=True)  # Escaleras inversas a la izquierda
    draw_stairs(position=(42.5, -2.5, 14.5), steps=10, reverse=True)   # Escaleras inversas a la derecha

    glPushMatrix()
    glTranslatef(-50, 0.1, -7.5) 
    draw_multiple_soportes_apilados(count=5, separation=0.7, length=6.0, axis='x')
    draw_multiple_soportes_apilados(count=5, separation=0.7, length=7.6, axis='z')
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
    gluPerspective(45, width / height, 1, 200)
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
    glutInitWindowSize(1200, 600)
    glutCreateWindow("Pasadizo y escalera")
    init()
    glutDisplayFunc(draw_scene)
    glutReshapeFunc(reshape)
    glutMouseFunc(mouse_button)
    glutMotionFunc(mouse_motion)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

if __name__ == "__main__":
    main()
