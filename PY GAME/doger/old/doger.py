import pygame
import random
import time
score=1

pygame.init()
enemy_speed=score/2
green = (10,250,33)

enemy_w = 75
enemy_h = 140

enemy_image=pygame.image.load("enemy.png")
enemy_image=pygame.transform.scale(enemy_image,(enemy_w,enemy_h))
enemy_image=pygame.transform.rotate(enemy_image,180)


player_image=pygame.image.load("us.png")
player_image=pygame.transform.scale(player_image,(75,125))



def draw_enemy(x,y):
    screen.blit(enemy_image,(x,y))


def draw_player(x,y):
    screen.blit(player_image,(x,y))


def draw_text(text,x,y,color,size):
    my_font=pygame.font.SysFont("Marker Felt",size)
    text_surface=my_font.render(text,False,color)
    screen.blit(text_surface,(x,y))


screen_width=700
screen_height=777
screen=pygame.display.set_mode((screen_width,screen_height))

black = (0,0,0)
white = (255,255,255)
playerx = 250


playery = 600
enemyx = random.randint(97,612)
enemyy = 0
player_direction=1

background=pygame.image.load("road.jpeg")
background=pygame.transform.scale(background,(screen_width,screen_height))


while True:
    playerx=playerx+player_direction
    screen.fill(white)
    screen.blit(background,(0,0))
    '''
        pygame.draw.rect(screen,black,(playerx,playery,75,125))#player
        pygame.draw.rect(screen,black,(enemyx,enemyy,75,125))#enemy
    '''
    draw_enemy(enemyx,enemyy)

    draw_player(playerx,playery)
    
    if playerx < 97 or playerx+75 > 612:
        draw_text("GAME OVER",275,200,black,50)
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        break
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player_direction = player_direction - 1 
                #i=i+1

            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player_direction= player_direction + 1 #chnage
                #player_direction = 1 #set

    enemyy=enemyy+enemy_speed
    if enemyy>770:
        enemyy = 0
        
        
        score=score+1
        enemyx = random.randint(97,550)
    draw_text("Score: "+str(score),350,0,green,25)
            

 

    if enemyy+enemy_h>playery and enemyy<playery+125: #second part of y colision
        #print ("Y colllision")
        if enemyx < playerx + 75 and enemyx+75 > playerx: #and enemyx+75 < playerx+75:
            draw_text("GAME OVER",275,200,black,50)
            pygame.display.update()
            time.sleep(2)
            pygame.quit()
            break

    pygame.display.update()
