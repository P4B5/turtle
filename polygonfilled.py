import turtle

alex=turtle.Turtle()
wn=turtle.Screen()



num=int(input('number of sides: '))
leng=int(input('lenght of the side: '))

col=input('color of line: ')
fillcol=input('fill color: ')

alex.color(col)

ang=360/num

for _ in range (num):
    alex.pensize(8)
    alex.forward(leng)
    alex.left(ang)
    alex.forward(leng)

for _ in range (2000):
    alex.color(fillcol)
    alex.pensize(3)
    alex.speed(0)
    alex.forward(leng)
    alex.left(ang)
    alex.forward(leng)
    leng=leng-0.05

wn.exitonclick()
