


import turtle
import random

wn=turtle.Screen()
alex=turtle.Turtle()


r=100
ax=90

X=random.randrange (1, 50)
Y=random.randrange(1, 50)

for _ in range (100):
    alex.goto(X,Y)
    alex.circle(r, ax)
    alex.penup()
    alex.goto(X,Y)
    alex.circle(r, ax)
    alex.pendown()
