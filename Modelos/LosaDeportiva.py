from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

camera_angle_x = 0
camera_angle_y = 0
camera_distance = 40
mouse_x, mouse_y = 0, 0
mouse_left_down = False

def init():
    glClearColor(0.5, 0.7, 0.9, 1.0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

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

def draw_scene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -camera_distance)
    glRotatef(camera_angle_x, 1.0, 0.0, 0.0)
    glRotatef(camera_angle_y, 0.0, 1.0, 0.0)

    draw_floor()
    draw_walls()

    glPushMatrix()
    glTranslatef(-4, 0, -10) 
    draw_rectangle() 
    glPopMatrix()

    glPushMatrix()
    glTranslatef(10, 0, -10) 
    draw_rectangle_green() 
    glPopMatrix()

    draw_rectangle_outline()
    draw_rectangle_outline2()
    draw_lines()

    glPushMatrix()
    glTranslatef(-16, 0.0, 0.0)  # Canasta izquierda
    draw_Soporte()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(16, 0.0, 0.0)  # Canasta derecha
    draw_Soporte()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-15.6, 0.0, 0.0)  # Canasta derecha
    draw_aro()
    draw_backboard(-1)  # Cuadrado blanco detrás
    glPopMatrix()

    glPushMatrix()
    glTranslatef(15.6, 0.0, 0.0)  # Canasta derecha
    draw_aro()
    draw_backboard(1)  # Cuadrado blanco detrás
    glPopMatrix()

    draw_yellow_squares()
    draw_stairs()

    glPushMatrix()
    glTranslatef(10.5, 0.0, 0.0) 
    glRotatef(90, 1.0, 0.0, 0.0)  
    glRotatef(180, 0.0, 0.0, 1.0)
    draw_half_circle(1.5, 100)  
    glPopMatrix()

    glPushMatrix()
    glTranslatef(14.5, 0.1, 0.0) 
    glRotatef(90, 1.0, 0.0, 0.0)  
    glRotatef(180, 0.0, 0.0, 1.0)
    draw_half_circle(0.7, 100) 
    glPopMatrix()

    glPushMatrix()
    glTranslatef(14.5, 0.0, 0.0)  
    glRotatef(90, 1.0, 0.0, 0.0)  
    glRotatef(180, 0.0, 0.0, 1.0)
    draw_half_circle(6, 100) 
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(-10.5, 0.0, 0.0)  
    glRotatef(90, 1.0, 0.0, 0.0)  
    glRotatef(0, 0.0, 0.0, 1.0)
    draw_half_circle(1.5, 100)  
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-14.5, 0.1, 0.0)  
    glRotatef(90, 1.0, 0.0, 0.0)  
    glRotatef(0, 0.0, 0.0, 1.0)
    draw_half_circle(0.7, 100)  
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-14.5, 0.0, 0.0) 
    glRotatef(90, 1.0, 0.0, 0.0)  
    glRotatef(0, 0.0, 0.0, 1.0)
    draw_half_circle(6, 100)  
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0, 0.0, 0.0)  
    glRotatef(90, 1.0, 0.0, 0.0)
    glColor3f(1.0, 1.0, 1.0)  
    draw_circle(2.0, 100)  
    glPopMatrix()
    glutSwapBuffers() 

def mouse_motion(x, y):
    global camera_angle_x, camera_angle_y, mouse_x, mouse_y
    if mouse_left_down:
        delta_x = x - mouse_x
        delta_y = y - mouse_y
        camera_angle_x += delta_y * 0.2
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
    gluPerspective(45, width / height, 1, 200)
    glMatrixMode(GL_MODELVIEW)

def keyboard(key, x, y):
    global camera_distance, camera_angle_x, camera_angle_y
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

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow("Cancha de Baloncesto")
    init()
    glutDisplayFunc(draw_scene)
    glutReshapeFunc(reshape)
    glutMouseFunc(mouse_button)
    glutMotionFunc(mouse_motion)
    glutKeyboardFunc(keyboard)  # Capturar entradas del teclado
    glutMainLoop()

if __name__ == "__main__":
    main()
