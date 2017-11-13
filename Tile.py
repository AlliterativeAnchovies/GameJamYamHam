from Sprite import Sprite
from Renderer import SPRITE_SIZE,GRID_SIZE,SCREEN_WIDTH,gridList,spriteList,enemyList,tileList
from GridGenerator import generateNewGrid
import pygame,os
from Enemy import Enemy
board = None
GRID_PIXEL_SIZE = (GRID_SIZE*SPRITE_SIZE)
EXCESS_GRIDS = 5

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

	#if 2 tiles have touching edges
	def adjacent(a,b):
		top = Screen.queryScreen(a.px,a.py-16)
		bottom = Screen.queryScreen(a.px,a.py+16)
		left = Screen.queryScreen(a.px-16,a.py)
		right = Screen.queryScreen(a.px+16,a.py)
		return b is top or b is bottom or b is left or b is right

	#if adjacent by edges or vertices
	def loosely_adjacent(a,b):
		top = Screen.queryScreen(a.px,a.py-16)
		bottom = Screen.queryScreen(a.px,a.py+16)
		left = Screen.queryScreen(a.px-16,a.py)
		right = Screen.queryScreen(a.px+16,a.py)
		c1 = Screen.queryScreen(a.px-16,a.py-16)
		c2 = Screen.queryScreen(a.px-16,a.py+16)
		c3 = Screen.queryScreen(a.px+16,a.py+16)
		c4 = Screen.queryScreen(a.px+16,a.py-16)
		return b is top or b is bottom or b is left or b is right or b is c1 or b is c2 or b is c3 or b is c4

	def clone(self):

		toReturn = Sprite.clone(self)
		toReturn.passable = self.passable
		toReturn.damage = self.damage
		toReturn.pickup = self.pickup.clone() if self.pickup else None
		toReturn.moveable = self.moveable.clone() if self.moveable else None
		return toReturn

	#if this is a 'smart' move, because it is allowed and won't hurt you
	#useful for AI because then you don't have to keep reusing the same line
	#over and over again
	def isNice(self):
		return self.passable and (self.damage<=0)

class Grid:
	#this represents our 4x4 chunks of tiles
	#Takes in 3 arguments, a 4x4 2d list of tiles
	#and a position (x,y)
	def __init__(self,tileList,positionX,positionY):
		self.tiles = tileList
		self.px = positionX
		self.py = positionY
		for row in range(len(self.tiles)):
			for col in range(len(self.tiles[row])):
				self.tiles[row][col].changePosition(self.px+col*SPRITE_SIZE,self.py+row*SPRITE_SIZE)
		self.px = positionX


	#moves a grid by its two agruments, (amountX,amountY)
	def move(self,amountX,amountY):
	   self.px += amountX
	   self.py += amountY
	   for row in range(len(self.tiles)):
		   for col in range(len(self.tiles[row])):
			   self.tiles[row][col].changePosition(self.px+col*SPRITE_SIZE,self.py+row*SPRITE_SIZE)

