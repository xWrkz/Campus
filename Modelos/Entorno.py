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
    glScalef(0.5, 0.05, 0.5)  
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

def draw_border_patio():
    # Paredes del comedor con ventanas
    glColor4f(0.8, 0.8, 0.8, 0.5)   
    glPushMatrix()
    glTranslatef(0.0, 2.0, 0.0)  

    # Pared frontal
    glPushMatrix()
    glScalef(15.0, 3.0, 0.2)  # Pared frontal
    glTranslatef(0.30, -0.30, -20.0)
    glutSolidCube(1)
    glPopMatrix()

    # Pared trasera
    glPushMatrix()
    glScalef(15.0, 3.0, 0.2)  # Pared trasera
    glTranslatef(0.30, -0.30, -80.0)
    glutSolidCube(1)
    glPopMatrix()

    # Pared lateral izquierda
    glPushMatrix()
    glTranslatef(-3.0, -0.90, -10.0)
    glScalef(0.2, 3.0, 12.0)  # Pared izquierda
    glutSolidCube(1)
    glPopMatrix()

    # Pared lateral derecha
    glPushMatrix()
    glTranslatef(12.0, -0.90, -10.0)
    glScalef(0.2, 3.0, 12.0)  # Pared derecha
    glutSolidCube(1)
    glPopMatrix()

    glPopMatrix()


def draw_central_patio():
    glColor3f(0.5, 0.7, 0.5)  # Color verde para el césped
    glPushMatrix()
    glTranslatef(14.5, -0.25, 0.0)  
    glScalef(15.0, 0.05, 10.0)  # Tamaño del patio
    glutSolidCube(1)
    glPopMatrix()

    # Dibujar líneas cuadradas alrededor del patio
    glColor3f(0.0, 0.0, 0.0)  # Color negro para la línea
    glLineWidth(2)
    glPushMatrix()
    glTranslatef(14.5, -0.25, 0.0)

    # Dibujar un cuadrado alrededor del patio
    glBegin(GL_LINE_LOOP)
    glVertex3f(-7.5, 0.01, -5.0)  # Esquina inferior izquierda
    glVertex3f(7.5, 0.01, -5.0)   # Esquina inferior derecha
    glVertex3f(7.5, 0.01, 5.0)    # Esquina superior derecha
    glVertex3f(-7.5, 0.01, 5.0)   # Esquina superior izquierda
    glEnd()
    
    glPopMatrix()


def draw_building():
    # Color de la pared del edificio (gris claro)
    glColor3f(0.7, 0.7, 0.7)  
    
    glPushMatrix()
    glScalef(35.0, 10.0, 15.0)  # Tamaño del edificio
    glutSolidCube(1)
    glPopMatrix()
    
    # Dibujar ventanas en la fachada
    glColor3f(0.3, 0.3, 0.9)  # Color de las ventanas (azul oscuro)
    for x in [-3.0, 0.0, 3.0]:  # Posición horizontal de las ventanas
        for y in [2.0, 4.0, 6.0]:  # Posición vertical de las ventanas
            glPushMatrix()
            glTranslatef(x, y, 2.05)  
            glScalef(1.5, 1.5, 0.1)  
            glutSolidCube(1)
            glPopMatrix()

    # Puerta de entrada
    glColor3f(0.4, 0.2, 0.1)  # Color de la puerta (marrón)
    glPushMatrix()
    glTranslatef(-15.0, -3.5, 7.5)  # Posicionar la puerta en la parte inferior del edificio
    glScalef(2.0, 3.0, 0.1)  # Tamaño de la puerta
    glutSolidCube(1)
    glPopMatrix()

def draw_vertical_path(offset_x):
    # Color del camino vertical (gris claro)
    glColor3f(0.7, 0.7, 0.7)
    glPushMatrix()
    glTranslatef(offset_x, 2.5, 0)  # Cambiar en el eje X para acercarlo a los edificios
    glScalef(10, 0.05, 90.0)  # Mantener el tamaño del camino vertical
    glutSolidCube(1)
    glPopMatrix()

def draw_horizontal_path(offset_z):
    # Color del camino horizontal (gris claro)
    glColor3f(0.7, 0.7, 0.7)
    glPushMatrix()
    glTranslatef(18, 2.5, offset_z)  # Mover en el eje Z según el parámetro offset_z
    glScalef(40.0, 0.05, 4.0)  # Camino horizontal más ancho que el vertical
    glutSolidCube(1)
    glPopMatrix()

