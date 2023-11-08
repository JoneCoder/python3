# Random Number

# import random
#
#
# def add(a, b):
#     return a + b
#
#
# # gaussNumber = random.random()
# gaussNumberInt = random.randint(1, 6)
# sumTwoNumber = add(1, 6)
#
# print(gaussNumberInt)

import turtle
import random

turtle.penup()
color = ["red", "green", "blue", "yellow", "orange", "black", "purple"]

for i in range(50):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    c = random.randint(0, len(color) - 1)
    turtle.setposition(x, y)
    turtle.dot(50, color[c])

turtle.done()
