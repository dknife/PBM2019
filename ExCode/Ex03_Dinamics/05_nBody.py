from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

import random
import numpy as np

from TUGameEngine import TUGame

nParticle = 30

def myRand(start, end) :
    interval = end - start
    return start + interval * random.random()

class myGame(TUGame.Game):

    def __init__(self, w, h, title):
        super().__init__(w, h, title)

        self.loc = []
        self.vel = []
        self.mass = []
        self.force = []

        for i in range(0, nParticle) :
            self.loc.append(np.array([0.,0.,0.]))
            self.vel.append(np.array([0., 0., 0.]))
            self.force.append(np.array([0., 0., 0.]))
            self.mass.append(1.0)

        self.initObjects()

        self.cameraAt([0,20,70], [0,0,0])


        #self.setBackground(b"cosmos.jpg")

    def initObjects(self):

        self.loc[0] = np.array([0.,0.,0.])
        self.vel[0] = np.array([0.,0.,0.])
        self.mass[0] = 1000.0

        for i in range(1, nParticle) :
            self.loc[i] = np.array([
                myRand(-40.0, 40.0), myRand(-1., 1.), myRand(-40.,40)])
            self.vel[i] = np.array([
                self.loc[i][2], 0, -self.loc[i][0]])
                #myRand(-40.0, 40.0), myRand(-1., 1.), myRand(-40.,40)])


    def frame(self):

        dt = self.getDt()

        super().frame()
        # your code here
        dt = 0.01
        G  = 50.0
        # compute force
        for i in range(0, nParticle) :
            self.force[i] = np.array([0., 0., 0.])

        for i in range(0, nParticle) :
            for j in range(i+1, nParticle) :
                dir = self.loc[j] - self.loc[i]
                d = np.linalg.norm(dir)
                if d < 1.0 :
                    d = 1.0
                force_ij = G * self.mass[i]*self.mass[j] * dir / (d**3.)
                self.force[i] += force_ij
                self.force[j] -= force_ij

        # integration
        for i in range(0, nParticle) :
            self.vel[i] += self.force[i]*dt/self.mass[i]
            self.loc[i] += self.vel[i]*dt

        glColor3f(1,1,0)
        for i in range(0,nParticle) :
            self.drawBall(self.loc[i], 0.5*self.mass[i]**(1./6.))

        super().afterFrame()


game = myGame(500, 500, b"gravity")
game.grid(True)


def key(k, x, y):
    if k is b' ':
        if game.timer.timerRunning:
            game.timerStop()
        else:
            game.timerStart()
    elif k is b'r':
        game.timerReset()
        game.initObjects()


def draw():
    game.frame()


game.start(draw, key)