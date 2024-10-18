import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np

# Dimensiones del edificio
width = 10
depth = 8
height = 4
floor_height = height / 4

def draw_building():
    glBegin(GL_QUADS)

    # Pisos
    for i in range(4):
        z = i * floor_height
        # Base
        glColor3f(0.8, 0.5, 0.2)  # Color marrón
        glVertex3f(-width/2, -depth/2, z)
        glVertex3f(width/2, -depth/2, z)
        glVertex3f(width/2, depth/2, z)
        glVertex3f(-width/2, depth/2, z)

    # Terraza
    z = height
    glColor3f(0.6, 0.3, 0.1)  # Color más claro
    glVertex3f(-width/2, -depth/2, z)
    glVertex3f(width/2, -depth/2, z)
    glVertex3f(width/2, depth/2, z)
    glVertex3f(-width/2, depth/2, z)

    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0, 0, -20)  # Mueve la cámara hacia atrás

    draw_building()

    glutSwapBuffers()

def init():
    glEnable(GL_DEPTH_TEST)
    glClearColor(1, 1, 1, 1)

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-15, 15, -15, 15, -100, 100)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow("Edificio 3D")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()

if __name__ == "__main__":
    main()
