from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

camera_angle_x = 0
camera_angle_y = 0
camera_distance = 40
mouse_x, mouse_y = 0, 0  # Posición inicial del mouse
mouse_left_down = False    

def init():
    glClearColor(0.5, 0.7, 0.9, 1.0)  # Fondo azul claro
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)  

def draw_table():
    glColor3f(0.6, 0.3, 0.1)  # Color de la mesa marrón
    glPushMatrix()
    glScalef(2.0, 0.1, 1.0)  
    glutSolidCube(1)
    glPopMatrix()

    # Pies de la mesa
    for x, z in [(-0.9, 0.4), (0.9, 0.4), (-0.9, -0.4), (0.9, -0.4)]:
        glPushMatrix()
        glTranslatef(x, -0.5, z)
        glScalef(0.1, 1.0, 0.1)
        glutSolidCube(1)
        glPopMatrix()

def draw_chair():
    glColor3f(0.5, 0.2, 0.1)  # Color de la silla
    glPushMatrix()
    glScalef(0.5, 0.05, 0.5)  # Asiento
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0, 0.25, -0.2)
    glScalef(0.5, 0.5, 0.05)
    glutSolidCube(1)
    glPopMatrix()

    for x, z in [(-0.2, -0.2), (0.2, -0.2), (-0.2, 0.2), (0.2, 0.2)]:
        glPushMatrix()
        glTranslatef(x, -0.3, z)
        glScalef(0.05, 0.5, 0.05)
        glutSolidCube(1)
        glPopMatrix()

def draw_walls_with_windows():
    # Paredes del comedor con ventanas
    glColor4f(0.8, 0.8, 0.8, 0.5)  # Paredes transparentes
    glPushMatrix()
    glTranslatef(0.0, 2.0, 0.0)  

    # Pared frontal
    glPushMatrix()
    glScalef(10.0, 4.0, 0.2)  # Pared frontal
    glutSolidCube(1)
    glPopMatrix()

    # Pared trasera
    glPushMatrix()
    glScalef(10.0, 4.0, 0.2)  # Pared trasera
    glTranslatef(0.0, 0.0, -6.0)
    glutSolidCube(1)
    glPopMatrix()

    # Pared lateral izquierda
    glPushMatrix()
    glTranslatef(-5.0, 0.0, -3.0)
    glScalef(0.2, 4.0, 6.0)  # Pared izquierda
    glutSolidCube(1)
    glPopMatrix()

    # Pared lateral derecha
    glPushMatrix()
    glTranslatef(5.0, 0.0, -3.0)
    glScalef(0.2, 4.0, 6.0)  # Pared derecha
    glutSolidCube(1)
    glPopMatrix()

    glPopMatrix()

def draw_bench():
    # Dibujar una banca
    glColor3f(0.4, 0.2, 0.1)  # Color de la banca marrón
    glPushMatrix()
    glScalef(2.0, 0.1, 0.5)  # Asiento de la banca
    glutSolidCube(1)
    glPopMatrix()

    # Pies de la banca
    for x in [-0.9, 0.9]:
        glPushMatrix()
        glTranslatef(x, -0.5, 0.0)
        glScalef(0.1, 1.0, 0.1)
        glutSolidCube(1)
        glPopMatrix()

    # Respaldo de la banca
    glPushMatrix()
    glTranslatef(0.0, 0.25, -0.2)
    glScalef(2.0, 0.5, 0.05)
    glutSolidCube(1)
    glPopMatrix()

def draw_central_patio():
    # Dibujar un área de patio central al lado del comedor
    glColor3f(0.5, 0.7, 0.5)  # Color verde para el césped
    glPushMatrix()
    glTranslatef(15.0, -0.25, 0.0)  # Ubicar el patio al lado derecho del comedor
    glScalef(15.0, 0.05, 10.0)  # Tamaño del patio
    glutSolidCube(1)
    glPopMatrix()

    # Dibujar líneas cuadradas alrededor del patio
    glColor3f(0.0, 0.0, 0.0)  # Color negro para la línea
    glLineWidth(2)
    glPushMatrix()
    glTranslatef(15.0, -0.25, 0.0)

    # Dibujar un cuadrado alrededor del patio
    glBegin(GL_LINE_LOOP)
    glVertex3f(-7.5, 0.01, -5.0)  # Esquina inferior izquierda
    glVertex3f(7.5, 0.01, -5.0)   # Esquina inferior derecha
    glVertex3f(7.5, 0.01, 5.0)    # Esquina superior derecha
    glVertex3f(-7.5, 0.01, 5.0)   # Esquina superior izquierda
    glEnd()
    
    glPopMatrix()

    # Dibujar bancas alrededor del patio
    for (x, z) in [(22.0, 2.5), (22.0, -2.5), (7.0, 2.5), (7.0, -2.5)]:
        glPushMatrix()
        glTranslatef(x, 0.0, z)  # Posición de las bancas
        draw_bench()
        glPopMatrix()

def draw_scene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Mover cámara
    glTranslatef(0.0, 0.0, -camera_distance)
    glRotatef(camera_angle_x, 1.0, 0.0, 0.0)
    glRotatef(camera_angle_y, 0.0, 1.0, 0.0)

    # Dibujar suelo (el terreno de la universidad)
    glColor3f(0.3, 0.3, 0.3)  # Color gris oscuro para el terreno
    glBegin(GL_QUADS)
    glVertex3f(-100.0, -0.5, -100.0)
    glVertex3f(100.0, -0.5, -100.0)
    glVertex3f(100.0, -0.5, 100.0)
    glVertex3f(-100.0, -0.5, 100.0)
    glEnd()

    # Dibujar paredes del comedor con ventanas
    draw_walls_with_windows()

    # Dibujar mesa en el centro del comedor
    glPushMatrix()
    glTranslatef(0.0, 0.0, 0.0)
    draw_table()
    glPopMatrix()

    # Dibujar sillas alrededor de la mesa
    for (x, z) in [(-1.5, 0.8), (1.5, 0.8), (-1.5, -0.8), (1.5, -0.8)]:
        glPushMatrix()
        glTranslatef(x, 0.0, z)
        draw_chair()
        glPopMatrix()

    # Dibujar el patio central al lado del comedor
    draw_central_patio()

    glutSwapBuffers()

def mouse_motion(x, y):
    global camera_angle_x, camera_angle_y, mouse_x, mouse_y
    if mouse_left_down:
        delta_x = x - mouse_x
        delta_y = y - mouse_y
        camera_angle_x += delta_y * 0.2  # Ajustar la velocidad de rotación
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

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Comedor con Patio Central")
    init()
    glutDisplayFunc(draw_scene)
    glutReshapeFunc(reshape)
    glutMouseFunc(mouse_button)
    glutMotionFunc(mouse_motion)
    glutMainLoop()

if __name__ == "__main__":
    main()