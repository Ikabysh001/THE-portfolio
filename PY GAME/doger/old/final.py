import pygame
import random
import time
pygame.init()

screen_width, screen_height = 710,770
screen=pygame.display.set_mode((screen_width,screen_height))
background=pygame.image.load("road.jpeg")
background=pygame.transform.scale(background,(screen_width,screen_height))

green = (10,250,33)
black = (0,0,0)


def draw_enemy(x,y):
    screen.blit(enemy_image,(x,y))


def draw_player(x,y):
    screen.blit(player_image,(x,y))


def draw_text(text,x,y,color,size):
    my_font=pygame.font.SysFont("Marker Felt",size)
    text_surface=my_font.render(text,False,color)
    screen.blit(text_surface,(x,y))

def game_over():
    draw_text("GAME OVER", 275, 200, black, 50)
    pygame.display.update()
    time.sleep(2)
    pygame.quit()


score=0
player_image=pygame.image.load("us.png")
player_image=pygame.transform.scale(player_image,(75,125))
playerx = 250
playery = 600
player_direction=0
player_acc = 0
player_breaking = False

enemy_w = 75
enemy_h = 140
enemy_speed=(score/2)+1
enemyx = random.randint(97,612)
enemyy = 0
enemy_image=pygame.image.load("enemy.png")
enemy_image=pygame.transform.scale(enemy_image,(enemy_w,enemy_h))
enemy_image=pygame.transform.rotate(enemy_image,180)


while True:
    #events and key handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        if event.type == pygame.KEYDOWN: #key pressed
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player_acc = -0.1
                player_breaking = False
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player_acc = 0.1
                player_breaking = False
        if event.type == pygame.KEYUP: #key released
            if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player_acc = 0
                player_breaking = True

    # road boundaries
    if playerx < 97 or playerx + 75 > 612:
        game_over()
        break

    #collision
    if enemyy+enemy_h>playery and enemyy<playery+125:
        if enemyx < playerx + 75 and enemyx+75 > playerx: #and enemyx+75 < playerx+75:
            game_over()
            break

    #acceleration
    if player_acc != 0 :
        player_direction = player_direction + player_acc

    #breaking
    if player_breaking == True:
        if player_direction > 0:
            player_direction = player_direction - 0.07
        elif player_direction < 0:
            player_direction = player_direction + 0.07
        if player_direction < 0.2 and player_direction > -0.2:
            player_direction = 0

    #enemy teleport
    if enemyy > screen_height:
        enemyy = 0
        score=score+1
        enemyx = random.randint(97,550)
    
    #object movement
    playerx = playerx + player_direction
    enemyy=enemyy+enemy_speed

    #drawing
    screen.blit(background,(0,0))
    draw_text("Score: "+str(score),350,0,green,25)
    draw_enemy(enemyx,enemyy)
    draw_player(playerx,playery)

    pygame.display.update()
