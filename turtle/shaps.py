 
import turtle


z = turtle.Turtle()
z.speed(0)

 #fd(10) / left(90) / lt() / right() / rt() / bd() / backward()  / obj.dosomething(params) - robot.footUP()

count = 0
while count <100:
    z.forward(100)
    z.left(360)
    count = count +1 #loops as  with change number 4 - makes forever loop 


## homework
    #https://www.teachwithict.com/uploads/5/5/8/2/5582303/challenge-cards_1.png
    #5 and up
count = 0
while count <5   :
    z.right (144)
    z.forward (100)
    count = count +1



'''
i = 0
length = 100
while i < 5:
    count = 0
    while count < 4:
        z.forward(length)
        z.left(90)
        count=count+1
    i = i + 1
    length = length + 20
'''

'''
i=0
while i< 30:
    z.left(10)
    count=0        
    while count < 4:
        z.forward(100)
        z.left(90)
        count=count+1
    i=i+1




'''i=0
while i<4:
    z.right(180)
    count=0
    while count <3:
        z.forward(100)
        z.right(90)
        count=count+1
    i=i+1
'''

z.left(180)
count=0
while count <3:
    z.forward(200)
    z.right(120)
    count=count+1
z.forward(100)
z.right (45)
z.forward(100)
z.right(135)
z.forward(130)
z.right(135)
z.forward (100)

