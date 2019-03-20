from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import time
import numpy as np

import TUGame


class myGame(TUGame.Game) :

    def frame(self):
        dt = self.getDt()
        et = self.getEt()

        super().frame()
        # your code here
        self.drawBall([0,0,0])
        super().afterFrame()

game = myGame(500,500, b"Hello My World")
game.grid(True)

def key(k, x,y) :
    game.timerStart()
def draw() :
    game.frame()

game.start(draw, key)