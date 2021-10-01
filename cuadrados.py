
import turtle
import time

wn=turtle.Screen()
cube=turtle.Turtle()

squares=50
size=40
angle=20

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

time.sleep(10)

# create a red colured heart using turtle graphics

# from turtle import *
# color("red")
# begin_fill()
# pensize(4)
# left(50)
# forward(133)
# circle(50,200)
# right(140)
# circle(50,200)
# forward(133)
# end_fill()
# time.sleep(5)
