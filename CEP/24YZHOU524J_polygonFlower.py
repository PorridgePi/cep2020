#ex3C_polygonFlower.py

# Full Name: Zhou Yikun
# Form Class: 2H

from turtle import *

def polygon(sides,length=100):
    for i in range(sides):
        forward(length)
        left(360/sides)

def polygonFlower(numPetals,petalSides,petalLen):
    turn=360/numPetals
    for i in range(numPetals):
        polygon(petalSides,petalLen)
        left(turn)
        
