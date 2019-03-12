from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import time
import numpy as np


dt = -1
currentTime = 0
lastTime=0

def TimerOn() :
    if dt>0 :
        return True
    else :
        return False

def TimerStart():
    global currentTime, lastTime, dt
    if dt<0 :
        currentTime = time.perf_counter()
        lastTime = currentTime

def TimerGetDt():
    global currentTime, lastTime, dt
    currentTime = time.perf_counter()
    dt = currentTime - lastTime
    lastTime = currentTime
    return dt

ball1 = np.array([0,0,0])
ball2 = np.array([0,0,5])

ball1V = np.array([1,0,0])
ball2V = np.array([0.5, 0,0])

simulationStart = False

def GLinit() :
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(250, 250)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"OpenGL with Python")

def RegisterCallbacks() :
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutKeyboardFunc(key)

def key(k, x,y) :
    global simulationStart
    simulationStart = True

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

    if TimerOn() != True :
        TimerStart()

    dt = TimerGetDt()

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

    if simulationStart :
        ball1 = ball1 + ball1V * dt
        ball2 = ball2 + ball2V * dt

    drawBall(ball1)
    drawBall(ball2)
    glFlush()


GLinit()
RegisterCallbacks()
glutMainLoop()

# End of program