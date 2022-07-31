import turtle


z = turtle.Turtle()

z.color("dark blue")
z.begin_fill()

count=0
while count <4:
    z.forward(100)
    z.right(90)
    count=count+1
z.end_fill()
