

import turtle

wn=turtle.Screen()
line=turtle.Turtle()

N1=int(input('write the number of sides you want: '))#N1
S1=int(input('write the size of the side: ')) #N2

print ('sides: ', N1)
print ('size: ', S1)


AN=360/N1

for _ in range (100):
    line.forward(S1)
    line.left(AN)
    line.forward(S1)



#other form to do using if

'''

if (N1=='3'):
    for _ in range (3):
        line.forward(S1)
        line.left(120)
        line.forward(S1)
        line.left(120)
elif (N1 =='4'):
    for _ in range (3):
        line.forward(S1)
        line.left(90)
        line.forward(S1)
        line.left(90)
elif (N1 =='5'):
    for _ in range (4):
        line.forward(S1)
        line.left(72)
        line.forward(S1)
        line.left(72)

elif (N1 =='6'):
    for _ in range (5):
        line.forward(S1)
        line.left(45)
        line.forward(S1)
        line.left(45)

elif (N1 =='7'):
    for _ in range (6):
        line.forward(S1)
        line.left(51.75)
        line.forward(S1)
        line.left(51.75)

elif (N1 =='8'):
    for _ in range (7):
        line.forward(S1)
        line.left(45)
        line.forward(S1)
        line.left(45)
'''
