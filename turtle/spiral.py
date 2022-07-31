'''
import turtle

z= turtle.Turtle()
z.speed(0)

#z.circle(50) - > forget


i = 0

while i< 360:
    z.fd(1)
    z.lt(1)
    i = i + 1


# https://media.geeksforgeeks.org/wp-content/uploads/20200117183856/Annotation-2020-01-17-183938-300x263.png
'''
import turtle
import random
color_i = 0
i = 0
colors = ["red","green","blue","yellow","orange","indigo","GreenYellow","bisque","MintCream","mistyrose","NavajoWhite"]

a = turtle.Turtle()
r = random.randint(0,10)
a.speed(0)
while i< 1000:
    a.forward(i/15)
    a.color(colors[r])
    r=random.randint(0,10)
    a.right(10)
    i = i + 1
    color_i=color_i+1
    if color_i < 10:
        color_i = color_i + 1
    else:
        color_i = 0