def draw_Upn(position, scale, rotate, color=(1.0, 1.0, 1.0)):  # Color blanco por defecto
    glColor3f(*color)  # Aplicar el color del bloque
    glPushMatrix()
    glRotatef(*rotate)
    glTranslatef(*position)  # Posicionar el bloque
    glScalef(*scale)         # Escalar el bloque
    glutSolidCube(1)         # Dibuja un cubo sólido
    glPopMatrix()
    
def draw_square():
    glColor3f(0.6, 0.4, 0.2)  # Color marrón para el cuadrado
    glBegin(GL_QUADS)
    
    # Cuadrado: Cara en el plano XY
    glVertex3f(-0.5, -0.5, 0.0)
    glVertex3f(0.5, -0.5, 0.0)
    glVertex3f(0.5, 0.5, 0.0)
    glVertex3f(-0.5, 0.5, 0.0)

    glEnd()

def draw_zigzag_path():
    glPushMatrix()
    glTranslatef(-13.7, 3.0, -24)  # Eleva el bloque más alto sobre el suelo
    glLineWidth(24.0)  # Aumenta el grosor de las líneas

    # Dimensiones del bloque y los triángulos
    block_length = 60.0    # Largo del bloque
    block_width = 1.4      # Ancho del bloque
    block_height = 2.0     # Altura del bloque
    triangle_width = 5.0   # Ancho de los triángulos laterales
    triangle_height = 10.0  # Altura de los triángulos laterales

    # Cuerpo principal del bloque rectangular (cara superior sin borde)
    glColor3f(0.0, 1.0, 0.0)  # Verde para la cara superior
    glBegin(GL_QUADS)
    glVertex3f(-block_width, block_height, 0)
    glVertex3f(block_width, block_height, 0)
    glVertex3f(block_width, block_height, block_length)
    glVertex3f(-block_width, block_height, block_length)
    glEnd()

    # Colorear los lados y la cara inferior en gris
    glColor3f(0.5, 0.5, 0.5)  # Gris
    glBegin(GL_QUADS)
    # Cara inferior
    glVertex3f(-block_width, 0, 0)
    glVertex3f(block_width, 0, 0)
    glVertex3f(block_width, 0, block_length)
    glVertex3f(-block_width, 0, block_length)

    # Caras laterales del bloque
    glVertex3f(-block_width, 0, 0)
    glVertex3f(-block_width, block_height, 0)
    glVertex3f(-block_width, block_height, block_length)
    glVertex3f(-block_width, 0, block_length)

    glVertex3f(block_width, 0, 0)
    glVertex3f(block_width, block_height, 0)
    glVertex3f(block_width, block_height, block_length)
    glVertex3f(block_width, 0, block_length)
    glEnd()

    # Triángulos en zigzag en el borde derecho (sin borde superior)
    num_zigzags = 3
    for i in range(num_zigzags):
        z_position = i * (block_length / num_zigzags)

        # Cara superior del triángulo en verde
        glColor3f(0.0, 1.0, 0.0)  # Verde para la cara superior
        glBegin(GL_TRIANGLES)
        glVertex3f(block_width, block_height, z_position)
        glVertex3f(block_width + triangle_width, block_height, z_position + triangle_height)
        glVertex3f(block_width, block_height, z_position + triangle_height * 2)
        glEnd()

        # Pintar los lados y la base del triángulo en gris
        glColor3f(0.5, 0.5, 0.5)  # Gris para los lados y la base
        glBegin(GL_QUADS)
        # Cara lateral derecha hacia el suelo
        glVertex3f(block_width + triangle_width, block_height, z_position + triangle_height)
        glVertex3f(block_width + triangle_width, 0, z_position + triangle_height)
        glVertex3f(block_width, 0, z_position + triangle_height * 2)
        glVertex3f(block_width, block_height, z_position + triangle_height * 2)

        # Cara lateral izquierda hacia el suelo
        glVertex3f(block_width, block_height, z_position)
        glVertex3f(block_width, 0, z_position)
        glVertex3f(block_width, 0, z_position + triangle_height * 2)
        glVertex3f(block_width, block_height, z_position + triangle_height * 2)

        # Base del triángulo en el suelo
        glVertex3f(block_width, 0, z_position)
        glVertex3f(block_width + triangle_width, 0, z_position + triangle_height)
        glVertex3f(block_width, 0, z_position + triangle_height * 2)
        glEnd()

        # Cara trasera del triángulo (cierra el triángulo en la parte trasera)
        glBegin(GL_QUADS)
        glVertex3f(block_width, block_height, z_position)
        glVertex3f(block_width + triangle_width, block_height, z_position + triangle_height)
        glVertex3f(block_width + triangle_width, 0, z_position + triangle_height)
        glVertex3f(block_width, 0, z_position)
        glEnd()

        # Bordes horizontales en la parte superior del triángulo
        glColor3f(0.5, 0.5, 0.5)  # Gris para los bordes horizontales
        # Borde superior en el lado derecho del triángulo
        glBegin(GL_LINES)
        glVertex3f(block_width + triangle_width, block_height, z_position + triangle_height)
        glVertex3f(block_width, block_height, z_position + triangle_height * 2)
        glEnd()

        # Borde superior en el lado izquierdo del triángulo
        glBegin(GL_LINES)
        glVertex3f(block_width, block_height, z_position)
        glVertex3f(block_width + triangle_width, block_height, z_position + triangle_height)
        glEnd()

    glPopMatrix()
    glLineWidth(1.0)  # Restablece el grosor de las líneas al valor 


