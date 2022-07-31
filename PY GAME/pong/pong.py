import pygame
import random
import time

pygame.init()

def draw_text(text,x,y,color,size):
    my_font=pygame.font.SysFont("Marker Felt",size)
    text_surface=my_font.render(text,False,color)
    screen.blit(text_surface,(x,y))


screen_width=800
screen_height=700
screen=pygame.display.set_mode((screen_width,screen_height))
blue = (0,0,0)
red = (0,0,0)
black=(0,0,0)
cool=(255, 255, 255)
score=0

x = 400
y = 650

x1 = 100
y1 = 100

x_direction = random.choice([-1,1,-2,2])
y_direction = random.choice([-1,1,-2,2])
paddle_direction=1


while True:
    #code here
    screen.fill(cool)
    pygame.draw.rect(screen,blue,(x,y,200,25)) #(x,y,width,hight)
    pygame.draw.rect(screen,red,(x1,y1,30,30))

    if x1 + 30 > screen_width: #right
        x_direction = x_direction * -1
    if x1 < 0: #left
        x_direction = x_direction * -1
    if y1 < 0:#top
        y_direction = y_direction * -1


    if y1 + 30 > screen_height:
        draw_text("GAME OVER",275,200,black,50)
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        break
        
    
    x1 = x1 + x_direction #movement
    y1 = y1 + y_direction
    x = x + paddle_direction

    if y1 + 30 > y and y1 + 30 < y+20: #paddle bounce
        if x1>x and x1+30 < x+200:
            y_direction = y_direction * -1
            score=score+1
    draw_text("Score: "+str(score),350,0,black,25)
            

    for event in pygame.event.get(): 
        if event.type==pygame.QUIT:
            pygame.quit()
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                paddle_direction=-1.5

            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                paddle_direction=1.5
            
    pygame.display.update()
