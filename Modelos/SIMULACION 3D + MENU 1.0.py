# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 16:07:59 2024

@author: Diego
"""

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

camera_angle_x = 0
camera_angle_y = 0
camera_distance = 40
mouse_x, mouse_y = 0, 0  # Posición inicial del mouse
mouse_left_down = False    

pabellon_a = (-15.0, 5.5, -15.0)
losa_deportiva = (65.50, 2.7, -53.5)
puerta_upn = (-85.0, 7.5, -15.0)
pabellon_b = (-15.0, 5.5, -1.5)

# Variables globales para mostrar/ocultar las líneas
linea2 = False  # Línea entre Edificio 1 y Edificio 2 (amarillo)
linea3 = False
linea4 = False

# Variables globales
main_window = None
menu_window = None
menu_items = ["1-.PABELLÓN", "BIBLIOTECA", "LCOM1", "LCOM2", "LAB ELECTRÓNICA", "AUDITORIO", "COMPLEJO DEPORTIVO", "ESTACIONAMIENTO"]


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
    for x in [-5.0, 0.0, 5.0]:  # Posición horizontal de las ventanas (más separadas)
        for y in [2.0, 2.5, 3.0]:  # Posición vertical de las ventanas 
            glPushMatrix()
            glTranslatef(x, y, 7.6)  # Posicionar ventanas 
            glScalef(2.5, 1.0, 0.5)  # Tamaño de las ventanas 
            glutSolidCube(1)
            glPopMatrix()
        
        # Ventanas adicionales más abajo
        for y in [-2.0, -1.5, -1.0]:  
            glPushMatrix()
            glTranslatef(x, y, 7.6)  
            glScalef(2.5, 1.0, 0.5)  
            glutSolidCube(1)
            glPopMatrix()

    # Puerta de entrada en el lado izquierdo
    glColor3f(0.4, 0.2, 0.1)  # Color de la puerta (marrón)
    glPushMatrix()
    glTranslatef(-15.0, -3.5, 7.5)  # Posicionar la puerta en la parte inferior del edificio
    glScalef(2.0, 3.0, 0.1)  # Tamaño de la puerta
    glutSolidCube(1)
    glPopMatrix()

    # Puerta de entrada en el lado derecho
    glColor3f(0.4, 0.2, 0.1)  # Color de la puerta (marrón)
    glPushMatrix()
    glTranslatef(15.0, -3.5, 7.5)  # Posicionar la puerta en el lado opuesto del edificio
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

def draw_zigzag_path():
    glPushMatrix()
    glTranslatef(-1.0 + 5.0 , 3.0, -36)  # Eleva el bloque más alto sobre el suelo
    glLineWidth(24.0)  # Aumenta el grosor de las líneas

    # Dimensiones del bloque y los triángulos
    block_length = 66.0    # Largo del bloque
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

# COMIENZO LOSA DEPORTIVA
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

# COMIENZO DE FACHADA UPN
def draw_paredes_fachada():
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

def draw_soporte_fachada(height):
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
        draw_soporte_fachada(height)  # Llamar a la función que dibuja un solo soporte con altura personalizada
        glPopMatrix()  # Restaurar la matriz de transformación

def draw_block_fachada(position, scale, color=(1.0, 1.0, 1.0)):  # Color blanco por defecto
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

def draw_postes_fachada():
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

def draw_escaleras_fachada():
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

# ------------------------------------------------------DIBUJADO DE ESCENA-------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------
def draw_scene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Movimiento de camara
    glTranslatef(0.0, 0.0, -camera_distance)
    glRotatef(camera_angle_x, 1.0, 0.0, 0.0)
    glRotatef(camera_angle_y, 0.0, 1.0, 0.0)

# COMIENZO DE FACHADA------------------------------------------------------------------------------------
    draw_paredes_fachada()  # Dibuja las paredes
    draw_postes_fachada()
    draw_escaleras_fachada()

    draw_block_fachada((-90, 9.5, -40.0), (0.5, 6.0, 30.0))
    draw_block_fachada((-90.0, 9.5, 20.0), (0.5, 6.0, 40.0))
    draw_block_fachada((-86.2, 8.5, -25.0), (8, 16, 0.5))
    draw_block_fachada((-86.2, 8.5, 0.0), (8, 16, 0.5))
    draw_block_fachada((-90, 15.5, -40.0), (0.5, 2, 30.0))
    draw_block_fachada((-90.0, 15.5, 20.0), (0.5, 2, 40.0))
    draw_block_fachada((-90, 11.5, -65.0), (0.5, 10, 20.0))
    draw_block_fachada((90.0, 7, -17.0), (0.5, 13, 116.0))
    draw_block_fachada((0.0, 9, -75.0), (180, 15, 0.5))
    draw_block_fachada((-90.0, 17.5, -12.5), (0.5,6.0, 25.5), (1.0, 1.0, 0.0))  # Color amarillo
    draw_block_fachada((-86.2, 16.5, -12.5), (7, 0.5, 25)) #techo de puerta principal

    draw_piso_entrada((-86.2, 6.5, -12.5), (4, 1.0, 13))

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
# FIN DE FACHADA--------------------------------------------------------------------------------------

# TERRENO UNIVERSIDAD---------------------------------------------------------------------------------
    # Terreno de pabellones
    glPushMatrix()
    glTranslatef(-12.0, 0.0, -47.0)
    draw_terreno_edificios()
    glPopMatrix()

    # Terreno del areaverde
    glPushMatrix()
    glTranslatef(-12.0, 0.0, -47.0)
    draw_terreno_patio()
    glPopMatrix()

    #--------------------------------CAMINOS------------------------------
    # Dibujado en terreno
    glPushMatrix()
    glTranslatef(0.0, 0.0, 0.0)
    glRotatef(90, 0.0, 1.0, 0.0)
    draw_vertical_path(65)
    draw_vertical_path(8)
    draw_zigzag_path()
    draw_Upn((7,3,10),(2,2,3),(0,0,0,0))
    draw_Upn((7.3,5,9),(1,5,0.5),(0,0,0,0),(1,1,0))
    draw_Upn((7.3,5,9.8),(1,5,0.5),(0,0,0,0),(1,1,0))
    draw_Upn((7.3,9.1,6),(1,1.8,0.5),(18,1,0,0),(1,1,0))
    draw_Upn((7.3,3.2,11.9),(1,1.8,0.5),(-18,1,0,0),(1,1,0))
    draw_vertical_path(30)
    glPopMatrix()
    
    # Separador de aparcamientos
    glPushMatrix()
    glTranslatef(0.0, 0.0, 0.0)
    glRotatef(90, 0.0, 1.0, 0.0)
    glPopMatrix()

    # Caminos delgados
    glPushMatrix()
    glTranslatef(0.0, 0.0, -30.0)
    glRotatef(90, 0.0, 1.0, 0.0)
    draw_horizontal_path(-13.0)  
    draw_horizontal_path(19.0)
    glPopMatrix()
    #--------------------------------CAMINOS------------------------------

    #--------------------------PATIO AREA VERDE------------------------------
    # Dibuja paredes del comedor con ventanas
    glPushMatrix()
    glTranslatef(13.0, 0.0, -43.0)
    glRotatef(90, 0.0, 1.0, 0.0)
    draw_border_patio()  
    glPopMatrix()

    # Dibuja el patio central al lado del comedor
    glPushMatrix()
    glTranslatef(3.0, 0.0, -33.0)
    glRotatef(90, 0.0, 1.0, 0.0)
    draw_central_patio()
    glPopMatrix()
    #--------------------------PATIO AREA VERDE------------------------------

    # ------------------------ PABELLONES ------------------------
    glPushMatrix()
    glTranslatef(-30.0, 7.5, -45.0)  # Ubica pabellon A en la escena
    glRotatef(90, 0.0, 1.0, 0.0) # La hace girar sobre su mismo eje
    draw_building()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(35.50, 7.5, -45.0)  # Ubica pabellon B en la escena
    glRotatef( 270, 0.0, 1.0, 0.0) # La hace girar sobre su mismo eje
    draw_building()
    glPopMatrix()
    # ------------------------ PABELLONES------------------------

    
# FIN DE TERRENO UNIVERDSIDAD ------------------------------------------------------------------------

# COMIENZO DE LOSA DEPORTIVA
    # Dibujado el terreno
    glPushMatrix()
    glTranslatef(65.50, 2.6, -53.0)
    glRotatef(270, 0.0, 1.0, 0.0) # La hace girar sobre su mismo eje
    draw_floor()
    draw_walls()
    glPopMatrix()
    
    # Dibujado de base de las escaleras
    glPushMatrix()
    glTranslatef(75.50, 2.6, -50.0)
    glRotatef(270, 0.0, 1.0, 0.0) # La hace girar sobre su mismo eje
    draw_rectangle()
    glPopMatrix()

    # Dibujado de area verde en la losa
    glPushMatrix()
    glTranslatef(75.50, 2.6, -42.5)
    glRotatef(270, 0.0, 1.0, 0.0) # La hace girar sobre su mismo eje
    draw_rectangle_green()
    glPopMatrix()

    # Dibujados sobre el terreno
    glPushMatrix()
    glTranslatef(65.50, 2.6, -53.5)
    glRotatef(270, 0.0, 1.0, 0.0) # La hace girar sobre su mismo eje
    draw_rectangle_outline()
    draw_rectangle_outline2()
    draw_lines()
    draw_yellow_squares()
    glPopMatrix()

    # Dibujados de basquet
    glPushMatrix()
    glTranslatef(65.50, 2.6, -69.5)  # Canasta izquierda
    glRotatef(90, 0.0, 1.0, 0.0)
    draw_Soporte()
    draw_aro()
    draw_backboard(-1)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(65.50, 2.6, -37.5)  # Canasta derecha
    glRotatef(90, 0.0, 1.0, 0.0)
    draw_Soporte()
    draw_aro()
    draw_backboard(1)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(65.50, 2.6, -51.0)   
    glRotatef(270, 0.0, 1.0, 0.0) # La hace girar sobre su mismo eje
    draw_stairs()
    glPopMatrix()
    
    # Lado IZQ
    # Circulo pequenio para el campo situado en el palo de baloncesto izq
    glPushMatrix()
    glTranslatef(65.50, 2.7, -67.5) 
    glRotatef(90, 1.0, 0.0, 0.0)  
    glRotatef(90, 0.0, 0.0, 1.0)
    draw_half_circle(0.7, 100) 
    glPopMatrix()

    # Circulo mediano para el campo situado en el palo de baloncesto izq
    glPushMatrix()
    glTranslatef(65.50, 2.7, -64.0)
    glRotatef(90, 1.0, 0.0, 0.0)  
    glRotatef(90, 0.0, 0.0, 1.0)
    draw_half_circle(1.5, 100)  
    glPopMatrix()

    # Circulo grande para el campo situado en el palo de baloncesto izq
    glPushMatrix()
    glTranslatef(65.50, 2.7, -68.0)
    glRotatef(90, 1.0, 0.0, 0.0)  
    glRotatef(90, 0.0, 0.0, 1.0)
    draw_half_circle(6, 100) 
    glPopMatrix()

    # Lado DER   
    # Circulo pequenio para el campo situado en el palo de baloncesto derecho
    glPushMatrix()
    glTranslatef(65.50, 2.7, -39.0)
    glRotatef(90, 1.0, 0.0, 0.0)  
    glRotatef(270, 0.0, 0.0, 1.0)
    draw_half_circle(0.7, 100)  
    glPopMatrix()

    # Circulo mediano para el campo situado en el palo de baloncesto derecho
    glPushMatrix()
    glTranslatef(65.50, 2.7, -43.0) 
    glRotatef(90, 1.0, 0.0, 0.0)  
    glRotatef(270, 0.0, 0.0, 1.0)
    draw_half_circle(1.5, 100)  
    glPopMatrix()

    # Circulo grande para el campo situado en el palo de baloncesto derecho
    glPushMatrix()
    glTranslatef(65.50, 2.7, -39.0)
    glRotatef(90, 1.0, 0.0, 0.0)  
    glRotatef(270, 0.0, 0.0, 1.0)
    draw_half_circle(6, 100)  
    glPopMatrix()

    # CIRCULO MEDIO
    glPushMatrix()
    glTranslatef(65.50, 2.7, -53.5)
    glRotatef(90, 1.0, 0.0, 0.0)
    glColor3f(1.0, 1.0, 1.0)  
    draw_circle(2.0, 100)  
    glPopMatrix()
    # Fin de loza deportiva 
    
    # Dibujar las líneas si están habilitadas
    

    if linea2:
        # Camino entre Edificio 1 y Edificio 2 (amarillo, línea recta)
        glColor3f(1.0, 1.0, 0.0)
        glBegin(GL_LINES)
        glVertex3f(*puerta_upn)
        glVertex3f(-15.0, 5.5, -15.0)  # Primer punto intermedio
        glVertex3f(-15.0, 5.7, -30.0)  # Segundo punto intermedio
        glVertex3f(*pabellon_a)
        glEnd()

        glColor3f(1.0, 1.0, 0.0)  # Cambia el color a otro (por ejemplo, cian)
        glBegin(GL_LINES)
        glVertex3f(-25.0, 5.7, -30.0)  # z = rectitud
        glVertex3f(-15.0, 5.7, -30.0)  # z = rectitud
        glEnd()

    if linea3:
        glColor3f(1.0, 1.0, 0.0)
        glBegin(GL_LINES)
        glVertex3f(*puerta_upn)
        glVertex3f(60.3, 5.5, -15.0)  # Primer punto intermedio
        glVertex3f(60.0, 5.7, -15.0)
        glVertex3f(*losa_deportiva)
        glEnd()

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
    gluPerspective(45, width / height, 1, 500)
    glMatrixMode(GL_MODELVIEW)

def keyboard(key, x, y):
    global camera_distance, camera_angle_x, camera_angle_y,linea2, linea3
    
    if key == b'1':  # Comprobar si se presiona el número '2' (amarillo)
        linea2 = not linea2  # Alternar la visibilidad de la línea amarilla
        glutPostRedisplay()  # Solicitar redibujar la escena

    if key == b'3':
        linea3 = not linea3
        glutPostRedisplay

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
    
def draw_menu_window():
    """Dibuja el contenido de la ventana del menú."""
    glClear(GL_COLOR_BUFFER_BIT)

    # Fondo del menú
    glColor3f(0.1, 0.1, 0.1)  # Gris oscuro
    glBegin(GL_QUADS)
    glVertex2f(0, 0)
    glVertex2f(300, 0)
    glVertex2f(300, 500)
    glVertex2f(0, 500)
    glEnd()

    # Título del menú
    glColor3f(1, 1, 1)
    glRasterPos2f(10, 470)
    for char in "MENU (Presionar la tecla numerica correspondiente)":
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))

    # Dibujar botones
    button_height = 40
    for i, item in enumerate(menu_items):
        y_position = 420 - i * (button_height + 10)
        draw_button(10, y_position, 290, y_position + button_height, item)

    glutSwapBuffers()

def draw_button(x1, y1, x2, y2, text):
    """Dibuja un botón en la ventana del menú."""
    glColor3f(0.3, 0.3, 0.3)  # Fondo del botón
    glBegin(GL_QUADS)
    glVertex2f(x1, y1)
    glVertex2f(x2, y1)
    glVertex2f(x2, y2)
    glVertex2f(x1, y2)
    glEnd()

    # Borde del botón
    glColor3f(1, 1, 1)
    glBegin(GL_LINE_LOOP)
    glVertex2f(x1, y1)
    glVertex2f(x2, y1)
    glVertex2f(x2, y2)
    glVertex2f(x1, y2)
    glEnd()

    # Texto del botón
    glRasterPos2f(x1 + 10, y1 + 15)
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(char))

def open_menu_window():
    """Crea la ventana del menú."""
    global menu_window
    glutInitWindowSize(300, 500)
    glutInitWindowPosition(100, 100)
    menu_window = glutCreateWindow("Menú Interactivo")
    glutDisplayFunc(draw_menu_window)
    glClearColor(0.2, 0.2, 0.2, 1.0)  # Fondo gris oscuro
    glOrtho(0, 300, 0, 500, -1, 1)

def keyboard_with_menu(key, x, y):
    """Control del teclado, incluyendo la apertura del menú."""
    if key == b'm':  # Abrir menú en una nueva ventana
        if not menu_window:
            open_menu_window()
        else:
            glutSetWindow(menu_window)
    else:
        keyboard(key, x, y)  # Llamar a la función de teclado original

def main():
    global main_window
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(1600, 900)
    main_window = glutCreateWindow(b"Entorno Interactivo UPN")
    init()
    glutDisplayFunc(draw_scene)
    glutReshapeFunc(reshape)
    glutMouseFunc(mouse_button)
    glutMotionFunc(mouse_motion)
    glutKeyboardFunc(keyboard_with_menu)  # Función de teclado extendida
    glutMainLoop()



if __name__ == "__main__":
    main()