def draw_scene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Mover cámara
    glTranslatef(0.0, 0.0, -camera_distance)
    glRotatef(camera_angle_x, 1.0, 0.0, 0.0)
    glRotatef(camera_angle_y, 0.0, 1.0, 0.0)

    # Dibujar suelo inferior(el terreno del patio)
    glColor3f(0.0, 0.0, 0.0)  # Color gris oscuro para el terreno
    glBegin(GL_QUADS)
    glVertex3f(-100.0, -0.5, -100.0)
    glVertex3f(100.0, -0.5, -100.0)
    glVertex3f(100.0, -0.5, 100.0)
    glVertex3f(-100.0, -0.5, 100.0)
    glEnd()

    # Dibujar suelo (el terreno de la universidad)
    glColor3f(0.3, 0.3, 0.3)  # Color gris oscuro para el terreno
    glBegin(GL_QUADS)
    glVertex3f(-100.0, 2.5, -100.0)
    glVertex3f(100.0, 2.5, -100.0)
    glVertex3f(100.0, 2.5, 100.0)
    glVertex3f(-100.0, 2.5, 100.0)
    glEnd()
    
    glPushMatrix
    draw_vertical_path(-10)
    draw_vertical_path(30)
    glPopMatrix 

    glPushMatrix
    draw_horizontal_path(-9.0)  # Camino horizontal cerca de la parte trasera
    draw_horizontal_path(9.0)
    glPopMatrix
    
    draw_zigzag_path()
    # Dibujar paredes del comedor con ventanas
    glPushMatrix()
    glTranslatef(10.0, 0.0, 10.0)
    draw_border_patio()
    glPopMatrix()
    # Dibujar el patio central al lado del comedor
    draw_central_patio()

    # Dibujar el edificio cercano al comedor
    glPushMatrix()
    glTranslatef(17.50, 7.5, -20.0)  # Ubicar el edificio en la escena
    draw_building()
    glPopMatrix()
    glPushMatrix()
    glTranslatef(17.50, 7.5, 20.0)  # Ubicar el edificio en la escena
    draw_building()
    glPopMatrix()

    draw_Upn((-5,3,10),(2,2,3),(0,0,0,0))
    draw_Upn((-5.5,5,9),(1,5,0.5),(0,0,0,0),(1,1,0))
    draw_Upn((-5.5,5,9.8),(1,5,0.5),(0,0,0,0),(1,1,0))
    draw_Upn((-5.5,9.1,6),(1,1.8,0.5),(18,1,0,0),(1,1,0))
    draw_Upn((-5.5,3.2,11.9),(1,1.8,0.5),(-18,1,0,0),(1,1,0))

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
    glutInitWindowSize(1600, 900)
    glutCreateWindow(b"Comedor con Patio Central")
    init()
    glutDisplayFunc(draw_scene)
    glutReshapeFunc(reshape)
    glutMouseFunc(mouse_button)
    glutMotionFunc(mouse_motion)
    glutMainLoop()

if __name__ == "__main__":
    main()
