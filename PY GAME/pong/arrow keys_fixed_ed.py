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
blue = (1,123,255)
blue2 = (4,5,244)
black = (0,0,0)
pink = (231,209,241)

paddle_x = 400
paddle_y = 650

ball_x = 100
ball_y = 100
ball_w = 30 # Ball width
ball_h = 30 # Ball height

x_direction = random.choice([-1,1,-2,2])
y_direction = random.choice([-1,1,-2,2])
paddle_direction=1

while True:
    screen.fill(pink)
    pygame.draw.rect(screen,blue,(paddle_x,paddle_y,200,25)) #Paddle (x,y,width,hight)
    pygame.draw.rect(screen,blue2,(ball_x,ball_y,ball_w,ball_h)) #Ball

    if ball_x + ball_w > screen_width: #right
        x_direction = x_direction * -1
    if ball_x < 0: #left
        x_direction = x_direction * -1
    if ball_y < 0:#top
        y_direction = y_direction * -1


    if ball_y + ball_h > screen_height:
        draw_text("GAME OVER",275,200,black,50)
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        break
        
    ball_x=ball_x + x_direction
    ball_y=ball_y + y_direction
    paddle_x = paddle_x + paddle_direction

    if ball_y + ball_h > paddle_y and ball_y + ball_h< paddle_y + 25: #paddle bounce
        if ball_x>paddle_x and ball_x+ball_w < paddle_x+200:
            y_direction = y_direction * -1

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
