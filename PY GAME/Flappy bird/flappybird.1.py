import pygame
import random
pygame.init()


#variables
gravity=0.8
score=0
green=(0,255,0)
enemyx = 900
enemyy = 300
enemyxsize= 250
enemyxsize=1435

#Screen init
screen_width, screen_height = 927,575
screen = pygame.display.set_mode((screen_width,screen_height))
screen = pygame.display.set_mode((screen_width,screen_height))

#Background
background=pygame.image.load("images/bg.jpg")
background=pygame.transform.scale(background,(screen_width,screen_height))

#player init
playerx = 250
playery = 400
orig_x = 171
orig_y = 122
player_scale = 0.3
player_image=pygame.image.load("images/good bird.png")
player_image=pygame.transform.scale(player_image,(orig_x*player_scale,orig_y*player_scale))



#put this in to draw
def draw_text(text,x,y,color,size):
    my_font=pygame.font.SysFont("Marker Felt",size)
    text_surface=my_font.render(text,False,color)
    screen.blit(text_surface,(x,y))
    

def draw_pipe(x,y,gap,gap2):
    screen.blit(fl_enemy_image,(x,y-gap))
    screen.blit(enemy_image,(x,y-gap2))


def draw_player(x,y):
    screen.blit(player_image,(x,y))


#enemy stuff
enemy_image=pygame.image.load("images/pipe.png")
enemy_image = pygame.transform.scale(enemy_image,(50,280))
fl_enemy_image =pygame.transform.rotate(enemy_image,180)

#g=gap btw
g = random.randint(450,550)
g2 = random.randint(-50,0)


#mainloop
while True:
    #movement
    enemyx=enemyx-0.5
    playery=playery+gravity
    
    #pipe shift
    if enemyx<0:
        enemyx=900
        g = random.randint(450,550)
        g2= random.randint(-50,0)
        score=score+1

    #event and button handling
    for event in pygame.event.get():
        if event.type==pygame.QUIT: 
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_a:
                playery=playery-60
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                break
    #collision

    if playery>screen_height or playery<0:
        print("game over failiure, wake up")

    if enemyx < playerx+(177*0.3) and enemyx +enemyxsize > playerx:
    	print("collsion")

        


    #drawing
    screen.blit(background,(0,0))
    draw_player(playerx,playery)
    draw_pipe(enemyx,enemyy,g,g2)
    draw_text("Score: "+str(score),450,0,green,25)
    
    pygame.display.update() #displays frame
