import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Definimos los vértices de un prisma rectangular más grande
vertices = [
    (2, 1, -1),   # Vértice superior derecho frontal
    (2, -1, -1),  # Vértice inferior derecho frontal
    (-2, -1, -1), # Vértice inferior izquierdo frontal
    (-2, 1, -1),  # Vértice superior izquierdo frontal
    (2, 1, 1),    # Vértice superior derecho trasero
    (2, -1, 1),   # Vértice inferior derecho trasero
    (-2, -1, 1),  # Vértice inferior izquierdo trasero
    (-2, 1, 1),   # Vértice superior izquierdo trasero
]

# Definimos las caras del prisma (cada cara está definida por 4 vértices)
faces = [
    (0, 1, 2, 3),  # Cara frontal
    (3, 2, 6, 7),  # Cara izquierda
    (7, 6, 5, 4),  # Cara trasera
    (4, 5, 1, 0),  # Cara derecha
    (1, 5, 6, 2),  # Cara inferior
    (4, 0, 3, 7),  # Cara superior
]

# Función para dibujar el prisma rectangular
def draw_prism():
    glBegin(GL_QUADS)  # Usamos GL_QUADS para las caras
    glColor3f(0.5, 0.5, 0.5)  # Color gris
    for face in faces:
        for vertex in face:
            glVertex3fv(vertices[vertex])  # Dibujamos cada vértice de la cara
    glEnd()

    # Opcional: Dibujar las aristas
    glBegin(GL_LINES)  # Dibujamos las aristas
    for face in faces:
        for i in range(len(face)):
            glVertex3fv(vertices[face[i]])
            glVertex3fv(vertices[face[(i + 1) % len(face)]])  # Conectar al siguiente vértice
    glEnd()

# Función para dibujar las puertas
def draw_doors():
    glBegin(GL_QUADS)  # Usamos GL_QUADS para las puertas
    glColor3f(0.0, 0.75, 1.0)  # Color celeste

    # Puerta izquierda (en la cara derecha del prisma)
    glVertex3f(1.6, -1.0, 1)  # Vértice inferior derecho
    glVertex3f(1.6, 0.5, 1)   # Vértice superior derecho
    glVertex3f(0.7, 0.5, 1)   # Vértice superior izquierdo
    glVertex3f(0.7, -1.0, 1)  # Vértice inferior izquierdo

    # Puerta derecha (en la cara derecha del prisma)
    glVertex3f(-1.0, -1.0, 1)  # Vértice inferior derecho
    glVertex3f(-1.0, 0.5, 1)   # Vértice superior derecho
    glVertex3f(-0.2, 0.5, 1)   # Vértice superior izquierdo
    glVertex3f(-0.2, -1.0, 1)  # Vértice inferior izquierdo

    glEnd()

# Inicializamos Pygame y OpenGL
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)  # Configuramos la perspectiva
    glTranslatef(0.0, 0.0, -8)  # Movemos la cámara hacia atrás para ver el prisma más grande

    while True:
        for event in pygame.event.get():
            if event.type == pygame .QUIT:
                pygame.quit()
                return

        glRotatef(1, 0, 1, 0)  # Rotamos el prisma
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Limpiamos la pantalla
        draw_prism()  # Dibujamos el prisma
        draw_doors()  # Dibujamos las puertas
        pygame.display.flip()  # Actualizamos la pantalla
        pygame.time.wait(10)  # Esperamos un poco

if __name__ == "__main__":
    main()