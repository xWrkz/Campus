from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

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

def draw_terreno_edificios():
    # Dibujar suelo (el terreno de la universidad) con un hueco en el centro
    glColor3f(0.3, 0.3, 0.3)  # Color gris oscuro para el terreno
    
    # Parte izquierda del terreno
    glBegin(GL_QUADS)
    glVertex3f(-100.0, 2.5, -100.0)
    glVertex3f( 6.5, 2.5, -100.0)
    glVertex3f( 6.5, 2.5, 100.0) #control 
    glVertex3f(-100.0, 2.5, 100.0)
    glEnd()

    # Parte derecha del terreno
    glBegin(GL_QUADS)
    glVertex3f(25.0, 2.5, -100.0) # x = mueve hacia el lado izq el patio
    glVertex3f(100.0, 2.5, -100.0)
    glVertex3f(100.0, 2.5, 100.0)
    glVertex3f(20.0, 2.5, 100.0)
    glEnd()

    # Parte superior del terreno
    glBegin(GL_QUADS)
    glVertex3f(-20.0, 2.5, 6.5) #no
    glVertex3f(50.0, 2.5, 6.5) #no
    glVertex3f(50.0, 2.5, 100.0) #no
    glVertex3f(-20.0, 2.5, 100.0) #no
    glEnd()

    # Parte inferior del terreno
    glBegin(GL_QUADS)
    glVertex3f(-20.0, 2.5, -100.0) #no
    glVertex3f(50.0, 2.5, -100.0) #no
    glVertex3f(50.0, 2.5, -6.5) # x = mueve los laterales del patio
    glVertex3f(-20.0, 2.5, -6.5) #no
    glEnd()



def draw_terreno_patio():
# Dibujar suelo inferior(el terreno del patio)
    glColor3f(0.0, 0.0, 0.0)  # Color gris oscuro para el terreno
    glBegin(GL_QUADS)
    glVertex3f(-100.0, -0.5, -100.0)
    glVertex3f(100.0, -0.5, -100.0)
    glVertex3f(100.0, -0.5, 100.0)
    glVertex3f(-100.0, -0.5, 100.0)
    glEnd()

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

def draw_border_patio():
    # Paredes del comedor con ventanas
    glColor4f(0.8, 0.8, 0.8, 0.5)  # Paredes transparentes
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
    # Dibujar un área de patio central al lado del comedor
    glColor3f(0.5, 0.7, 0.5)  # Color verde para el césped
    glPushMatrix()
    glTranslatef(14.5, -0.25, 0.0)  # Ubicar el patio al lado derecho del comedor
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
    
    # Cuerpo del edificio
    glPushMatrix()
    glScalef(35.0, 10.0, 15.0)  # Tamaño del edificio
    glutSolidCube(1)
    glPopMatrix()
    
    # Dibujar ventanas en la fachada
    glColor3f(0.3, 0.3, 0.9)  # Color de las ventanas (azul oscuro)
    for x in [-3.0, 0.0, 3.0]:  # Posición horizontal de las ventanas
        for y in [2.0, 4.0, 6.0]:  # Posición vertical de las ventanas
            glPushMatrix()
            glTranslatef(x, y, 2.05)  # Posicionar ventanas ligeramente fuera de la fachada
            glScalef(1.5, 1.5, 0.1)  # Tamaño de las ventanas
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
    
def draw_block():
    # Dibuja un bloque largo y alto encima del camino
    glColor3f(0.6, 0.4, 0.2)  # Color marrón para el bloque
    glPushMatrix()
    
    # Posicionar el bloque para que esté alineado con el camino vertical
    glTranslatef(-7.0, 3.5, 0.0)  # Moverse al lado del camino vertical
    glScalef(1, 0.5, 50.0)  # Tamaño del bloque (alto y largo)
    glutSolidCube(1)
    
    glPopMatrix()

# Comienzo de la creacion de la losa deportiva
def draw_half_circle(radius, segments):
    glLineWidth(2.0)
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINE_STRIP)
    for i in range(segments + 1):
        angle = math.pi * i / segments
        x = radius * math.sin(angle)
        y = radius * math.cos(angle)
        glVertex2f(x, y)
    glEnd()

