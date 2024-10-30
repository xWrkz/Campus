# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 20:46:21 2024

@author: Diego
"""

import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Variables globales
angle_x, angle_y = 0, 0  # Ángulos de rotación para la cámara
mouse_down = False
last_mouse_x, last_mouse_y = 0, 0

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Color de fondo blanco
    glEnable(GL_DEPTH_TEST)

def draw_chair():
    # Dibuja la silla (asiento)
    glPushMatrix()
    glColor3f(1.0, 0.5, 0.0)  # Color naranja
    glScalef(0.5, 0.1, 0.5)  # Escala para simular el asiento
    glutSolidCube(1)
    glPopMatrix()

    # Dibuja las patas de la silla (4 cilindros delgados)
    glColor3f(0.5, 0.5, 0.5)  # Color gris
    for x, z in [(-0.2, -0.2), (-0.2, 0.2), (0.2, -0.2), (0.2, 0.2)]:
        glPushMatrix()
        glTranslatef(x, -0.35, z)  # Coloca las patas en las esquinas del asiento
        glScalef(0.05, 0.7, 0.05)  # Cilindros delgados y altos
        glutSolidCube(1)
        glPopMatrix()

    # Dibuja el respaldo de la silla
    glPushMatrix()
    glColor3f(1.0, 0.5, 0.0)  # Color naranja
    glTranslatef(0.0, 0.35, -0.25)  # Coloca el respaldo detrás del asiento
    glScalef(0.5, 0.5, 0.05)  # Escala delgada para el respaldo
    glutSolidCube(1)
    glPopMatrix()

def draw_table():
    # Dibuja una mesa ovalada
    glPushMatrix()
    glColor3f(1.0, 1.0, 1.0)  # Color blanco
    glTranslatef(0.0, 0.5, 0.0)
    glScalef(1.5, 0.1, 1.0)  # Escala diferente en x y z para hacerla ovalada
    glutSolidSphere(1, 20, 20)
    glPopMatrix()

    # Dibuja las patas de la mesa (cilindros)
    glColor3f(0.5, 0.5, 0.5)  # Gris
    for i in range(4):
        angle = i * math.pi / 2
        x = 0.7 * math.cos(angle)
        z = 0.7 * math.sin(angle)
        glPushMatrix()
        glTranslatef(x, -0.5, z)
        glScalef(0.1, 1.0, 0.1)
        glutSolidCube(1)
        glPopMatrix()

def draw_walls():
    # Dibujar las 4 paredes alrededor del comedor alineadas al ras del piso
    glColor3f(0.6, 0.6, 0.6)  # Gris claro
    wall_height = 1.0
    wall_thickness = 0.1
    wall_length = 12.0

    # Pared del fondo
    glPushMatrix()
    glTranslatef(0.0, 0.5 * wall_height - 0.51, -6.0)
    glScalef(wall_length, wall_height, wall_thickness)
    glutSolidCube(1)
    glPopMatrix()

    # Pared del frente
    glPushMatrix()
    glTranslatef(0.0, 0.5 * wall_height - 0.51, 6.0)
    glScalef(wall_length, wall_height, wall_thickness)
    glutSolidCube(1)
    glPopMatrix()

    # Pared lateral izquierda
    glPushMatrix()
    glTranslatef(-6.0, 0.5 * wall_height - 0.51, 0.0)
    glScalef(wall_thickness, wall_height, wall_length)
    glutSolidCube(1)
    glPopMatrix()

    # Pared lateral derecha
    glPushMatrix()
    glTranslatef(6.0, 0.5 * wall_height - 0.51, 0.0)
    glScalef(wall_thickness, wall_height, wall_length)
    glutSolidCube(1)
    glPopMatrix()

def draw_floor():
    # Dibujar el piso marrón en la base
    glColor3f(0.55, 0.27, 0.07)  # Marrón
    glPushMatrix()
    glTranslatef(0.0, -0.51, 0.0)  # Ligeramente debajo de las mesas y sillas
    glScalef(12.0, 0.1, 12.0)  # Piso grande
    glutSolidCube(1)
    glPopMatrix()

def draw_scene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Configura la vista aérea por defecto
    gluLookAt(0.0, 10.0, 10.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    # Rotación de la escena según el movimiento del mouse
    glRotatef(angle_x, 1.0, 0.0, 0.0)
    glRotatef(angle_y, 0.0, 1.0, 0.0)

    # Dibujar el piso
    draw_floor()

    # Dibujar las paredes
    draw_walls()

    # Dibujar las mesas y sillas dentro de los límites de las paredes
    for i in range(-1, 2):  # Filas de mesas
        for j in range(-1, 2):  # Columnas de mesas
            glPushMatrix()
            glTranslatef(i * 3.5, 0.0, j * 3.5)

            # Dibuja la mesa
            draw_table()

            # Dibuja las sillas (alrededor de la mesa)
            for x, z in [(1.8, 0.0), (-1.8, 0.0), (0.0, 1.8), (0.0, -1.8)]:
                glPushMatrix()
                glTranslatef(x, 0.0, z)
                draw_chair()
                glPopMatrix()

            glPopMatrix()

    glutSwapBuffers()

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, w / h, 1, 50.0)
    glMatrixMode(GL_MODELVIEW)

def mouse_motion(x, y):
    global last_mouse_x, last_mouse_y, angle_x, angle_y, mouse_down
    if mouse_down:
        angle_y += (x - last_mouse_x) * 0.2
        angle_x += (y - last_mouse_y) * 0.2
        last_mouse_x, last_mouse_y = x, y
        glutPostRedisplay()

def mouse_button(button, state, x, y):
    global mouse_down, last_mouse_x, last_mouse_y
    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            mouse_down = True
            last_mouse_x, last_mouse_y = x, y
        elif state == GLUT_UP:
            mouse_down = False

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow("Comedor 3D")

    init()

    glutDisplayFunc(draw_scene)
    glutReshapeFunc(reshape)
    glutMouseFunc(mouse_button)
    glutMotionFunc(mouse_motion)
    glutMainLoop()

if __name__ == "__main__":
    main()