class Screen:
	def __init__(self):
		self.px = 0
		self.py = 0

	#fillfind, but diagonal connections are included too
	def fillFind_loose(x,y,condition):
		return board.fillFindInternal_loose(x,y,condition,[board.querySpecificScreen(x,y)])
	def fillFindInternal_loose(self,x,y,condition,searched):
		#you should not call this method - use fillFind instead
		top = self.querySpecificScreen(x,y-16)
		bottom = self.querySpecificScreen(x,y+16)
		left = self.querySpecificScreen(x-16,y)
		right = self.querySpecificScreen(x+16,y)
		c1 = self.querySpecificScreen(x-16,y-16)
		c2 = self.querySpecificScreen(x-16,y+16)
		c3 = self.querySpecificScreen(x+16,y+16)
		c4 = self.querySpecificScreen(x+16,y-16)
		if not (top is None or top in searched) and condition(top):
			searched.append(top)
			searched = self.fillFindInternal_loose(x,y-16,condition,searched)
		if not (bottom is None or bottom in searched) and condition(bottom):
			searched.append(bottom)
			searched = self.fillFindInternal_loose(x,y+16,condition,searched)
		if not (left is None or left in searched) and condition(left):
			searched.append(left)
			searched = self.fillFindInternal_loose(x-16,y,condition,searched)
		if not (right is None or right in searched) and condition(right):
			searched.append(right)
			searched = self.fillFindInternal_loose(x+16,y,condition,searched)
		if not (c1 is None or c1 in searched) and condition(c1):
			searched.append(c1)
			searched = self.fillFindInternal_loose(x-16,y-16,condition,searched)
		if not (c2 is None or c2 in searched) and condition(c2):
			searched.append(c2)
			searched = self.fillFindInternal_loose(x-16,y+16,condition,searched)
		if not (c3 is None or c3 in searched) and condition(c3):
			searched.append(c3)
			searched = self.fillFindInternal_loose(x+16,y+16,condition,searched)
		if not (c4 is None or c4 in searched) and condition(c4):
			searched.append(c4)
			searched = self.fillFindInternal_loose(x+16,y-16,condition,searched)
		return searched

	#returns a list of all tiles touching the tile at (x,y), [including
	#the tile at x,y], that satisfy condition
	def fillFind(x,y,condition):
		return board.fillFindInternal(x,y,condition,[board.querySpecificScreen(x,y)])
	def fillFindInternal(self,x,y,condition,searched):
		#you should not call this method - use fillFind instead
		top = self.querySpecificScreen(x,y-16)
		bottom = self.querySpecificScreen(x,y+16)
		left = self.querySpecificScreen(x-16,y)
		right = self.querySpecificScreen(x+16,y)
		if not (top is None or top in searched) and condition(top):
			searched.append(top)
			searched = self.fillFindInternal(x,y-16,condition,searched)
		if not (bottom is None or bottom in searched) and condition(bottom):
			searched.append(bottom)
			searched = self.fillFindInternal(x,y+16,condition,searched)
		if not (left is None or left in searched) and condition(left):
			searched.append(left)
			searched = self.fillFindInternal(x-16,y,condition,searched)
		if not (right is None or right in searched) and condition(right):
			searched.append(right)
			searched = self.fillFindInternal(x+16,y,condition,searched)
		return searched
	#finds closest tile on board that satisfies a condition
	#condition(None)=True cause this to return None if it reaches
	#the end of the screen.  It will also return None if no such
	#tile is found
	def findClosest(x,y,condition,startingDirection=None,includestart=None):
		return board.findClosestInternal(x,y,condition,startingDirection,includestart)
	def findClosestInternal(self,x,y,condition,startingDirection,includestart):
		UP = 0
		LEFT = 1
		DOWN = 2
		RIGHT = 3
		if includestart is None:
			includestart = False
		if startingDirection is None:
			startingDirection = UP
		startingTile = self.querySpecificScreen(x,y)
		if (includestart and condition(startingTile)):
			return startingTile
		tileschecked = 0
		tilestocheck = GRID_SIZE*len(self.gridList)*len(self.gridList[0])
		directionLooking = startingDirection
		spiralLength = 1
		curSpiralsSearched = 0
		#look in a spiral
		while tileschecked<tilestocheck:
			if directionLooking is UP:
				y-=SPRITE_SIZE
			elif directionLooking is DOWN:
				y+=SPRITE_SIZE
			elif directionLooking is LEFT:
				x-=SPRITE_SIZE
			elif directionLooking is RIGHT:
				x+=SPRITE_SIZE
			tileSearching = self.querySpecificScreen(x,y)
			if condition(tileSearching):
				return tileSearching
			tileschecked+=1
			curSpiralsSearched+=1
			if curSpiralsSearched==spiralLength:
				curSpiralsSearched = 0
				#spiral grows bigger every other turn
				if (directionLooking is (startingDirection+1)%4) or (directionLooking is (startingDirection+3)%4):
					spiralLength+=1
				directionLooking = (directionLooking+1)%4
		return None


	#finds the tile at position x,y on board
	def queryScreen(x,y):
		return board.querySpecificScreen(x,y)

	#finds the tile at position x,y on any screen
	def querySpecificScreen(self, x, y):
		#get x coord of first tile:
		firsttilex = self.gridList[0][0].px
		#shift incoming position to account for that
		x-=firsttilex
		#find what grid its on
		gridx = x//(GRID_PIXEL_SIZE)
		gridy = y//(GRID_PIXEL_SIZE)
		if (gridy not in range(len(self.gridList))) or (gridx not in range(len(self.gridList[gridy]))):
			return None
		relevantGrid = self.gridList[gridy][gridx]
		#shift x,y to be relative to this grid
		x = x%GRID_PIXEL_SIZE
		y = y%GRID_PIXEL_SIZE
		#and now make x,y represent tiles not pixels
		x = x//SPRITE_SIZE
		y = y//SPRITE_SIZE
		#get relevant tile
		if y not in range(len(relevantGrid.tiles)) or x not in range(len(relevantGrid.tiles[y])):
			return None
		relevantTile = relevantGrid.tiles[y][x]
		return relevantTile

	def addToScreen(self, grid, x, y):
		global spriteList,tileList
		tilesToPut = []
		for row in range(len(grid.tiles)):
			tilesToPut.append([])
			for col in range(len(grid.tiles[row])):
				newTile = grid.tiles[row][col].clone()
				spriteList.append(newTile)
				tilesToPut[row].append(newTile)
				tileList.append(newTile)
		return Grid(tilesToPut, x, y)

	def generateInitialScreen(self):
		gridColsThatFitOnScreen = (SCREEN_WIDTH//GRID_PIXEL_SIZE)+1
		self.gridList = []
		for row in range(6): # Should be changed to constant in renderer
			self.gridList.append([])
			for col in range(gridColsThatFitOnScreen+EXCESS_GRIDS):
				leftGrid = self.gridList[row][-1] if len(self.gridList[row]) > 0 else None
				topGrid = self.gridList[row-1][-1] if row-1 >= 0 else None
				self.gridList[row].append(generateNewGrid(self, leftGrid, topGrid, col*GRID_PIXEL_SIZE, row*GRID_PIXEL_SIZE))


	def move(self, amountX, amountY):
		self.px += amountX
		self.py += amountY

		for en in enemyList:
			Enemy.rawmove(en,amountX,amountY)

		rows = len(self.gridList)

		# When the left-most-grid falls off the screen
		if self.px % GRID_PIXEL_SIZE == 0:
			for row in range(rows):
				del self.gridList[row][0]

		# When the right-most-grid needs to be generated
		if (self.px + SCREEN_WIDTH) % GRID_PIXEL_SIZE == 0:
			print("Whoop")
			for row in range(rows):
				leftGrid = self.gridList[row][-1]
				upGrid = self.gridList[row-1][-1] if rows-1 >= 0 else None
				self.gridList[row].append(generateNewGrid(self,leftGrid, upGrid,((SCREEN_WIDTH//GRID_PIXEL_SIZE)+1)*GRID_PIXEL_SIZE-2*SPRITE_SIZE+EXCESS_GRIDS*GRID_PIXEL_SIZE,row*GRID_PIXEL_SIZE))

		for row in range(rows):
			for col in range(len(self.gridList[row])):
				self.gridList[row][col].move(amountX, amountY)

board = Screen()

def loadGrids():
	global board

	getfiles = os.listdir('./resources/grids')
	bmpfiles = [x for x in getfiles if x[-1]=='p']
	bmpimages = []
	for image in bmpfiles:
		relevantImage = pygame.image.load('resources/grids/'+image)
		relevantPixels = pygame.PixelArray(relevantImage)
		tileList = []
		for i in range(GRID_SIZE):
			tileRow = []
			for j in range(GRID_SIZE):
				pixelcolor = (relevantPixels[i][j]<<8)>>8 #shifting so that we get rid of alpha values
				if (pixelcolor==0x00ffffff):
					dummyspritedict = {"defaultstate":["Base Tile 1"],"debug":["FireTile_1"]}
					tiletoappend = Tile(dummyspritedict,0,0,True,0)
					tileRow.append(tiletoappend)
				elif (pixelcolor==0x00000000):
					dummyspritedict = {"defaultstate":["Base Wall 1"],"debug":["Fire1"]}
					tiletoappend = Tile(dummyspritedict,0,0,False,0)
					tileRow.append(tiletoappend)
				elif (pixelcolor==0x00ff0000):
					dummyspritedict = {"defaultstate":["FireTile_1","FireTile_2","FireTile_3"],"debug":["Corner"]}
					tiletoappend = Tile(dummyspritedict,0,0,True,1)
					tiletoappend.setTickrate(10)
					tileRow.append(tiletoappend)
				else:
					print("I hate my life")
			tileList.append(tileRow)
		gridList.append(Grid(tileList,0,0))

	board.generateInitialScreen()
