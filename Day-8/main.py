import turtle


def drawSquare(sideLength):
    for i in range(4):
        turtle.forward(sideLength)
        turtle.left(90)


counter = 0
while counter < 90:
    drawSquare(150)
    turtle.right(4)
    counter += 1

turtle.exitonclick()
