

import turtle

wn=turtle.Screen()


line=turtle.Turtle()

D=20

line.right(30)

for _ in range (30):
    line.forward(D)
    line.right(120)
    line.forward(D)
    D=D+10
