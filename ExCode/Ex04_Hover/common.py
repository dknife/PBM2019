import math
import numpy as np


def local2global(angle, vec) :
    c = math.cos(angle)
    s = math.sin(angle)
    x = c*vec[0] -s*vec[1]
    y = s*vec[0] +c*vec[1]
    return np.array([x,y,0.0])

def rad2deg(rad) :
    return 180.0*(rad/3.141592)

def deg2rad(deg) :
    return 3.141592*(deg/180.0)