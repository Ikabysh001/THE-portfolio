import random
import pygame

pygame.init()

i=0
fps = 100
clock = pygame.time.Clock()
window_width = 612
window_height = 382

gameDisplay = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Collector_1')


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images\ghost.png")
        self.size = self.image.get_rect().size
        self.image = pygame.transform.scale(self.image, (int(self.size[0] / 5.5), int(self.size[1] / 5.5)))
        self.size = self.image.get_rect().size
        self.rect = self.image.get_rect()
        self.rect.x = pygame.mouse.get_pos()[0]
        self.rect.y = pygame.mouse.get_pos()[1]

    def update(self):
        self.rect.x = pygame.mouse.get_pos()[0] -self.size [0]/2
        self.rect.y = pygame.mouse.get_pos()[1] -self.size [1]/2


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images\coin.png")
        self.size = self.image.get_rect().size
        self.image = pygame.transform.scale(self.image, (int(self.size[0] / 10), int(self.size[1] / 10)))
        self.size = self.image.get_rect().size
        self.rect = self.image.get_rect()
        self.rect.x=random.randint (0,612)
        self.rect.y = random.randint(0,382)

    def update (self):
        collision=pygame.sprite.spritecollide(self,player_gp,False,False)
        print(collision)



coin_gp = pygame.sprite.Group()

while i < 30:
    coin = Coin()
    i = i + 1
    coin_gp.add(coin)



player_gp = pygame.sprite.Group()
player = Player()
player_gp.add(player)

bg = pygame.image.load("images\\back.jpg")

while True:
    clock.tick(fps)
    gameDisplay.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

    coin_gp.update()
    player_gp.update()
    coin_gp.draw(gameDisplay)
    player_gp.draw(gameDisplay)
    pygame.display.flip()
