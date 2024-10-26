import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QOpenGLWidget
from OpenGL.GL import *
from OpenGL.GLU import *
from PyQt5.QtCore import Qt
from math import sin, cos, radians

class OpenGLWidget(QOpenGLWidget):
    def __init__(self):
        super(OpenGLWidget, self).__init__()
        self.setMinimumSize(800, 600)

        # Variables de cámara
        self.camera_pos = [0.0, 5.0, 20.0]  # Posición de la cámara en XYZ
        self.camera_target = [0.0, 0.0, 0.0]  # Punto hacia el que mira la cámara
        self.yaw = 0.0    # Ángulo horizontal
        self.pitch = 0.0  # Ángulo vertical

        # Para detectar el estado de las teclas
        self.keys = {}

    def initializeGL(self):
        glEnable(GL_DEPTH_TEST)
        glClearColor(0.5, 0.5, 0.5, 1)

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, w / h, 1.0, 100.0)
        glMatrixMode(GL_MODELVIEW)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        # Calcular la posición de la cámara con rotación
        cam_x = self.camera_pos[0] + 10 * sin(self.yaw)
        cam_y = self.camera_pos[1] + 10 * sin(self.pitch)
        cam_z = self.camera_pos[2] + 10 * cos(self.yaw)

        gluLookAt(
            cam_x, cam_y, cam_z,
            self.camera_target[0], self.camera_target[1], self.camera_target[2],
            0, 1, 0
        )

        # Dibujar el plano base y objetos
        self.draw_plane((0, 0, 0), (30, 1, 30))
        self.draw_cubes()
        self.draw_new_planes()
        self.draw_new_cubes()

        # Actualiza la posición y dirección de la cámara
        self.move_camera()

    def move_camera(self):
        # Avanzar y retroceder
        if self.keys.get(Qt.Key_W):
            self.camera_pos[2] -= 0.5  # Avanza en Z
        if self.keys.get(Qt.Key_S):
            self.camera_pos[2] += 0.5  # Retrocede en Z

        # Rotaciones
        if self.keys.get(Qt.Key_A):
            self.yaw -= 0.05  # Rotación a la izquierda
        if self.keys.get(Qt.Key_D):
            self.yaw += 0.05  # Rotación a la derecha
        if self.keys.get(Qt.Key_Q):
            self.camera_pos[1] += 0.5  # Sube en Y
        if self.keys.get(Qt.Key_E):
            self.camera_pos[1] -= 0.5  # Baja en Y
        if self.keys.get(Qt.Key_Up):
            self.pitch += 0.05  # Rotación hacia arriba
        if self.keys.get(Qt.Key_Down):
            self.pitch -= 0.05  # Rotación hacia abajo

        # Normalizar los ángulos
        self.yaw = self.yaw % (2 * 3.14159)  # Normalizar yaw entre 0 y 2π
        self.pitch = max(-1.57, min(self.pitch, 1.57))  # Limitar pitch entre -π/2 y π/2

    def keyPressEvent(self, event):
        self.keys[event.key()] = True  # Marcar la tecla como presionada
        self.update()  # Redibuja la escena

    def keyReleaseEvent(self, event):
        self.keys[event.key()] = False  # Marcar la tecla como no presionada

    def draw_plane(self, position, scale):
        glPushMatrix()
        glTranslatef(*position)
        glScalef(*scale)

        glBegin(GL_QUADS)
        glColor3f(0.3, 0.3, 0.3)
        glVertex3f(-0.5, 0, -0.5)
        glVertex3f(0.5, 0, -0.5)
        glVertex3f(0.5, 0, 0.5)
        glVertex3f(-0.5, 0, 0.5)
        glEnd()

        glPopMatrix()

    def draw_cubes(self):
        self.draw_cube((-10, 1, 3.6), (5, 2, 3), (0, 0, 0))
        self.draw_cube((12.861, 1, 3.6), (5, 2, 3), (0, 0, 0))
        self.draw_cube((9.66, 5, 9.5), (6.94, 1.8, 3), (0, 0, -90))
        self.draw_cube((-6.81, 5, 9.5), (6.94, 1.8, 3), (0, 0, -90))
        self.draw_cube((-6.8, 6.5, 3.6), (5, 1.78, 3), (0, 0, -90))
        self.draw_cube((-9.65, 7, 3.6), (5, 1.78, 3), (0, 0, -90))

    def draw_new_planes(self):
        self.draw_plane((1.3815, 0, 5.5682), (6.56, 1.02, 3))
        self.draw_plane((1.074, 1.25, 10), (7, 5.5, 1))

    def draw_new_cubes(self):
        positions = [(-2.4225, 1, 8.2858), (1.582, 1, 8.2858), (5.7811, 1, 8.2858)]
        scale = (0.25, 0.20, 1.71)
        for position in positions:
            self.draw_cube(position, scale, (0, 0, 0))

    def draw_cube(self, position, scale, rotation):
        glPushMatrix()
        glTranslatef(*position)
        glScalef(*scale)
        glRotatef(rotation[0], 1, 0, 0)
        glRotatef(rotation[1], 0, 1, 0)
        glRotatef(rotation[2], 0, 0, 1)

        vertices = [
            (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1),
            (1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1)
        ]

        glBegin(GL_LINES)
        edges = [
            (0, 1), (1, 2), (2, 3), (3, 0),
            (4, 5), (5, 7), (7, 6), (6, 4),
            (0, 4), (1, 5), (2, 7), (3, 6)
        ]
        glColor3f(1, 1, 1)
        for edge in edges:
            for vertex in edge:
                glVertex3fv(vertices[vertex])
        glEnd()

        glPopMatrix()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.opengl_widget = OpenGLWidget()
        self.setCentralWidget(self.opengl_widget)
        self.setWindowTitle("OpenGL with PyQt5")
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
