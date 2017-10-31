import turtle

color = "green"
lineOfLength = 0
angle = 0

lineOfLength = float(input("please input a line length: (0 to stop drawing)"))

while lineOfLength != 0:
    color = input("please input your pen color: ").lower()
    angle = int(input("please input a rotation angle: "))

    turtle.color(color)
    turtle.forward(lineOfLength)
    turtle.right(angle)

    lineOfLength = float(input("please input a line length: "))

print("line length is 0. Everything is finished")

