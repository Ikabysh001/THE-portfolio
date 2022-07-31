import turtle


z = turtle.Turtle()
z.speed(0)

colors = ["red","green","blue","yellow","orange","indigo","GreenYellow","bisque","MintCream","mistyrose","NavajoWhite"]


color_i = 0
i=0
while i< 100:
    
    z.color(colors[color_i])
    z.left(1)
    count=0        
    z.begin_fill()
    while count < 4:
        z.forward(100)
        z.left(90)
        count=count+1
    z.end_fill()
    i=i+1
    if color_i < 10:
        color_i = color_i + 1
    else:
        color_i = 0
    
    
