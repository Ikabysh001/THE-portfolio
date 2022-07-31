import turtle
import random

turtle.colormode(255)

z = turtle.Turtle()
z.speed(0)
i=0
while i<10:
    x = random.randint(-250,250)
    y = random.randint(-300,255)

    r = random.randint(100,255)
    g = random.randint(100,255)
    b = random.randint(100,255)
    
    z.penup()
    z.goto(x,y)
    z.pendown()

    z.begin_fill()
    z.color(r,g,b)
    z.circle(random.randint(0,50))

    z.end_fill()

i=i+1
