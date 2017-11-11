from Renderer import screen,size,clock
from Sprite import Sprite
import pyglet


#load images


done = False
while done == False:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	screen.fill((255, 255, 255))

	pygame.draw.rect(screen, (0,0,0), (100, 100, 100, 100))

	spriteList = [Sprite(["test"],0,0),Sprite(["test"],1,1)]
	for sp in spriteList:
		sp.draw()
	pygame.display.update()
	clock.tick(60)

pygame.quit()
