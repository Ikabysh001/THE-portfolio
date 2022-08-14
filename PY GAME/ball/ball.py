import pygame,random

pygame.init()


window_width=500

window_height=500

gameDisplay = pygame.display.set_mode((window_width,window_height))

pygame.display.set_caption('Ball')


class Ball(pygame.sprite.Sprite):

	def __init__(self):

		pygame.sprite.Sprite.__init__ (self)

		self.image=pygame.Surface((20,20))

		self.image.fill((0,0,0))

		pygame.draw.circle(self.image,(random.randint(0,255),random.randint(0,255),random.randint(0,255),random.randint(0,255)),(10,10),10,0)

		self.rect=self.image.get_rect()

		self.rect.x, self.rect.y=pygame.mouse.get_pos()

		self.x_speed, self.y_speed  = random.randint(-15,15),random.randint(-15,15)

		self.gravity = 0.7

ball_gp = pygame.sprite.Group()

ball = Ball()

ball_gp.add(ball)

while True:

	for event in pygame.event.get():

		if event.type==pygame.KEYDOWN:

			if event.key==pygame.K_ESCAPE:

				pygame.quit()

				quit()


	ball_gp.update()
	
	ball_gp.draw(gameDisplay)
	
	pygame.display.flip()