def draw_circle(radius, segments):
    glLineWidth(3.0)
    glBegin(GL_LINE_LOOP)
    for i in range(segments):
        angle = 2 * math.pi * i / segments
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex2f(x, y)
    glEnd()

def draw_Soporte():
    glColor3f(1.0, 1.0, 0.0)
    glPushMatrix()
    glTranslatef(0.0, 1.5, 0.0)
    glScalef(0.1, 3.0, 0.1)
    glutSolidCube(1)
    glPopMatrix()
    draw_black_cubes_and_pyramid()

def draw_aro():
    glColor3f(1.0, 1.0, 0.0)
    glPushMatrix()
    glTranslatef(0.0, 3.5, 0.0)
    glTranslatef(0.0, 0.0, 0.0) 
    glRotatef(90, 1, 0, 0)
    glutSolidTorus(0.1, 0.3, 20, 20) 
    glPopMatrix()

def draw_backboard(x_position):
    glColor3f(1.0, 1.0, 1.0)
    glPushMatrix()
    glTranslatef(x_position, 4.0, 0.0) 
    glRotatef(90, 0.0, 1.0, 0.0)
    glScalef(1.5, 1.0, 0.1) 
    glutSolidCube(1)
    glPopMatrix()

def draw_walls():
    glColor3f(0.5, 0.6, 0.7)
    wall_positions = [
        (0.0, 1.0, -15.0),  
        (0.0, 1.0, 8.0),  
        (-18.0, 1.0, -3.5), 
        (18.0, 1.0, -5) 
    ]
    wall_scales = [
        (36.0, 2.0, 0.4),   
        (36.0, 2.0, 0.4),
        (0.4, 2.0, 23.0), 
        (0.4, 2.0, 20.0)
    ]
    for position, scale in zip(wall_positions, wall_scales):
        glPushMatrix()
        glTranslatef(*position)
        glScalef(*scale)
        glutSolidCube(1)
        glPopMatrix()

def draw_rectangle():
    glColor3f(0.75, 0.75, 0.75) 
    glBegin(GL_QUADS)
    glVertex3f(-14, 0.02, -3.0) 
    glVertex3f(7.0, 0.02, -3.0)
    glVertex3f(7.0, 0.02, 3.0) 
    glVertex3f(-14, 0.02, 3.0) 
    glEnd()

def draw_rectangle_green():
    glColor3f(0.0, 0.75, 0.0)
    glBegin(GL_QUADS)
    glVertex3f(-28, 0.01, -5.0) 
    glVertex3f(7.0, 0.01, -5.0) 
    glVertex3f(7.0, 0.01, 3.0)
    glVertex3f(-28, 0.01, 3.0)  
    glEnd()

def draw_lines():
    glLineWidth(3.0)
    glColor3f(1.0, 1.0, 1.0) 
    glBegin(GL_LINES)
    glVertex3f(0, 0.0, 7.0)
    glVertex3f(0, 0.0, 2.0)
    glVertex3f(0, 0.0, -2.0)
    glVertex3f(0, 0.0, -7.0)
    glEnd()

def draw_floor():
    glColor3f(0.5, 0.5, 0.65)
    glBegin(GL_QUADS)
    glVertex3f(-18.0, 0.0, -15.0) 
    glVertex3f(18.0, 0.0, -15.0)
    glVertex3f(18.0, 0.0, 8.0)
    glVertex3f(-18.0, 0.0, 8.0)
    glEnd()

def draw_rectangle_outline():
    glLineWidth(3.0) 
    glColor3f(1.0, 1.0, 0.0)  
    glBegin(GL_LINE_LOOP) 
    glVertex3f(-12.0, 0.0, -4.0) 
    glVertex3f(12.0, 0.0, -4.0)   
    glVertex3f(12.0, 0.0, 4.0)   
    glVertex3f(-12.0, 0.0, 4.0) 
    glEnd()

def draw_rectangle_outline2():
    glLineWidth(4.0)  
    glColor3f(1.0, 1.0, 1.0)  
    glBegin(GL_LINE_LOOP) 
    glVertex3f(-14.5, 0.0, -7.0)  
    glVertex3f(14.5, 0.0, -7.0)   
    glVertex3f(14.5, 0.0, 7.0)    
    glVertex3f(-14.5, 0.0, 7.0)  
    glEnd()

