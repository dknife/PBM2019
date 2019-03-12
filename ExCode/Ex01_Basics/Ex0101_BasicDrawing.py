from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

def GLinit() :
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(250, 250)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"OpenGL with Python")

def RegisterCallbacks() :
    glutDisplayFunc(draw)
    glutIdleFunc(draw)

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glutWireSphere(0.5, 30, 30)
    glFlush()


GLinit()
RegisterCallbacks()
glutMainLoop()
