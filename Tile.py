from Sprite import Sprite
from Renderer import SPRITE_SIZE,GRID_SIZE,SCREEN_WIDTH,allSprites
from GridGenerator import generateNewGrid


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
        toReturn = Sprite.clone(self)
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
        gridColsThatFitOnScreen = SCREEN_WIDTH//GRID_PIXEL_SIZE + 1
        self.gridList = []
        for row in range(6): # Should be changed to constant in renderer
            self.gridList.append([])
            for col in range(gridColsThatFitOnScreen):
                leftGrid = self.gridList[row][-1] if len(self.gridList[row]) > 0 else None
                topGrid = self.gridList[row-1][-1] if row-1 >= 0 else None
                self.gridList[row].append(generateNewGrid(leftGrid, topGrid))

        self.px = 0
        self.py = 0

    def addToScreen(self, grid):
        tileList = []
        for row in range(len(grid.tiles)):
            tileList.append([])
            for col in range(len(grid.tiles[row])):
                newTile = grid.tiles[row][col].clone()
                allSprites.append(newTile)
                tileList[row].append(newTile)

        return Grid(tileList, grid.positionX, grid.positionY)

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

                
