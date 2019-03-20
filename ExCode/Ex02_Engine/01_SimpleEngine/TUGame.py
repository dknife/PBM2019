import time

from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *


class Graphics:
    def drawGrid(self, numberOfLines):
        glColor3f(0.5, 0.5, 0.5)
        for x in range(0, numberOfLines):
            glBegin(GL_LINES)
            glVertex3f(x-numberOfLines/2.0, 0, -numberOfLines/2.0)
            glVertex3f(x-numberOfLines/2.0, 0, numberOfLines/2.0)
            glEnd()

        for z in range(0, numberOfLines):
            glBegin(GL_LINES)
            glVertex3f(-numberOfLines/2.0, 0, z-numberOfLines/2.0)
            glVertex3f(numberOfLines/2.0, 0, z-numberOfLines/2.0)
            glEnd()

    def drawBall(self, pos):
        glPushMatrix()
        glTranslatef(pos[0], pos[1], pos[2])
        glutWireSphere(1.0, 10, 10)
        glPopMatrix()


class Timer:

    def __init__(self):
        self.dt = -1.0
        self.et = 0.0
        self.currentTime = 0.0
        self.lastTime = 0.0
        self.timerRunning = False

    def isTimerOn(self):
        if self.dt > 0:
            return True
            return False

    def start(self):
        if self.timerRunning is not True:
            self.currentTime = time.clock()
            self.lastTime = self.currentTime

        self.timerRunning = True

    def stop(self):
        self.timerRunning = False


    def getDt(self):
        if self.timerRunning is not True :
            return 0.0

        self.currentTime = time.clock()
        self.dt = self.currentTime - self.lastTime
        self.lastTime = self.currentTime
        self.et += self.dt
        return self.dt

    def getEt(self):
        self.getDt()
        return self.et

class Camera:


    def __init__(self, fov=60.0, asp=1.0, near=0.1, far=1000.0):
        self.fov = fov
        self.asp = asp
        self.near = near
        self.far = far
        self.eye = [1, 1, 1]
        self.target = [0, 0, 0]
        self.up = [0, 1, 0]



    def applyCamera(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(self.fov, self.asp, self.near, self.far)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(self.eye[0],self.eye[1],self.eye[2], self.target[0], self.target[1], self.target[2], self.up[0], self.up[1], self.up[2])

    def setLens(self, fov, asp, near, far):
        self.fov = fov
        self.asp = asp
        self.near = near
        self.far = far

    def setPos(self, x, y, z, tx, ty, tz, ux=0.0, uy=1.0, uz=0.0):
        self.eye = [x,y,z]
        self.target = [tx,ty,tz]
        self.up = [ux,uy,uz]

    def setAsp(self, w, h):
        self.asp = w/h

class Game:
    def __init__(self, w, h, title):
        self.cam = Camera(60., 1.0, 0.1, 1000.0)
        self.cam.setPos(10,10,10, 0,0,0)
        self.timer = Timer()
        self.gridMode = False
        self.graphics = Graphics()

        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(w, h)
        glutInitWindowPosition(100, 100)
        glutCreateWindow(title)
        glClearColor(0.25, 0.25, 0.25, 1.0)

    def reshape(self, w, h):
        self.cam.setAsp(w,h)
        glViewport(0,0, w,h)

    def grid(self, option):
        self.gridMode = option

    def timerStart(self):
        self.timer.start()

    def timerStop(self):
        self.timer.stop()

    def getDt(self):
        return self.timer.getDt()

    def getEt(self):
        return self.timer.getEt()

    def frame(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.cam.applyCamera()

        if self.gridMode :
            self.graphics.drawGrid(100)


    def afterFrame(self):
        glFlush()

    def start(self, displayCallback, keyCallback):
        glutDisplayFunc(displayCallback)
        glutIdleFunc(displayCallback)
        glutKeyboardFunc(keyCallback)
        glutReshapeFunc(self.reshape)
        glutMainLoop()

    def drawBall(self, pos):
        self.graphics.drawBall(pos)