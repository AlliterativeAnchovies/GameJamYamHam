#This is our actual 'main' file that we should compile.  "actualpythontest.py" should
#be used for testing (so we don't cause clashes if we both edited Main.py to test
#our code.  It's okay if actualpythontest.py classes because it's not going to be part
#of our actual finished project.  In fact, it should probably be added to a gitignore
#but I'm too lazy to do that.

#import Renderer
import Renderer
from Sprite import Sprite
from Movable import Movable
from Pickup import Pickup
from Tile import loadGrids,board,Tile
from Enemy import Enemy,initializeEnemies
from Friendly import Friendly
import pygame
import Snek

#sprite images are loaded in Renderer.py as allSprites
#the window is also initialized there

#initialize everything

def init():
	Renderer.loadSprites()
	initializeEnemies()
	loadGrids()
	#print(spriteList)

#draw everything
def drawLoop():
	Renderer.tick.append(Renderer.tick[0]+1)
	Renderer.tick.pop(0)
	Renderer.screen.fill((255, 255, 255))
	for drawable in Renderer.tileList:
		Tile.draw(drawable)
	for drawable in Renderer.enemyList:
		Enemy.draw(drawable)
	for drawable in Renderer.snekParts:
		Friendly.draw(drawable)
	pygame.display.update()
	Renderer.screen.fill((0,0,0,0))
	board.move(-1,0)
	return False

#runs the actual game
def gameLoop():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			return True
		if event.type == pygame.KEYDOWN:
			pressMap = {
				pygame.K_DOWN: (0,-1),
				pygame.K_UP: (0,1),
				pygame.K_LEFT: (-1,0),
				pygame.K_RIGHT: (1,0),

				}
			if event.key in pressMap:
				Snek.moveSnek(*pressMap[event.key])

	#init enemies when they are almost on screen
	for enemy in Renderer.enemiesToInit:
		if (enemy.px<Renderer.SCREEN_WIDTH+2*Renderer.SPRITE_SIZE):
			Enemy.finish_init(enemy)
	#remove excess enemies
	Renderer.enemiesToInit = [x for x in Renderer.enemiesToInit if not Enemy.isinit(x)]
	for enemy in Renderer.enemyList:
		if (Enemy.isinit(enemy)):
			Enemy.update(enemy)

	return False


DRAW_TO_GAME_RATIO = 1#ratio of draw updates to game updates
#controls the flow of the program
def controlLoop():
	error = False
	while not error:
		error = error or drawLoop()#todo: add some kind of tick control mechanism
		error = error or gameLoop()#for updating these (for example, update gameLoop 1/3 as often)
		Renderer.clock.tick(60)

#run the code
init()
controlLoop()
