import turtle
import random

# screen setup
screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.left(90)
t.penup()
t.goto(0, -250)
t.pendown()
t.color("brown")

def blossom_tree(branch):
    if branch < 10:
        # cherry blossom
        t.color("pink")
        t.dot(8)
        t.color("brown")
        return

    t.forward(branch)

    angle = random.randint(15,30)

    t.right(angle)
    blossom_tree(branch - random.randint(10,15))

    t.left(angle * 2)
    blossom_tree(branch - random.randint(10,15))

    t.right(angle)
    t.backward(branch)

# draw tree
blossom_tree(100)

turtle.done()