import pygame
from Sprite import Sprite

pygame.init()
size = [640, 480]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('My Game')
clock = pygame.time.Clock()

done = False
while done == False:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	screen.fill((255, 255, 255))

	pygame.draw.rect(screen, (0,0,0), (100, 100, 100, 100))

	spriteList = [Sprite('',0,0),Sprite('',1,1)]
	pygame.display.update()
	clock.tick(60)

pygame.quit()
