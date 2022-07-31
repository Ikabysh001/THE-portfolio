import  turtle


z=turtle.Turtle()
z.speed(0)
i=0
b=1
a=0

z.color("green")

z.penup()
z.goto(-300,100)
z.pendown()

z.pensize(15)

while a<10:
    i =0
    while i<180:
        #print("a=",str(a),"i=",str(i))
        z.forward(b)
        z.right(1)
        i=i+1
    a = a + 1
    b = b + -0.1

#https://inotgo.com/imagesLocal/202110/19/20211019042942119W_0.png
'''
z.penup()
z.goto(300,100)
z.pendown()

z.circle(30)
'''
