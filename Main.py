#This is our actual 'main' file that we should compile.  "actualpythontest.py" should
#be used for testing (so we don't cause clashes if we both edited Main.py to test
#our code.  It's okay if actualpythontest.py classes because it's not going to be part
#of our actual finished project.  In fact, it should probably be added to a gitignore
#but I'm too lazy to do that.

from Renderer import screen,size,clock,SPRITE_SIZE,GRID_SIZE
from Sprite import Sprite
from Movable import Movable
from Tile import Tile,Grid
from Pickup import Pickup
import pygame

#sprite images are loaded in Renderer.py as allSprites
#the window is also initialized there

spriteList = []
gridList = []
#initialize everything
def init():
    global spriteList,gridList
    #here we are creating grids.  Grids are 4x4 sets of tiles
    agrid = []
    for i in range (0,GRID_SIZE):
        agrid.append([])
        for j in range (0,GRID_SIZE):
            dummyspritedict = {"defaultstate":["test"]}
            dummysprite = Sprite(dummyspritedict,i*SPRITE_SIZE,j*SPRITE_SIZE)
            spriteList.append(dummysprite)
            agrid[i].append(dummysprite)
    gridList.append(Grid(agrid,GRID_SIZE/2,GRID_SIZE/2))

#draw everything
def drawLoop():
    screen.fill((255, 255, 255))
    for drawable in spriteList:
        drawable.draw()
    pygame.display.update()
    return False

#runs the actual game
def gameLoop():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                gridList[0].move(5,5)
    return False


#controls the flow of the program
def controlLoop():
    error = False
    while not error:
        error = error or drawLoop()#todo: add some kind of tick control mechanism
        error = error or gameLoop()#for updating these (for example, update gameLoop 1/3 as often)
        clock.tick(60)

#run the code
init()
controlLoop()
