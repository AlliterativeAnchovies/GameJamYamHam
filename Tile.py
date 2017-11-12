from Sprite import Sprite
from Renderer import SPRITE_SIZE

class Tile(Sprite):
    #Tiles are initialized just like Sprites
    #Except tiles are also either Passable or Not,
    #And they have an amount of damage that they deal when passed over
    def __init__(self,sprites,locationX,locationY,passable,damage):
        Sprite.__init__(self,sprites,locationX,locationY)
        self.passable = passable
        self.damage = damage

class Grid:
    #this represents our 4x4 chunks of tiles
    #Takes in 3 arguments, a 4x4 2d list of tiles
    #and a position (x,y)
    def __init__(self,tileList,positionX,positionY):
        self.tiles = tileList
        self.px = positionX-SPRITE_SIZE*2
        self.py = positionY
        for row in range(0,len(self.tiles)):
            for col in range(0,len(self.tiles[row])):
                self.tiles[row][col].changePosition(self.px+col*SPRITE_SIZE,self.py+row*SPRITE_SIZE)
        self.px = positionX

    #moves a grid by its two agruments, (amountX,amountY)
    def move(self,amountX,amountY):
       self.px += amountX-SPRITE_SIZE*2
       self.py += amountY
       for row in range(0,len(self.tiles)):
           for col in range(0,len(self.tiles[row])):
               self.tiles[row][col].changePosition(self.px+col*SPRITE_SIZE,self.py+row*SPRITE_SIZE)
       self.px += SPRITE_SIZE*2
