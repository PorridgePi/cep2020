#ex3B_spiral.py

# Full Name: Zhou Yikun
# Form Class: 2H

from turtle import *

def spiral(sideLen,angle,scaleFactor,numSides):
    for i in range(numSides):
        forward(sideLen)
        left(angle)
        sideLen*=scaleFactor

spiral(300, 93, 0.95, 100)
