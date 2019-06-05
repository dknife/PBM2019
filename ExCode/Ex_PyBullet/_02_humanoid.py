import pybullet as p
import pybullet_data
import time
import math
import numpy as np
import random

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally

p.loadURDF("plane.urdf")


nCube = 10
cubeId = []
for i in range(nCube) :
    cubeStartPos = [random.random(), random.random(), random.random()+1]
    cubeStartOrientation = p.getQuaternionFromEuler([random.random(), random.random(), random.random()])
    cubeId.append(p.loadURDF("r2d2.urdf", cubeStartPos, cubeStartOrientation))

p.setGravity(0, 0, -10)

useRealTimeSimulation = 1

if (useRealTimeSimulation):
  p.setRealTimeSimulation(1)

while 1:
  if (useRealTimeSimulation):
    p.setGravity(0, 0, -10)
    time.sleep(0.01)  # Time in seconds.
  else:
    p.stepSimulation()