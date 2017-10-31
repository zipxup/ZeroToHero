import turtle

nbrSides = input("how many sides the object will have? ")
nbrSides = int(nbrSides)

lenghOfLine = 100
for step in range(nbrSides):
    turtle.forward(lenghOfLine)
    turtle.right(360/nbrSides)
    for morestep in range(nbrSides):
        turtle.forward(lenghOfLine/2)
        turtle.right(360/nbrSides)