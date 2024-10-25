import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtOpenGL import QOpenGLWidget
from OpenGL.GL import *
from OpenGL.GLU import *
from PyQt5.QtCore import Qt

class OpenGLWidget(QOpenGLWidget):
    def __init__(self):
        super(OpenGLWidget, self).__init__()
        self.setMinimumSize(800, 600)
        
        # Variables de cámara
        self.camera_pos = [0.0, 0.0, -15.0]
        self.camera_angle = [0.0, 0.0]  # (yaw, pitch)

    def initializeGL(self):
        glEnable(GL_DEPTH_TEST)
        glClearColor(0.1, 0.1, 0.1, 1)

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, w / h, 0.1, 50.0)
        glMatrixMode(GL_MODELVIEW)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        # Configurar la cámara
        self.setup_camera()

        # Dibuja el plano base
        self.draw_plane((0.021057, 5, 0.71124), (30, 10, 1))

        # Dibuja el primer nuevo plano
        self.draw_new_plane((1.3815, 5, 5.5682), (6.56, 1.02, 3), (90, 0, 0))

        # Dibuja el segundo nuevo plano
        self.draw_new_plane((1.074, 2.51, 10), (7, 5.5, 1), (0, 0, 0))

        # Dibuja los cubos existentes
        self.draw_cubes()

        # Dibuja los nuevos cubos
        self.draw_new_cubes()

    def setup_camera(self):
        # Calcula la dirección de la cámara usando ángulos
        yaw_rad = self.camera_angle[0] * (3.14159 / 180.0)
        pitch_rad = self.camera_angle[1] * (3.14159 / 180.0)

        # Dirección de la cámara
        cam_dir_x = -1 * (abs(yaw_rad))
        cam_dir_y = abs(pitch_rad)
        cam_dir_z = -1 * (abs(yaw_rad))

        gluLookAt(
            self.camera_pos[0], self.camera_pos[1], self.camera_pos[2],
            self.camera_pos[0] + cam_dir_x, self.camera_pos[1] + cam_dir_y, self.camera_pos[2] + cam_dir_z,
            0, 1, 0
        )

    def draw_cubes(self): #base fachada
        # Primer par de cubos
        self.draw_cube((-10, -1.054, 3.6), (5, 2, 3), (0, 0, 0))
        self.draw_cube((12.861, -0.726, 3.6), (5, 2, 3), (0, 0, 0))

        # Segundo par de cubos
        self.draw_cube((9.66, 4.22, 9.5298), (6.940, 1.8, 3), (0, 0, -90))
        self.draw_cube((-6.81, 3.88, 9.5298), (6.940, 1.8, 3), (0, 0, -90))

        # Tercer par de cubos
        self.draw_cube((-6.8041, 5.796, 3.6), (5, 1.78, 3), (0, 0, -90))
        self.draw_cube((-9.6482, 6.1733, 3.6), (5, 1.78, 3), (0, 0, -90))

    def draw_new_cubes(self): #soporte cartel
        # Dibuja los nuevos cubos
        positions = [
            (-2.4225, 5, 8.2858),
            (1.582, 5, 8.2858),
            (5.7811, 5, 8.2858)
        ]
        scale = (0.25, 0.20, 1.710)
        rotation = (0, 0, 0)

        for position in positions:
            self.draw_cube(position, scale, rotation)

    def draw_cube(self, position, scale, rotation):
        glPushMatrix()
        glTranslatef(*position)  # Trasladar a la posición
        glScalef(*scale)         # Escalar
        glRotatef(rotation[0], 1, 0, 0)  # Rotar alrededor del eje X
        glRotatef(rotation[1], 0, 1, 0)  # Rotar alrededor del eje Y
        glRotatef(rotation[2], 0, 0, 1)  # Rotar alrededor del eje Z
        
        # Define los vértices del cubo
        vertices = [
            (1, -1, -1),
            (1, 1, -1),
            (-1, 1, -1),
            (-1, -1, -1),
            (1, -1, 1),
            (1, 1, 1),
            (-1, -1, 1),
            (-1, 1, 1)
        ]

        # Dibuja las aristas del cubo
        glBegin(GL_LINES)
        edges = [
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 0),
            (4, 5),
            (5, 7),
            (7, 6),
            (6, 4),
            (0, 4),
            (1, 5),
            (2, 7),
            (3, 6)
        ]
        for edge in edges:
            for vertex in edge:
                glVertex3fv(vertices[vertex])
        glEnd()
        
        glPopMatrix()

    def draw_plane(self, position, scale):
        glPushMatrix()
        glTranslatef(*position)  # Trasladar a la posición
        glScalef(*scale)         # Escalar
        
        glBegin(GL_QUADS)
        glVertex3f(-0.5, 0, -0.5)
        glVertex3f(0.5, 0, -0.5)
        glVertex3f(0.5, 0, 0.5)
        glVertex3f(-0.5, 0, 0.5)
        glEnd()
        
        glPopMatrix()

    def draw_new_plane(self, position, scale, rotation):
        glPushMatrix()
        glTranslatef(*position)  # Trasladar a la posición
        glScalef(*scale)         # Escalar
        glRotatef(rotation[0], 1, 0, 0)  # Rotar alrededor del eje X
        glRotatef(rotation[1], 0, 1, 0)  # Rotar alrededor del eje Y
        glRotatef(rotation[2], 0, 0, 1)  # Rotar alrededor del eje Z
        
        glBegin(GL_QUADS)
        glVertex3f(-0.5, 0, -0.5)
        glVertex3f(0.5, 0, -0.5)
        glVertex3f(0.5, 0, 0.5)
        glVertex3f(-0.5, 0, 0.5)
        glEnd()
        
        glPopMatrix()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_W:  # Mover cámara hacia adelante
            self.camera_pos[2] += 0.5
        elif event.key() == Qt.Key_S:  # Mover cámara hacia atrás
            self.camera_pos[2] -= 0.5
        elif event.key() == Qt.Key_A:  # Rotar a la izquierda
            self.camera_angle[0] -= 5
        elif event.key() == Qt.Key_D:  # Rotar a la derecha
            self.camera_angle[0] += 5
        elif event.key() == Qt.Key_Q:  # Mirar hacia arriba
            self.camera_angle[1] += 5
        elif event.key() == Qt.Key_E:  # Mirar hacia abajo
            self.camera_angle[1] -= 5

        self.update()  # Redibuja la escena

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
