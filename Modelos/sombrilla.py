import sys
from PyQt5.QtWidgets import QApplication, QOpenGLWidget
from PyQt5.QtCore import Qt
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import gluPerspective, gluCylinder, gluNewQuadric

class SombrillaApp(QOpenGLWidget):
    def __init__(self):
        super().__init__()
        self.angle_x = 0  
        self.angle_y = 0 
        self.zoom = -6  # Control de zoom (más cercano)
        self.last_mouse_x = 0
        self.last_mouse_y = 0
        self.mouse_down = False

    def initializeGL(self):
        glEnable(GL_DEPTH_TEST)
        glClearColor(0.2, 0.3, 0.4, 1.0)

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, w / h, 0.1, 100)
        glMatrixMode(GL_MODELVIEW)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, self.zoom)  # Control de la distancia de la cámara

        # Aplicar rotaciones
        glRotatef(self.angle_x, 1, 0, 0)
        glRotatef(self.angle_y, 0, 1, 0)

        # Dibujar la sombrilla
        self.dibujar_sombrilla(0, 0)  # Centrado en el origen (0,0)

        glFlush()

    def dibujar_sombrilla(self, x, z):
        # Dibujar el palo de la sombrilla (cilindro)
        glColor3f(0.5, 0.5, 0.5)  # Color madera
        glPushMatrix()
        glTranslatef(x, 1.0, z-2.6)  # Mover el cilindro para que se alinee con el centro
        gluCylinder(gluNewQuadric(), 0.05, 0.05, 3.5, 16, 16)  # Crear cilindro (palo)
        glPopMatrix()

        # Dibujar la cubierta de la sombrilla (cono invertido)
        glColor3f(1.0, 1.0, 1.0)  # Color blanco para el cono
        glPushMatrix()
        glTranslatef(x, 1, z)  # Mover el cono encima del palo
        gluCylinder(gluNewQuadric(), 3.0, 0.0, 1.0, 16, 16)  # Crear cono invertido
        glPopMatrix()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:
            self.angle_y -= 5
        elif event.key() == Qt.Key_Right:
            self.angle_y += 5
        elif event.key() == Qt.Key_Up:
            self.angle_x -= 5
        elif event.key() == Qt.Key_Down:
            self.angle_x += 5
        self.update()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mouse_down = True
            self.last_mouse_x = event.x()
            self.last_mouse_y = event.y()

    def mouseMoveEvent(self, event):
        if self.mouse_down:
            dx = event.x() - self.last_mouse_x
            dy = event.y() - self.last_mouse_y
            self.angle_y += dx * 0.5
            self.angle_x += dy * 0.5
            self.last_mouse_x = event.x()
            self.last_mouse_y = event.y()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mouse_down = False

    def wheelEvent(self, event):
        # Acercar o alejar la cámara con la rueda del mouse
        delta = event.angleDelta().y()
        if delta > 0:
            self.zoom += 0.1  # Alejar
        else:
            self.zoom -= 0.1  # Acercar
        self.update()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SombrillaApp()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec_())
