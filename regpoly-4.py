

import turtle

wn=turtle.Screen()

A=turtle.Turtle()
B=turtle.Turtle()
C=turtle.Turtle()
D=turtle.Turtle()

A.shape('circle')
B.shape('turtle')
C.shape('triangle')
D.shape('arrow')

A.color('red')
B.color('green')
C.color('yellow')
D.color('blue')



A.penup()
B.penup()
C.penup()
D.penup()

A.goto(-200,200)
B.goto(200,200)
C.goto(-200,-200)
D.goto(200, -200)

A.pendown()
B.pendown()
C.pendown()
D.pendown()

X=int(input('number of sides: '))
Y=int(input('size of sides: '))

F=360/X

for _ in range (50):
    A.forward(Y)
    A.left(F)
    A.forward(Y)

    B.forward(Y)
    B.left(F)
    B.forward(Y)

    C.forward(Y)
    C.left(F)
    C.forward(Y)

    D.forward(Y)
    D.left(F)
    D.forward(Y)
