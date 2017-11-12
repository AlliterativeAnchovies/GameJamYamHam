from Sprite import Sprite
from Renderer import SPRITE_SIZE,GRID_SIZE,SCREEN_WIDTH,allSprites,gridList,spriteList,board
from GridGenerator import generateNewGrid
import pygame,os

GRID_PIXEL_SIZE = (GRID_SIZE*SPRITE_SIZE)

class Tile(Sprite):
    #Tiles are initialized just like Sprites
    #Except tiles are also either Passable or Not,
    #And they have an amount of damage that they deal when passed over
    def __init__(self,sprites,locationX,locationY,passable,damage):
        Sprite.__init__(self,sprites,locationX,locationY)
        self.passable = passable
        self.damage = damage
        self.pickup = None
        self.moveable = None

    def clone(self):
        toReturn = super(Tile,self).clone()
        toReturn.passable = passable
        toReturn.damage = damage
        toReturn.pickup = self.pickup.clone() if self.pickup else None
        toReturn.moveable = self.moveable.clone() if self.moveable else None
        return toReturn

class Grid:
    #this represents our 4x4 chunks of tiles
    #Takes in 3 arguments, a 4x4 2d list of tiles
    #and a position (x,y)
    def __init__(self,tileList,positionX,positionY):
        self.tiles = tileList
        self.px = positionX
        self.py = positionY
        for row in range(0,len(self.tiles)):
            for col in range(0,len(self.tiles[row])):
                self.tiles[row][col].changePosition(self.px+col*SPRITE_SIZE,self.py+row*SPRITE_SIZE)
        self.px = positionX


    #moves a grid by its two agruments, (amountX,amountY)
    def move(self,amountX,amountY):
       self.px += amountX
       self.py += amountY
       for row in range(0,len(self.tiles)):
           for col in range(0,len(self.tiles[row])):
               self.tiles[row][col].changePosition(self.px+col*SPRITE_SIZE,self.py+row*SPRITE_SIZE)

class Screen:
    def __init__(self):
        self.px = 0
        self.py = 0

    def addToScreen(self, grid, x, y):
        global spriteList
        tileList = []
        for row in range(len(grid.tiles)):
            tileList.append([])
            for col in range(len(grid.tiles[row])):
                newTile = grid.tiles[row][col].clone()
                spriteList.append(newTile)
                tileList[row].append(newTile)
        return Grid(tileList, x, y)

    def generateInitialScreen(self):
        gridColsThatFitOnScreen = SCREEN_WIDTH//GRID_PIXEL_SIZE + 1
        self.gridList = []
        for row in range(6): # Should be changed to constant in renderer
            self.gridList.append([])
            for col in range(gridColsThatFitOnScreen):
                leftGrid = self.gridList[row][-1] if len(self.gridList[row]) > 0 else None
                topGrid = self.gridList[row-1][-1] if row-1 >= 0 else None
                self.gridList[row].append(generateNewGrid(self, leftGrid, topGrid, col*GRID_PIXEL_SIZE, row*GRID_PIXEL_SIZE))
    def move(self, amountX, amountY):
        self.px += amountX
        self.py += amountY

        rows = len(self.gridList)

        # When the left-most-grid falls off the screen
        if self.px % GRID_PIXEL_SIZE == 0:
            for row in range(rows):
                del self.gridList[row][0]

        # When the right-most-grid needs to be generated
        if (self.px + SCREEN_WIDTH) % GRID_PIXEL_SIZE == 0:
            for row in range(rows):
                leftGrid = self.gridList[row][-1]
                upGrid = self.gridList[row-1][-1] if rows-1 >= 0 else None
                self.gridList[row].append(generateNewGrid(leftGrid, topGrid))

        for row in range(rows):
            for col in range(len(self.gridList[row])):
                self.gridList[row][col].move(amountX, amountY)


def loadGrids():
    global board

    getfiles = os.listdir('./resources/grids')
    bmpfiles = [x for x in getfiles if x[len(x)-1]=='p']
    bmpimages = []
    for image in bmpfiles:
        relevantImage = pygame.image.load('resources/grids/'+image)
        relevantPixels = pygame.PixelArray(relevantImage)
        tileList = []
        for i in range(0,GRID_SIZE):
            tileRow = []
            for j in range(0,GRID_SIZE):
                pixelcolor = (relevantPixels[i][j]<<8)>>8 #shifting so that we get rid of alpha values
                if (pixelcolor==0x00ffffff):
                    dummyspritedict = {"defaultstate":["Base Tile 1"]}
                    tiletoappend = Tile(dummyspritedict,0,0,True,False)
                    tileRow.append(tiletoappend)
                elif (pixelcolor==0x000000):
                    dummyspritedict = {"defaultstate":["Test"]}
                    tiletoappend = Tile(dummyspritedict,0,0,False,True)
                    tileRow.append(tiletoappend)
                else:
                    print("I hate my life")
            tileList.append(tileRow)
        gridList.append(Grid(tileList,0,0))

    board = Screen()
    board.generateInitialScreen()
