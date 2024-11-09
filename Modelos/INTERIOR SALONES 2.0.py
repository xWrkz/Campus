# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 21:46:10 2024

@author: Diego
"""

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Variables para la posición de la cámara
camera_pos = [0, 10, 15]  # Posición inicial de la cámara

# Función para inicializar la ventana y las configuraciones de OpenGL
def init():
    glClearColor(0.53, 0.81, 0.92, 1.0)  # Color de fondo: azul claro
    glEnable(GL_DEPTH_TEST)  # Habilitar el buffer de profundidad

# Función para dibujar el salón de clases
def draw_classroom():
    # Limpiar el buffer de color y profundidad
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Colocar la cámara en una vista aérea
    gluLookAt(camera_pos[0], camera_pos[1], camera_pos[2], 0, 0, 0, 0, 1, 0)

    # Dibujar las paredes
    draw_walls()

    # Dibujar el suelo
    glBegin(GL_QUADS)
    glColor3f(0.6, 0.6, 0.6)  # Color del suelo (gris)
    glVertex3f(-10, -1, -10)
    glVertex3f(10, -1, -10)
    glVertex3f(10, -1, 10)
    glVertex3f(-10, -1, 10)
    glEnd()

    # Dibujar mesas y sillas en columnas, ahora más dispersas
    for i in range(-2, 3):  # Aumentar el espaciado entre las mesas
        for j in range(-2, 2):  # Aumentar el espaciado entre las mesas
            draw_table(i * 3, 0, j * 3)  # Multiplicar por 3 para dispersar

    # Dibujar la pizarra
    draw_blackboard()

    glutSwapBuffers()

# Función para dibujar las paredes
def draw_walls():
    wall_height = 3  # Altura de las paredes
    wall_color = (0.5, 0.5, 0.5)  # Color gris de las paredes

    # Paredes alrededor del salón
    glBegin(GL_QUADS)

    # Pared frontal
    glColor3fv(wall_color)
    glVertex3f(-10, -1, 10)  # Esquina inferior izquierda
    glVertex3f(10, -1, 10)   # Esquina inferior derecha
    glVertex3f(10, wall_height, 10)  # Esquina superior derecha
    glVertex3f(-10, wall_height, 10)  # Esquina superior izquierda

    # Pared trasera
    glVertex3f(-10, -1, -10)  # Esquina inferior izquierda
    glVertex3f(10, -1, -10)   # Esquina inferior derecha
    glVertex3f(10, wall_height, -10)  # Esquina superior derecha
    glVertex3f(-10, wall_height, -10)  # Esquina superior izquierda

    # Pared izquierda
    glVertex3f(-10, -1, -10)  # Esquina inferior izquierda
    glVertex3f(-10, -1, 10)   # Esquina inferior derecha
    glVertex3f(-10, wall_height, 10)  # Esquina superior derecha
    glVertex3f(-10, wall_height, -10)  # Esquina superior izquierda

    # Pared derecha
    glVertex3f(10, -1, -10)  # Esquina inferior izquierda
    glVertex3f(10, -1, 10)   # Esquina inferior derecha
    glVertex3f(10, wall_height, 10)  # Esquina superior derecha
    glVertex3f(10, wall_height, -10)  # Esquina superior izquierda

    glEnd()

# Función para dibujar una mesa
def draw_table(x, y, z):
    # Dibujar el tablero de la mesa
    glPushMatrix()
    glTranslatef(x, y, z)
    glScalef(1.5, 0.1, 1)
    glColor3f(0.55, 0.27, 0.07)  # Color madera
    glutSolidCube(1)
    glPopMatrix()

    # Dibujar las patas de la mesa
    for i in [-0.7, 0.7]:
        for j in [-0.4, 0.4]:
            glPushMatrix()
            glTranslatef(x + i, y - 0.5, z + j)
            glScalef(0.1, 1, 0.1)
            glColor3f(0.2, 0.2, 0.2)  # Color de las patas (gris oscuro)
            glutSolidCube(1)
            glPopMatrix()

    # Dibujar silla detrás de la mesa
    draw_chair(x, y, z - 1.5)  # Silla detrás de la mesa

# Función para dibujar una silla
def draw_chair(x, y, z):
    # Asiento de la silla
    glPushMatrix()
    glTranslatef(x, y, z)  # Mantener el nivel del suelo
    glScalef(0.6, 0.1, 0.6)
    glColor3f(0.55, 0.27, 0.07)  # Color madera
    glutSolidCube(1)
    glPopMatrix()

    # Patas de la silla
    for dx, dz in [(-0.25, -0.25), (0.25, -0.25), (-0.25, 0.25), (0.25, 0.25)]:
        glPushMatrix()
        glTranslatef(x + dx, y - 0.5, z + dz)  # Patas deben estar un poco más abajo
        glScalef(0.1, 1, 0.1)
        glColor3f(0.2, 0.2, 0.2)  # Color de las patas (gris oscuro)
        glutSolidCube(1)
        glPopMatrix()
    
    # Respaldo de la silla
    glPushMatrix()
    glTranslatef(x, y + 0.4, z - 0.3)  # Ajustar el respaldo
    glScalef(0.6, 0.8, 0.1)  # Dimensiones del respaldo
    glColor3f(0.55, 0.27, 0.07)  # Color madera
    glutSolidCube(1)
    glPopMatrix()

# Función para dibujar la pizarra
def draw_blackboard():
    glPushMatrix()
    glTranslatef(0, 2, 9.5)  # Colocar la pizarra en el lado opuesto
    glRotatef(180, 0, 1, 0)  # Girar la pizarra para que mire hacia el salón
    glScalef(6, 3, 0.1)
    glColor3f(1.0, 1.0, 1.0)  # Color blanco para la pizarra
    glutSolidCube(1)

    glPopMatrix()

# Función para manejar el movimiento del mouse
def mouse_motion(x, y):
    global camera_pos
    camera_pos[0] = (x - 400) / 40.0  # Escalar posición x
    camera_pos[2] = (300 - y) / 40.0  # Escalar posición z

# Función para manejar el redimensionamiento de la ventana
def resize(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, w / h, 1, 50)
    glMatrixMode(GL_MODELVIEW)

# Función principal para configurar la ventana y los callbacks
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow("Salón de Clases 3D")
    init()
    glutDisplayFunc(draw_classroom)
    glutIdleFunc(draw_classroom)
    glutMotionFunc(mouse_motion)  # Mover la cámara con el mouse
    glutReshapeFunc(resize)
    glutMainLoop()

if __name__ == "__main__":
    main()
