
import turtle
z= turtle.Turtle()
z.speed(0)
z.shape ("turtle")
window = turtle.Screen()
window.bgcolor("light blue")
pen_down =  True

def turn_left():
    z.left (15)


def turn_right():
    z.right (15)


def go_up():
    z.forward (20)

def go_down():
    z.backward (20)

def pen_up():
    global pen_down
    if pen_down == True:
        z.penup()
        pen_down = False
    else:
        z.pendown()
        pen_down = True



    
window.onkeypress(turn_left,"Left")
window.onkeypress(turn_right,"Right")
window.onkeypress(go_up,"Up")
window.onkeypress(go_down,"Down")
window.onkeypress(pen_up,"a")


window.listen()
turtle.done()
