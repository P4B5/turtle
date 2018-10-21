
import turtle

wn=turtle.Screen()
cube=turtle.Turtle()


squares=int(input('write the number of squares:'))
size=int(input('write size of the squares'))
angle=int(input('write the grades of the angle'))

cube.right(angle)


for _ in range(squares):
    cube.right(angle)
    for _ in range(1):

        #cube.goto(0,0)
        cube.forward(size)
        cube.right(90)
        cube.forward(size)
        cube.right(90)
        cube.forward(size)
        cube.right(90)
        cube.forward(size)
