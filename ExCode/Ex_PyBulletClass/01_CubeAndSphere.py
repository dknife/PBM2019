import pybullet as p
import time
import random

class World :
    def __init__(self):
        self.sphereRadius = 0.1
        self.colSphereId = p.createCollisionShape(p.GEOM_SPHERE, radius=self.sphereRadius)
        self.colBoxId = p.createCollisionShape(p.GEOM_BOX, halfExtents=[self.sphereRadius,self.sphereRadius,self.sphereRadius])
        self.mass = 1.0
        self.visualShapeId = p.createVisualShape(shapeType=p.GEOM_SPHERE, radius=self.sphereRadius, rgbaColor=[1, 1, 0, 0.75])

    def initPos(self):

        for _ in range(10) :
            basePosition = [random.random(), random.random(), random.random() + 1]
            p.createMultiBody(self.mass, self.colSphereId, self.visualShapeId, basePosition, p.getQuaternionFromEuler([0.0, 0.0, 0.0]))
            basePosition = [random.random(), random.random(), random.random() + 1]
            baseOrientation = p.getQuaternionFromEuler([random.random(), random.random(), random.random()])
            p.createMultiBody(self.mass, self.colBoxId, -1, basePosition, baseOrientation)

def main():
    p.connect(p.GUI)
    planeId = p.createCollisionShape(p.GEOM_PLANE)
    p.createMultiBody(0.0, planeId)

    world = World()
    world.initPos()

    p.setGravity(0, 0, -10)
    p.setRealTimeSimulation(1)

    while (1):
        keys = p.getKeyboardEvents()
        if(keys=={32:3}) : world.initPos()
        time.sleep(0.01)

if __name__ == '__main__':
    main()