from Renderer import screen,size,clock
from Sprite import Sprite
import pygame

done = False
while done == False:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	screen.fill((255, 255, 255))

	pygame.draw.rect(screen, (0,0,0), (100, 100, 100, 100))

	spriteList = [Sprite('',0,0),Sprite('',1,1)]
	for sp in spriteList:
		sp.draw()
	pygame.display.update()
	clock.tick(60)

pygame.quit()
