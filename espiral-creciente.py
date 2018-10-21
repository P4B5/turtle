

import turtle

wn=turtle.Screen()
alex=turtle.Turtle()


size=1
sides=800
figure=10


alex.pensize(5)
alex.speed(8)

for _ in range(800):
    alex.forward(size)
    alex.left(figure)
    alex.forward(size)
    size=size+0.07
