from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

ball1 = [0,0,0]
ball2 = [0,0,5]

def GLinit() :
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(250, 250)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"OpenGL with Python")

def RegisterCallbacks() :
    glutDisplayFunc(draw)
    glutIdleFunc(draw)

def drawLine(x,y,z, xx,yy,zz) :
    glBegin(GL_LINES)
    glVertex3f(x,y,z)
    glVertex3f(xx,yy,zz)
    glEnd()

def drawBall(pos) :
    glPushMatrix()
    glTranslatef(pos[0], pos[1], pos[2])
    glutWireSphere(1.0, 10,10)
    glPopMatrix()


def draw():
    global ball1, ball2

    glClear(GL_COLOR_BUFFER_BIT)

    # Lens
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1.0, 0.1, 1000.0)

    # World
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(20,20,20, 0,0,0, 0,1,0)

    glColor3f(1,0,0)
    drawLine(0, 0, 0, 10, 0, 0)
    glColor3f(0, 1, 0)
    drawLine(0, 0, 0,  0,10, 0)
    glColor3f(0, 0, 1)
    drawLine(0, 0, 0,  0, 0,10)

    glColor3f(1,1,1)

    drawBall(ball1)
    drawBall(ball2)
    glFlush()


GLinit()
RegisterCallbacks()
glutMainLoop()

# End of program
