from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

import random
import numpy as np

from TUGameEngine import TUGame

class rigidObj :

    def __init__(self):
        self.loc = np.array([0.5,0.5,0.])
        self.vel = np.array([0.,0.,0.])
        self.engines = [False,False,False,False]
        self.engineLoc = np.array([[-1.,1.,0.],[1.,1.,0.],[-1.,-1.,0.],[1.,-1.,0.]])
        self.engineForce = np.array([[1.,0.,0.],[-1.,0.,0.],[0.,3.,0.],[0.,3.,0.]])
        print(self.engineLoc[0])

        return

    def show(self):
        glColor3f(1,0,0)
        glPushMatrix()
        glTranslatef(self.loc[0], self.loc[1], self.loc[2])

        # 본체
        glBegin(GL_QUADS)
        glVertex2f(-1, 1)
        glVertex2f(-1,-1)
        glVertex2f( 1,-1)
        glVertex2f( 1, 1)
        glEnd()
        # 엔진
        for i in range(4) :
            if self.engines[i] is True :
                glLineWidth(5)
                glColor3f(1,1,0)
                glPushMatrix()
                L = self.engineLoc[i]
                F = self.engineForce[i]
                glTranslatef(L[0], L[1], L[2])
                glBegin(GL_LINES)
                glVertex3f(0,0,0)
                glVertex3f(-F[0], -F[1], -F[2])
                glEnd()
                glPopMatrix()
                glLineWidth(1)

        glPopMatrix()

    def simulate(self, dt):
        self.loc += self.vel * dt

    def engineSwitch(self, swNo):
        idx = swNo - 1
        if idx < 0 or idx > 3 :
            return
        if self.engines[idx] is True :
            self.engines[idx] = False
        else :
            self.engines[idx] = True

class myGame(TUGame.Game) :


    def __init__(self, w, h, title):
        super().__init__(w,h,title)

        self.myObj = rigidObj()

        self.initObjects()

        self.cameraAt([0.,0.,10.], [0.,0.,0.], [0.,1.,0.])
        self.cam.setLens(60, 1, 0.1, 2000.)


        #self.setBackground("bg_cosmos.jpg")


    def initObjects(self):

        return


    def frame(self):
        dt = self.getDt()

        super().frame()

        self.myObj.simulate(dt)
        self.myObj.show()

        super().afterFrame()


game = myGame(500,500, b"2D Rigid")
game.grid(True)
game.rotateGrid(90, [1,0,0])

def key(k, x,y) :

    if k is b' ' :
        if game.timer.timerRunning :
            game.timerStop()
        else :
            game.timerStart()
    elif k is b'r':
        game.timerReset()
        game.initObjects()

    elif k is b'1':
        game.myObj.engineSwitch(1)
    elif k is b'2':
        game.myObj.engineSwitch(2)
    elif k is b'3':
        game.myObj.engineSwitch(3)
    elif k is b'4':
        game.myObj.engineSwitch(4)


def draw() :
    game.frame()

game.start(draw, key)