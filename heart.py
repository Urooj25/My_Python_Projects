import turtle
import math

t = turtle.Turtle()
t.speed(7)
t.width(2)
t.color("red")

turtle.bgcolor("black")

def heart():
    t.begin_fill()
    t.left(140)
    t.forward(111)

    for i in range(200):
        t.right(1)
        t.forward(1)

    t.left(120)

    for i in range(200):
        t.right(1)
        t.forward(1)

    t.forward(111)
    t.end_fill()

for i in range(36):
    heart()
    t.right(10)

turtle.done()
