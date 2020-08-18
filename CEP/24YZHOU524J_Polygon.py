#ex3A_polygon.py

# Full Name: Zhou Yikun
# Form Class: 2H

from turtle import *

def polygon(sides,length=100):
    for i in range(sides):
        forward(length)
        left(360/sides)

'''
    Example: Using for loop to create a square (4-sided polygon) of length 100
'''
polygon(4)


'''
   Exercise: Use for loop to create a regular triangle (3-sided polygon) of length 100
'''
polygon(3)


'''
   Exercise: Use for loop to create a regular pentagon (5-sided polygon) of length 100
'''
polygon(5)

'''
   Exercise: Use for loop to create a regular hexagon (6-sided polygon) of length 100
'''
polygon(6)

'''
   Exercise: Use for loop to create a regular heptagon (7-sided polygon) of length 100
'''
polygon(7)



'''
   Exercise: Use for loop to create a regular octagon (8-sided polygon) of length 100
'''
polygon(8)


'''
    Challenge: 
       Use for loop to create a circle (?-sided polygon) 
'''

polygon(1000,1)



