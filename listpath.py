import turtle

wn=turtle.Screen()
alex=turtle.Turtle()

lst=[160,-43, 270, -97, -43, 200, -940, 17, -86]

for a in lst:
    alex.forward(100)
    alex.right(a)