def draw_black_cubes_and_pyramid():
    glColor3f(0.0, 0.0, 0.0)
    glPushMatrix()
    glTranslatef(0.0, 0.5, 0.0)
    glutSolidCube(1.0) 
    glPopMatrix()
    glBegin(GL_TRIANGLES)
    # Cara frontal
    glVertex3f(0.0, 2.0, 0.0) 
    glVertex3f(-0.5, 1.0, -0.5)  
    glVertex3f(0.5, 1.0, -0.5) 
    # Cara derecha
    glVertex3f(0.0, 2.0, 0.0)
    glVertex3f(0.5, 1.0, -0.5)
    glVertex3f(0.5, 1.0, 0.5) 
    # Cara trasera
    glVertex3f(0.0, 2.0, 0.0)
    glVertex3f(0.5, 1.0, 0.5)
    glVertex3f(-0.5, 1.0, 0.5) 
    # Cara izquierda
    glVertex3f(0.0, 2.0, 0.0)
    glVertex3f(-0.5, 1.0, 0.5)
    glVertex3f(-0.5, 1.0, -0.5) 
    glEnd()
    # Dibuja un cubo pequeño en la punta de la pirámide
    glColor3f(0.0, 0.0, 0.0) 
    glPushMatrix()
    glTranslatef(0.0, 1.8, 0.0)  
    glutSolidCube(0.3) 
    glPopMatrix()

def draw_yellow_squares():
    square_size = 4.0  
    glColor3f(1.0, 1.0, 0.0)
    glPushMatrix()
    glTranslatef(-12.5, 0.0, 0.0) 
    glScalef(square_size, 0.1, square_size)
    glutSolidCube(1)
    glPopMatrix()
    # Dibujar cuadrado a la derecha
    glColor3f(1.0, 1.0, 0.0) 
    glPushMatrix()
    glTranslatef(12.5, 0.0, 0.0) 
    glScalef(square_size, 0.1, square_size)  
    glutSolidCube(1)
    glPopMatrix()

def draw_stairs():
    stair_width = 7.5
    stair_depth = 0.5
    stair_height = 0.2
    num_steps = 5
    glColor3f(0.5, 0.5, 0.5) 
    for i in range(num_steps):
        glPushMatrix()
        glTranslatef(-3, 0.1 + (i * stair_height), -10 - (i * stair_depth))
        glScalef(stair_width, stair_height, stair_depth)
        glutSolidCube(1) 
        glPopMatrix()
    # Dibujar el techo
    roof_width = stair_width
    roof_depth = stair_depth * 6
    roof_height = 0.1  
    glColor3f(0.75, 0.75, 0.75) 
    glPushMatrix()
    glTranslatef(-3, 1.1 + (num_steps * stair_height) + roof_height + 0.5, -9 - (num_steps * stair_depth))
    glScalef(roof_width, roof_height, roof_depth) 
    glutSolidCube(1) 
    glPopMatrix()
    # Dibujar los soportes
    support_width = 0.1
    support_height = 2.7
    support_depth = 0.1  
    glColor3f(0.5, 0.5, 0.5)  
    for i in [-1, 1]: 
        glPushMatrix()
        glTranslatef(-3 - (roof_width / 2) * i, 0.4 + (num_steps * stair_height), -10 - (num_steps * stair_depth)) 
        glScalef(support_width, support_height, support_depth) 
        glutSolidCube(1) 
        glPopMatrix()

def draw_scene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Movimiento de cámara
    glTranslatef(0.0, 0.0, -camera_distance)
    glRotatef(camera_angle_x, 1.0, 0.0, 0.0)
    glRotatef(camera_angle_y, 0.0, 1.0, 0.0)

    # Terreno de edificios
    glPushMatrix()
    draw_terreno_edificios()
    glPopMatrix()

    # Terreno del patio
    glPushMatrix()
    draw_terreno_patio()
    glPopMatrix()

    glPushMatrix
    draw_vertical_path(-10)
    draw_vertical_path(30)
    glPopMatrix 

    glPushMatrix
    draw_horizontal_path(-9.0)  # Camino horizontal cerca de la parte trasera
    draw_horizontal_path(9.0)
    glPopMatrix
    
    draw_block()

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

