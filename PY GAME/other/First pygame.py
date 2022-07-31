import pygame
import random

pygame.init()

screen_width=500
screen_height=500
screen=pygame.display.set_mode((screen_width,screen_height))
blue = (1,123,255)

x = 200
y = 200

x_direction = random.choice([-1,1,2,-2])
y_direction = random.choice([-1,1,2,-2])

while True:
    #code here
    screen.fill((0,0,150))
    pygame.draw.rect(screen,blue,(x,y,100,100)) #(x,y,width,hight)
    
    if x + 100 > screen_width:
        x_direction = -1

    if x < 0:
        x_direction = 1

    if y < 0:
        y_direction = 1

    if y + 100 > screen_height:
        y_direction = -1

        
    x=x + x_direction
    y=y + y_direction
    

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            
    pygame.display.update()
