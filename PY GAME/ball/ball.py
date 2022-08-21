import pygame,random

pygame.init()


fps = 100
clock = pygame.time.Clock()
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
		self.rect.x=pygame.mouse.get_pos()[0]
		self.rect.y=pygame.mouse.get_pos()[1]
		self.gravity = -5
		self.x_speed = random.randint(-5,5)
		self.y_speed = random.randint(-5,5)

	def update(self):
		self.rect.x=self.rect.x+self.x_speed
		self.rect.y=self.rect.y+self.gravity
		self.gravity=self.gravity+5

ball_gp = pygame.sprite.Group()
ball = Ball()
ball2 = Ball()
ball_gp.add(ball)
ball_gp.add(ball2)


while True:
	pressed = pygame.mouse.get_pressed()
	if pressed [0]== True:
		ball=Ball()
		ball_gp.add(ball)
	clock.tick(fps)
	gameDisplay.fill((0,0,0))
	for event in pygame.event.get():
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_ESCAPE:
				pygame.quit()
				quit()


	ball_gp.update()
	ball_gp.draw(gameDisplay)
	pygame.display.flip()
