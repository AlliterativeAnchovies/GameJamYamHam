#Enemy are baddies that do bad stuff beccause they're mean.
from Movable import Movable
import Tile
from Renderer import spriteList,enemyList,enemiesToInit,enemyNames,enemyLastNames
import math
from random import choice
import DebugDefines
enemyArchetypes = []
FORWARD = 1
BACKWARD = -1

class Enemy(Movable):
  	#takes in the arguments that create movable, as well as an id that
  	#will define the enemy. (enemy's other stats loaded in from text file)
  	#this should NOT be called on the outside
	def __init__(self,sprites,locationX,locationY,id,behavior,initial):
		Movable.__init__(self,sprites,locationX,locationY)
		self.id = id
		self.behavior = behavior
		self.initial = initial
		self.path = []
		self.pathindex = 0
		self.direction = FORWARD
		self.inited = False
		self.removeflag = False
		self.name = "Archetype"
		self.lastname = "Johnson"
	#this should be called to create a new enemy
	def create(id):
		global spriteList
		archetype = enemyArchetypes[id]
		newEnemy = Enemy.clone(archetype)
		spriteList.append(newEnemy)
		enemyList.append(newEnemy)
		enemiesToInit.append(newEnemy)
		if DebugDefines.PRINT_ENEMY_BIRTHS:
			print(Enemy.getName(newEnemy) + " was born.")
		return newEnemy

	def getName(self):
		return self.name + " " + self.lastname

	def clone(self):
		toReturn = Movable.clone(self)
		toReturn.id = self.id
		toReturn.behavior = self.behavior
		toReturn.initial = self.initial
		toReturn.path = []
		toReturn.pathindex = 0
		toReturn.direction = FORWARD
		toReturn.inited = False
		toReturn.name = choice(enemyNames)
		toReturn.lastname = choice(enemyLastNames)
		toReturn.removeflag = False
		return toReturn

	def getPath(self):
		return self.path

	def getPathIndex(self):
		return self.pathindex

	def getDirection(self):
		return self.direction

	#performs its initial function
	def finish_init(self):
		self.inited = True
		self.initial(self)

	def isinit(self):
		return self.inited

	def needsremoving(self):
		return self.removeflag

	def on_survived_board(self):
		self.removeflag = True
		if DebugDefines.PRINT_ENEMY_SURVIVALS:
			print(Enemy.getName(self) + " survived a day at work.")

	def update(self):
		Movable.update(self)
		self.behavior(self)
		#Movable.move(self)
		#(Tile.Screen.queryScreen(self.px,self.py)).changeState("teststate")

def noBehavior(this):
	pass

def id0behavior(this):
	if len(this.path)==0:
		return
	relevantpath = this.path[0][1]
	if (len(relevantpath)>0):
		tileon = Tile.Screen.queryScreen(int(this.px),int(this.py))
		toheadto = relevantpath[this.pathindex]
		if tileon==toheadto:#arrived at destination, choose new destination
			if this.path[0][0]:#repeat path
				this.pathindex+=this.direction
				if this.pathindex>=len(relevantpath) or this.pathindex<0:#change direction
					#check if should loop path forward
					if this.direction==FORWARD and Tile.Tile.adjacent(relevantpath[0],tileon):
						this.pathindex = 0
					#check if should loop path backward
					elif this.direction==BACKWARD and Tile.Tile.adjacent(relevantpath[-1],tileon):
						this.pathindex = len(this.path)-1
					#cant loop, turn around
					else:
						this.direction*=-1
						this.pathindex+=2*this.direction
				toheadto = relevantpath[this.pathindex]
			else:#move on to the next path
				this.path.pop(0)
				if (len(this.path)==0):
					return
				else:
					toheadto = this.path[0][1][0]
		deltx = toheadto.px-this.px
		delty = toheadto.py-this.py
		if abs(deltx)>abs(delty) and deltx is not 0:
			deltx = deltx/abs(deltx)
			delty = 0
		elif delty is not 0:
			delty = delty/abs(delty)
			deltx = 0
		else:
			deltx = 0
			delty = 0
		Movable.movesnap(this,deltx,delty)


def id0initial(this):
	#here, our goal is to find the closest 'wall' and then
	#create a path that 'circles' it.  Then id0behavior will
	#just have the enemy follow that path.
	condition = lambda tile: (tile is not None) and (not tile.passable)
	condition2 = lambda tile: (tile is not None) and (not Tile.Tile.isNice(tile))
	closestwall = (Tile.Screen.findClosest(this.px,this.py,condition))
	if closestwall is not None:
		#closestwall.changeState("debug")
		walltohug = Tile.Screen.fillFind_loose(closestwall.px,closestwall.py,condition2)
		walltohugadjacencies = []
		#we have found the wall, now let's find the walkable path adjacent to it
		for a in walltohug:
			#a.changeState("debug")
			top = Tile.Screen.queryScreen(a.px,a.py-16)
			bottom = Tile.Screen.queryScreen(a.px,a.py+16)
			left = Tile.Screen.queryScreen(a.px-16,a.py)
			right = Tile.Screen.queryScreen(a.px+16,a.py)
			c1 = Tile.Screen.queryScreen(a.px-16,a.py-16)
			c2 = Tile.Screen.queryScreen(a.px-16,a.py+16)
			c3 = Tile.Screen.queryScreen(a.px+16,a.py+16)
			c4 = Tile.Screen.queryScreen(a.px+16,a.py-16)
			if (top is not None and Tile.Tile.isNice(top)):
				walltohugadjacencies.append(top)
			if (bottom is not None and Tile.Tile.isNice(bottom)):
				walltohugadjacencies.append(bottom)
			if (left is not None and Tile.Tile.isNice(left)):
				walltohugadjacencies.append(left)
			if (right is not None and Tile.Tile.isNice(right)):
				walltohugadjacencies.append(right)
			if (c1 is not None and Tile.Tile.isNice(c1)):
				walltohugadjacencies.append(c1)
			if (c2 is not None and Tile.Tile.isNice(c2)):
				walltohugadjacencies.append(c2)
			if (c3 is not None and Tile.Tile.isNice(c3)):
				walltohugadjacencies.append(c3)
			if (c4 is not None and Tile.Tile.isNice(c4)):
				walltohugadjacencies.append(c4)
		walltohugadjacencies = list(set(walltohugadjacencies))#remove duplicates
		#for b in walltohugadjacencies:
			#b.changeState("debug")
		closestadjacent = walltohugadjacencies[0]#later on we'll add a calculation here
		lastadjacent = closestadjacent
		patharoundwall = []
		while True:
			isvalid = lambda tile: (Tile.Tile.adjacent(tile,lastadjacent) and not (tile in patharoundwall))
			possibilities = [x for x in walltohugadjacencies if isvalid(x)]
			if len(possibilities)==0:
				break
			patharoundwall.append(possibilities[0])
			lastadjacent = possibilities[0]
		if DebugDefines.SHOW_ENEMY_PATHS:
			for c in patharoundwall:
				c.changeState("debug")
		this.path = [[False,[closestwall]],[True,patharoundwall]]
		this.pathindex = 0
		this.direction = FORWARD


def initializeEnemies():
	global enemyArchetypes
	wizarddict = {"lookingleft":["SRPG_Wizard"]}
	enemyArchetypes.append(Enemy(wizarddict,0,0,0,id0behavior,id0initial))
	enemyArchetypes.append(Enemy(wizarddict,0,0,1,noBehavior,noBehavior))
