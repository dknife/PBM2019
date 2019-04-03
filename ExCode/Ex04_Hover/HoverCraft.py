from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

import random
import math
import numpy as np

import common

class HoverCraft :

    def __init__(self):
        # constants
        self.Cd  = 2.0
        self.Cdr = 2.0

        # 선 운동
        self.loc = np.array([2.5,0.5,0.])
        self.vel = np.array([0.,0.,0.])
        self.acc = np.array([0.,0.,0.])
        self.mass = 10.0;

        # 회전 운동
        self.angle = 3.14/4.0 # radian
        self.aVel = 0.
        self.aAcc = 0.
        self.I = 2.0*self.mass/3.


        self.engines = [False,False,False,False]
        self.engineLoc = np.array([[-1.,1.,0.],[1.,1.,0.],[-1.,-1.,0.],[1.,-1.,0.]])
        self.engineForce = np.array([[1.,0.,0.],[-1.,0.,0.],[0.,3.,0.],[0.,3.,0.]])
        print(self.engineLoc[0])

        return

    def show(self):
        glColor3f(1,0,0)
        glPushMatrix()
        glTranslatef(self.loc[0], self.loc[1], self.loc[2])
        glRotatef(common.rad2deg(self.angle), 0.,0.,1.)

        # 본체
        glBegin(GL_POLYGON)
        glVertex2f( 0, 1.5)
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

        # 힘 계산
        self.acc = np.array([0.,0.,0.])
        for engine in range(4) :
            if self.engines[engine] is True :
                force = common.local2global(self.angle, self.engineForce[engine])
                self.acc += force/self.mass
        # 항력: fd = -Cd*v
        self.acc += - self.Cd * self.vel / self.mass;

        # 선운동 수치 적분
        self.vel += self.acc * dt
        self.loc += self.vel * dt

        # 토크 계산
        self.aAcc = 0.
        for engine in range(4) :
            if self.engines[engine] is True :
                torque = np.cross(self.engineLoc[engine],
                                  self.engineForce[engine])
                self.aAcc += torque[2]/self.I
        # 회전 항력 : td = -Cdr * w
        self.aAcc += - self.Cdr * self.aVel / self.I;

        # 회전운동 수치적분
        self.aVel += self.aAcc * dt
        self.angle += self.aVel * dt

    def engineSwitch(self, swNo):
        idx = swNo - 1
        if idx < 0 or idx > 3 :
            return
        if self.engines[idx] is True :
            self.engines[idx] = False
        else :
            self.engines[idx] = True

    def getLoc(self):
        return self.loc