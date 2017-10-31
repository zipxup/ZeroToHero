import turtle
import math

#draw a squre
#for step in range(4):
#    turtle.forward(100)
#    turtle.right(90)
#    for morestep in range(4):
#        turtle.forward(50)
#        turtle.right(90)

#draw a triangle
#turtle.color('purple')
#for degree in range(3):
#    turtle.forward(100)
#    turtle.right(120)

#draw a circle
#for steps in range(360):
#    turtle.forward(1)
#    turtle.right(1)

nbrSides = 20
for steps in range(nbrSides):
    turtle.forward(10)
    turtle.right(360/nbrSides)
    for morestemps in range(nbrSides):
        turtle.forward(5)
        turtle.right(360/nbrSides)