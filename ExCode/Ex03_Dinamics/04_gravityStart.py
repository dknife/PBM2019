from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

import random
import numpy as np

from TUGameEngine import TUGame


class myGame(TUGame.Game):
    def __init__(self, w, h, title):
        super().__init__(w, h, title)

        self.loc = []
        self.vel = []
        self.mass = []
        self.force = []
        self.loc.append(np.array([-15., 5., 0.]))
        self.loc.append(np.array([15., -5., 0.]))
        self.vel.append(np.array([5., 0., 0.]))
        self.vel.append(np.array([-5., 0., 0.]))
        self.mass.append(1.0)
        self.mass.append(20.0)
        self.force.append(np.array([0., 0., 0.]))
        self.force.append(np.array([0., 0., 0.]))

        self.cameraAt([0, 0, 50], [0, 0, 0])

        #self.setBackground(b"background.jpg")

    def initObjects(self):
        self.loc[0] = np.array([-15., 5., 0.])
        self.loc[1] = np.array([15., -5., 0.])
        self.vel[0] = np.array([5., 0., 0.])
        self.vel[1] = np.array([-5., 0., 0.])

    def frame(self):

        dt = self.getDt()

        super().frame()
        # your code here

        # compute force
        for i in range(0, 2):
            self.force[i] = np.array([0., 0., 0.])

        G = 150.0
        dir = self.loc[1] - self.loc[0]
        d = np.linalg.norm(dir)
        dir = dir / d;
        mag = G * self.mass[0] * self.mass[1] / (d * d)
        self.force[0] = mag * dir;
        self.force[1] = -self.force[0]

        # simulate with the force
        for i in range(0, 2):
            self.vel[i] += self.force[i] * dt / self.mass[i]
            self.loc[i] += self.vel[i] * dt

        for balls in self.loc:
            self.drawBall(balls)

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