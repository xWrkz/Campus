import sys
from PyQt5.QtWidgets import QApplication, QOpenGLWidget
from PyQt5.QtCore import Qt
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import gluPerspective

class MesaApp(QOpenGLWidget):
    def __init__(self):
        super().__init__()
        self.angle_x = 0 
        self.angle_y = 0 
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
        gluPerspective(60, w / h, 0.1, 100)
        glMatrixMode(GL_MODELVIEW)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glFrustum(-1, 1, -1, 1, 2, 100)

        glRotatef(self.angle_x, 1, 0, 0)
        glRotatef(self.angle_y, 0, 1, 0)

        self.dibujar_mesa(0, 0, ancho=1.8, largo=1., alto=0.8)

        glFlush()

    def dibujar_mesa(self, x, z, ancho=1.2, largo=0.8, alto=0.8):

        glColor3f(0.7, 0.5, 0.2)

        mitad_ancho = ancho / 2
        mitad_largo = largo / 2
        grosor_pata = 0.1 
        desplazamiento_patas = 0.2  

        glBegin(GL_QUADS)

        glVertex3f(x - mitad_ancho, alto, z - mitad_largo)
        glVertex3f(x + mitad_ancho, alto, z - mitad_largo)
        glVertex3f(x + mitad_ancho, alto, z + mitad_largo)
        glVertex3f(x - mitad_ancho, alto, z + mitad_largo)
        glEnd()

        glBegin(GL_QUADS)
        glVertex3f(x - mitad_ancho, alto - grosor_pata, z - mitad_largo)
        glVertex3f(x + mitad_ancho, alto - grosor_pata, z - mitad_largo)
        glVertex3f(x + mitad_ancho, alto - grosor_pata, z + mitad_largo)
        glVertex3f(x - mitad_ancho, alto - grosor_pata, z + mitad_largo)
        glEnd()

        glBegin(GL_QUADS)

        glVertex3f(x - mitad_ancho, alto, z - mitad_largo)
        glVertex3f(x - mitad_ancho, alto - grosor_pata, z - mitad_largo)
        glVertex3f(x - mitad_ancho, alto - grosor_pata, z + mitad_largo)
        glVertex3f(x - mitad_ancho, alto, z + mitad_largo)

        glVertex3f(x + mitad_ancho, alto, z - mitad_largo)
        glVertex3f(x + mitad_ancho, alto - grosor_pata, z - mitad_largo)
        glVertex3f(x + mitad_ancho, alto - grosor_pata, z + mitad_largo)
        glVertex3f(x + mitad_ancho, alto, z + mitad_largo)

        glVertex3f(x - mitad_ancho, alto, z + mitad_largo)
        glVertex3f(x + mitad_ancho, alto, z + mitad_largo)
        glVertex3f(x + mitad_ancho, alto - grosor_pata, z + mitad_largo)
        glVertex3f(x - mitad_ancho, alto - grosor_pata, z + mitad_largo)

        glVertex3f(x - mitad_ancho, alto, z - mitad_largo)
        glVertex3f(x + mitad_ancho, alto, z - mitad_largo)
        glVertex3f(x + mitad_ancho, alto - grosor_pata, z - mitad_largo)
        glVertex3f(x - mitad_ancho, alto - grosor_pata, z - mitad_largo)
        glEnd()

        glColor3f(0.6, 0.6, 0.6)

        glBegin(GL_QUADS)
        # Base
        glVertex3f(x - mitad_ancho + desplazamiento_patas, 0, z - mitad_largo + desplazamiento_patas)
        glVertex3f(x - mitad_ancho + desplazamiento_patas + grosor_pata, 0, z - mitad_largo + desplazamiento_patas)
        glVertex3f(x - mitad_ancho + desplazamiento_patas + grosor_pata, alto - grosor_pata, z - mitad_largo + desplazamiento_patas)
        glVertex3f(x - mitad_ancho + desplazamiento_patas, alto - grosor_pata, z - mitad_largo + desplazamiento_patas)

        # Cara lateral
        glVertex3f(x - mitad_ancho + desplazamiento_patas, 0, z - mitad_largo + desplazamiento_patas + grosor_pata)
        glVertex3f(x - mitad_ancho + desplazamiento_patas + grosor_pata, 0, z - mitad_largo + desplazamiento_patas + grosor_pata)
        glVertex3f(x - mitad_ancho + desplazamiento_patas + grosor_pata, alto - grosor_pata, z - mitad_largo + desplazamiento_patas + grosor_pata)
        glVertex3f(x - mitad_ancho + desplazamiento_patas, alto - grosor_pata, z - mitad_largo + desplazamiento_patas + grosor_pata)

        # Cara trasera
        glVertex3f(x - mitad_ancho + desplazamiento_patas, alto - grosor_pata, z - mitad_largo + desplazamiento_patas)
        glVertex3f(x - mitad_ancho + desplazamiento_patas, alto - grosor_pata, z - mitad_largo + desplazamiento_patas + grosor_pata)
        glVertex3f(x - mitad_ancho + desplazamiento_patas, 0, z - mitad_largo + desplazamiento_patas + grosor_pata)
        glVertex3f(x - mitad_ancho + desplazamiento_patas, 0, z - mitad_largo + desplazamiento_patas)

        # Cara frontal
        glVertex3f(x - mitad_ancho + desplazamiento_patas + grosor_pata, 0, z - mitad_largo + desplazamiento_patas)
        glVertex3f(x - mitad_ancho + desplazamiento_patas + grosor_pata, 0, z - mitad_largo + desplazamiento_patas + grosor_pata)
        glVertex3f(x - mitad_ancho + desplazamiento_patas + grosor_pata, alto - grosor_pata, z - mitad_largo + desplazamiento_patas + grosor_pata)
        glVertex3f(x - mitad_ancho + desplazamiento_patas + grosor_pata, alto - grosor_pata, z - mitad_largo + desplazamiento_patas)
        
        # Cara inferior
        glVertex3f(x - mitad_ancho + desplazamiento_patas, 0, z - mitad_largo + desplazamiento_patas)
        glVertex3f(x - mitad_ancho + desplazamiento_patas + grosor_pata, 0, z - mitad_largo + desplazamiento_patas)
        glVertex3f(x - mitad_ancho + desplazamiento_patas + grosor_pata, 0, z - mitad_largo + desplazamiento_patas + grosor_pata)
        glVertex3f(x - mitad_ancho + desplazamiento_patas, 0, z - mitad_largo + desplazamiento_patas + grosor_pata)
        glEnd()

        # Pata frontal derecha
        glBegin(GL_QUADS)
        # Base
        glVertex3f(x + mitad_ancho - desplazamiento_patas - grosor_pata, 0, z - mitad_largo + desplazamiento_patas)
        glVertex3f(x + mitad_ancho - desplazamiento_patas, 0, z - mitad_largo + desplazamiento_patas)
        glVertex3f(x + mitad_ancho - desplazamiento_patas, alto - grosor_pata, z - mitad_largo + desplazamiento_patas)
        glVertex3f(x + mitad_ancho - desplazamiento_patas - grosor_pata, alto - grosor_pata, z - mitad_largo + desplazamiento_patas)

        # Cara lateral
        glVertex3f(x + mitad_ancho - desplazamiento_patas - grosor_pata, 0, z - mitad_largo + desplazamiento_patas + grosor_pata)
        glVertex3f(x + mitad_ancho - desplazamiento_patas, 0, z - mitad_largo + desplazamiento_patas + grosor_pata)
        glVertex3f(x + mitad_ancho - desplazamiento_patas, alto - grosor_pata, z - mitad_largo + desplazamiento_patas + grosor_pata)
        glVertex3f(x + mitad_ancho - desplazamiento_patas - grosor_pata, alto - grosor_pata, z - mitad_largo + desplazamiento_patas + grosor_pata)

        # Cara trasera
        glVertex3f(x + mitad_ancho - desplazamiento_patas - grosor_pata, alto - grosor_pata, z - mitad_largo + desplazamiento_patas)
        glVertex3f(x + mitad_ancho - desplazamiento_patas - grosor_pata, alto - grosor_pata, z - mitad_largo + desplazamiento_patas + grosor_pata)
        glVertex3f(x + mitad_ancho - desplazamiento_patas - grosor_pata, 0, z - mitad_largo + desplazamiento_patas + grosor_pata)
        glVertex3f(x + mitad_ancho - desplazamiento_patas - grosor_pata, 0, z - mitad_largo + desplazamiento_patas)

        # Cara frontal
        glVertex3f(x + mitad_ancho - desplazamiento_patas, 0, z - mitad_largo + desplazamiento_patas)
        glVertex3f(x + mitad_ancho - desplazamiento_patas, 0, z - mitad_largo + desplazamiento_patas + grosor_pata)
        glVertex3f(x + mitad_ancho - desplazamiento_patas, alto - grosor_pata, z - mitad_largo + desplazamiento_patas + grosor_pata)
        glVertex3f(x + mitad_ancho - desplazamiento_patas, alto - grosor_pata, z - mitad_largo + desplazamiento_patas)
        
        # Cara inferior
        glVertex3f(x + mitad_ancho - desplazamiento_patas - grosor_pata, 0, z - mitad_largo + desplazamiento_patas)
        glVertex3f(x + mitad_ancho - desplazamiento_patas, 0, z - mitad_largo + desplazamiento_patas)
        glVertex3f(x + mitad_ancho - desplazamiento_patas, 0, z - mitad_largo + desplazamiento_patas + grosor_pata)
        glVertex3f(x + mitad_ancho - desplazamiento_patas - grosor_pata, 0, z - mitad_largo + desplazamiento_patas + grosor_pata)
        glEnd()

        glBegin(GL_QUADS)
        # Base
        glVertex3f(x - mitad_ancho + desplazamiento_patas, 0, z + mitad_largo - desplazamiento_patas)
        glVertex3f(x - mitad_ancho + desplazamiento_patas + grosor_pata, 0, z + mitad_largo - desplazamiento_patas)
        glVertex3f(x - mitad_ancho + desplazamiento_patas + grosor_pata, alto - grosor_pata, z + mitad_largo - desplazamiento_patas)
        glVertex3f(x - mitad_ancho + desplazamiento_patas, alto - grosor_pata, z + mitad_largo - desplazamiento_patas)

        # Cara lateral
        glVertex3f(x - mitad_ancho + desplazamiento_patas, 0, z + mitad_largo - desplazamiento_patas - grosor_pata)
        glVertex3f(x - mitad_ancho + desplazamiento_patas + grosor_pata, 0, z + mitad_largo - desplazamiento_patas - grosor_pata)
        glVertex3f(x - mitad_ancho + desplazamiento_patas + grosor_pata, alto - grosor_pata, z + mitad_largo - desplazamiento_patas - grosor_pata)
        glVertex3f(x - mitad_ancho + desplazamiento_patas, alto - grosor_pata, z + mitad_largo - desplazamiento_patas - grosor_pata)

        # Cara trasera
        glVertex3f(x - mitad_ancho + desplazamiento_patas, alto - grosor_pata, z + mitad_largo - desplazamiento_patas)
        glVertex3f(x - mitad_ancho + desplazamiento_patas, alto - grosor_pata, z + mitad_largo - desplazamiento_patas - grosor_pata)
        glVertex3f(x - mitad_ancho + desplazamiento_patas, 0, z + mitad_largo - desplazamiento_patas - grosor_pata)
        glVertex3f(x - mitad_ancho + desplazamiento_patas, 0, z + mitad_largo - desplazamiento_patas)

        # Cara frontal
        glVertex3f(x - mitad_ancho + desplazamiento_patas + grosor_pata, 0, z + mitad_largo - desplazamiento_patas)
        glVertex3f(x - mitad_ancho + desplazamiento_patas + grosor_pata, 0, z + mitad_largo - desplazamiento_patas - grosor_pata)
        glVertex3f(x - mitad_ancho + desplazamiento_patas + grosor_pata, alto - grosor_pata, z + mitad_largo - desplazamiento_patas - grosor_pata)
        glVertex3f(x - mitad_ancho + desplazamiento_patas + grosor_pata, alto - grosor_pata, z + mitad_largo - desplazamiento_patas)

        # Cara inferior
        glVertex3f(x - mitad_ancho + desplazamiento_patas, 0, z + mitad_largo - desplazamiento_patas)
        glVertex3f(x - mitad_ancho + desplazamiento_patas + grosor_pata, 0, z + mitad_largo - desplazamiento_patas)
        glVertex3f(x - mitad_ancho + desplazamiento_patas + grosor_pata, 0, z + mitad_largo - desplazamiento_patas - grosor_pata)
        glVertex3f(x - mitad_ancho + desplazamiento_patas, 0, z + mitad_largo - desplazamiento_patas - grosor_pata)
        glEnd()

        glBegin(GL_QUADS)
        # Base
        glVertex3f(x + mitad_ancho - desplazamiento_patas - grosor_pata, 0, z + mitad_largo - desplazamiento_patas)
        glVertex3f(x + mitad_ancho - desplazamiento_patas, 0, z + mitad_largo - desplazamiento_patas)
        glVertex3f(x + mitad_ancho - desplazamiento_patas, alto - grosor_pata, z + mitad_largo - desplazamiento_patas)
        glVertex3f(x + mitad_ancho - desplazamiento_patas - grosor_pata, alto - grosor_pata, z + mitad_largo - desplazamiento_patas)

        # Cara lateral
        glVertex3f(x + mitad_ancho - desplazamiento_patas - grosor_pata, 0, z + mitad_largo - desplazamiento_patas - grosor_pata)
        glVertex3f(x + mitad_ancho - desplazamiento_patas, 0, z + mitad_largo - desplazamiento_patas - grosor_pata)
        glVertex3f(x + mitad_ancho - desplazamiento_patas, alto - grosor_pata, z + mitad_largo - desplazamiento_patas - grosor_pata)
        glVertex3f(x + mitad_ancho - desplazamiento_patas - grosor_pata, alto - grosor_pata, z + mitad_largo - desplazamiento_patas - grosor_pata)

        # Cara trasera
        glVertex3f(x + mitad_ancho - desplazamiento_patas - grosor_pata, alto - grosor_pata, z + mitad_largo - desplazamiento_patas)
        glVertex3f(x + mitad_ancho - desplazamiento_patas - grosor_pata, alto - grosor_pata, z + mitad_largo - desplazamiento_patas - grosor_pata)
        glVertex3f(x + mitad_ancho - desplazamiento_patas - grosor_pata, 0, z + mitad_largo - desplazamiento_patas - grosor_pata)
        glVertex3f(x + mitad_ancho - desplazamiento_patas - grosor_pata, 0, z + mitad_largo - desplazamiento_patas)

        # Cara frontal
        glVertex3f(x + mitad_ancho - desplazamiento_patas, 0, z + mitad_largo - desplazamiento_patas)
        glVertex3f(x + mitad_ancho - desplazamiento_patas, 0, z + mitad_largo - desplazamiento_patas - grosor_pata)
        glVertex3f(x + mitad_ancho - desplazamiento_patas, alto - grosor_pata, z + mitad_largo - desplazamiento_patas - grosor_pata)
        glVertex3f(x + mitad_ancho - desplazamiento_patas, alto - grosor_pata, z + mitad_largo - desplazamiento_patas)

        # Cara inferior
        glVertex3f(x + mitad_ancho - desplazamiento_patas - grosor_pata, 0, z + mitad_largo - desplazamiento_patas)
        glVertex3f(x + mitad_ancho - desplazamiento_patas, 0, z + mitad_largo - desplazamiento_patas)
        glVertex3f(x + mitad_ancho - desplazamiento_patas, 0, z + mitad_largo - desplazamiento_patas - grosor_pata)
        glVertex3f(x + mitad_ancho - desplazamiento_patas - grosor_pata, 0, z + mitad_largo - desplazamiento_patas - grosor_pata)
        glEnd()

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MesaApp()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec_())
