import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.color("red")
t.width(2)
t.left(90)
t.penup()
t.goto(0,-250)
t.pendown()

def tree(branch):
    if branch < 8:
        t.dot(6,"red")
        return
    
    t.forward(branch)
    
    angle = random.randint(15,25)

    t.right(angle)
    tree(branch - random.randint(10,15))

    t.left(angle*2)
    tree(branch - random.randint(10,15))

    t.right(angle)
    t.backward(branch)

tree(120)

turtle.done()