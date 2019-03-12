from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import time

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
    if TimerOn() is not True :
        TimerStart()


    print(TimerGetDt())
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glutWireSphere(0.5, 30, 30)
    glFlush()
    time.sleep(0.5)



GLinit()
RegisterCallbacks()
glutMainLoop()

# End of program