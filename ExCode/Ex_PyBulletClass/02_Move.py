import pybullet as p
import time
import random
import numpy as np


class World :
    def __init__(self):
        self.sphereRadius = 0.1
        self.colSphereId = p.createCollisionShape(p.GEOM_SPHERE, radius=self.sphereRadius)
        self.mass = 1.0
        self.visualShapeId = p.createVisualShape(shapeType=p.GEOM_SPHERE, radius=self.sphereRadius, rgbaColor=[1, 1, 0, 0.75])

        wallId = p.createCollisionShape(p.GEOM_BOX, halfExtents=[5.0, 0.1, 0.5])
        p.createMultiBody(0, wallId, -1, [ 0, 5, 0.25], p.getQuaternionFromEuler([0.0, 0.0, 0.0]))
        p.createMultiBody(0, wallId, -1, [ 0,-5, 0.25], p.getQuaternionFromEuler([0.0, 0.0, 0.0]))
        p.createMultiBody(0, wallId, -1, [ 5, 0, 0.25], p.getQuaternionFromEuler([0.0, 0.0, 3.14/2.0]))
        p.createMultiBody(0, wallId, -1, [-5, 0, 0.25], p.getQuaternionFromEuler([0.0, 0.0, 3.14/2.0]))

        self.paddleColId = p.createCollisionShape(p.GEOM_BOX, halfExtents=[0.5, 0.1, 0.1])
        self.paddle = p.createMultiBody(10.0, self.paddleColId, -1, [ 0, 0, 0.05], p.getQuaternionFromEuler([0.0, 0.0, 0.0]))

    def force(self, dir=1.0):
        paddlePos, boxOrn = p.getBasePositionAndOrientation(self.paddle)
        p.applyExternalForce(objectUniqueId=self.paddle, linkIndex=-1, forceObj=dir*np.array([100,0,0]), posObj=paddlePos, flags=p.WORLD_FRAME)
        p.stepSimulation()

    def initPos(self):

        for _ in range(10) :
            basePosition = [random.random(), random.random(), random.random() + 1]
            p.createMultiBody(self.mass, self.colSphereId, self.visualShapeId, basePosition, p.getQuaternionFromEuler([0.0, 0.0, 0.0]))


def main():
    p.connect(p.GUI)
    planeId = p.createCollisionShape(p.GEOM_PLANE)
    p.createMultiBody(0.0, planeId)

    world = World()
    world.initPos()

    p.setGravity(0, 0, -10)
    #p.setRealTimeSimulation(1)

    while (1):
        keys = p.getKeyboardEvents()
        if(keys=={32:3}) : world.initPos()
        if (keys == {102: 1}): world.force(1)
        if (keys == {100: 1}): world.force(-1)
        p.stepSimulation()
        print(keys)
        time.sleep(0.01)

if __name__ == '__main__':
    main()