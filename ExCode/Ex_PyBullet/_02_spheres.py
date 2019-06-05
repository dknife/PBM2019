import pybullet as p
import time
import random

def _initPos() :
    for i in range(10):
        basePosition = [random.random(), random.random(), random.random() + 1]
        baseOrientation = p.getQuaternionFromEuler([random.random(), random.random(), random.random()])
        sphereUid = p.createMultiBody(mass, colSphereId, visualShapeId, basePosition, baseOrientation)


p.connect(p.GUI)
p.createCollisionShape(p.GEOM_PLANE)
p.createMultiBody(0, 0)

sphereRadius = 0.05
colSphereId = p.createCollisionShape(p.GEOM_SPHERE, radius=sphereRadius)

mass = 1
visualShapeId = -1

_initPos()

p.setGravity(0, 0, -10)
p.setRealTimeSimulation(1)

while (1):
  keys = p.getKeyboardEvents()
  if(keys=={32:1}) :
      _initPos()
  time.sleep(0.01)