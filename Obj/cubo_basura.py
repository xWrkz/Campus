import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Variables globales para almacenar vértices y caras
vertices = []
faces = []

def load_obj(file_path):
    global vertices, faces
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('v '):  # Lee vértices
                _, x, y, z = line.strip().split()
                vertices.append((float(x), float(y), float(z)))
            elif line.startswith('f '):  # Lee caras
                face = [int(idx.split('/')[0]) - 1 for idx in line.strip().split()[1:]]
                faces.append(face)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glBegin(GL_TRIANGLES)
    for face in faces:
        for vertex_idx in face:
            glVertex3fv(vertices[vertex_idx])
    glEnd()
    glutSwapBuffers()

def init_gl(width, height):
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glShadeModel(GL_FLAT)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45.0, float(width) / float(height), 1.0, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glTranslatef(0.0, 0.0, -5)

def main():
    # Especifica la ruta completa a tu archivo .obj en el escritorio
    obj_file_path = "C:/Users/Michael/Desktop/basura.obj"  # Cambia esta ruta a la ubicación de tu archivo

    # Carga el modelo
    load_obj(obj_file_path)

    # Inicializa OpenGL y muestra el modelo
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(640, 480)
    glutCreateWindow("Modelo 3D sin Textura")
    glutDisplayFunc(display)
    init_gl(640, 480)
    glutMainLoop()

if __name__ == "__main__":
    main()
