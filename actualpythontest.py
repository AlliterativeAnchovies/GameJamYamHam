from Renderer import screen,size,clock
from Sprite import Sprite
from Movable import Movable
from Tile import Tile
from Pickup import Pickup
import pygame


#load images


done = False
while done == False:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	screen.fill((255, 255, 255))

	pygame.draw.rect(screen, (0,0,0), (100, 100, 100, 100))
	dummyspritedict = {"defaultstate":["test"]}
	spriteList = [Sprite(dummyspritedict,0,0)]
	for sp in spriteList:
		sp.draw()
	pygame.display.update()
	clock.tick(60)

pygame.quit()