# Comienzo de ubicacion de la Losa deportiva

    # Dibujado el terreno
    glPushMatrix()
    glTranslatef(20.0, 2.6, 50.0)
    draw_floor()
    draw_walls()
    glPopMatrix()
    
    # Dibujado de base de las escaleras
    glPushMatrix()
    glTranslatef(27.0, 2.6, 53.0)   
    draw_rectangle()
    glPopMatrix()

    # Dibujado de area verde en la losa
    glPushMatrix()
    glTranslatef(30.5, 2.6, 55.0)
    draw_rectangle_green()
    glPopMatrix()

    # Dibujados sobre el terreno
    glPushMatrix()
    glTranslatef(20.0, 2.7, 42.5)
    draw_rectangle_outline()
    draw_rectangle_outline2()
    draw_lines()
    draw_yellow_squares()
    glPopMatrix()

    # Dibujados de basquet
    glPushMatrix()
    glTranslatef( 3.5 , 2.7, 42.0)  # Canasta izquierda
    draw_Soporte()
    draw_aro()
    draw_backboard(-1)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(36.5 , 2.7, 42.0)  # Canasta derecha
    draw_Soporte()
    draw_aro()
    draw_backboard(1)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(20.0, 2.6, 42.0)   
    glRotatef(180, 0.0, 1.0, 0.0) # La hace girar sobre su mismo eje
    draw_stairs()
    glPopMatrix()
    
    # Circulo pequenio para el campo situado en el palo de baloncesto izq
    glPushMatrix()
    glTranslatef(30.6, 2.8, 42.5) 
    glRotatef(90, 1.0, 0.0, 0.0)  
    glRotatef(180, 0.0, 0.0, 1.0)
    draw_half_circle(1.5, 100)  
    glPopMatrix()

    # Circulo mediano para el campo situado en el palo de baloncesto izq
    glPushMatrix()
    glTranslatef(34.5, 2.8, 42.5) 
    glRotatef(90, 1.0, 0.0, 0.0)  
    glRotatef(180, 0.0, 0.0, 1.0)
    draw_half_circle(0.7, 100) 
    glPopMatrix()

    # Circulo grande para el campo situado en el palo de baloncesto izq
    glPushMatrix()
    glTranslatef(34.5, 2.8, 42.5) 
    glRotatef(90, 1.0, 0.0, 0.0)  
    glRotatef(180, 0.0, 0.0, 1.0)
    draw_half_circle(6, 100) 
    glPopMatrix()

    # Circulo pequenio para el campo situado en el palo de baloncesto derecho
    glPushMatrix()
    glTranslatef( 9.5 , 2.8, 42.5) 
    glRotatef(90, 1.0, 0.0, 0.0)  
    glRotatef(0, 0.0, 0.0, 1.0)
    draw_half_circle(1.5, 100)  
    glPopMatrix()
    
    # Circulo mediano para el campo situado en el palo de baloncesto derecho
    glPushMatrix()
    glTranslatef( 5.5 , 2.8, 42.5)
    glRotatef(90, 1.0, 0.0, 0.0)  
    glRotatef(0, 0.0, 0.0, 1.0)
    draw_half_circle(0.7, 100)  
    glPopMatrix()

    # Circulo grande para el campo situado en el palo de baloncesto derecho
    glPushMatrix()
    glTranslatef( 5.5 , 2.8, 42.5)
    glRotatef(90, 1.0, 0.0, 0.0)  
    glRotatef(0, 0.0, 0.0, 1.0)
    draw_half_circle(6, 100)  
    glPopMatrix()

    glPushMatrix()
    glTranslatef( 20.0 , 2.8, 42.5) 
    glRotatef(90, 1.0, 0.0, 0.0)
    glColor3f(1.0, 1.0, 1.0)  
    draw_circle(2.0, 100)  
    glPopMatrix()
    # Fin de loza deportiva 
    
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
    glutInitWindowSize(1600, 900)
    glutCreateWindow(b"Comedor con Patio Central")
    init()
    glutDisplayFunc(draw_scene)
    glutReshapeFunc(reshape)
    glutMouseFunc(mouse_button)
    glutMotionFunc(mouse_motion)
    glutKeyboardFunc(keyboard)  # Capturar entradas del teclado
    glutMainLoop()

if __name__ == "__main__":
    main()