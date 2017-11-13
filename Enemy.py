#Enemy are baddies that do bad stuff beccause they're mean.
from Movable import Movable
import Tile
from Renderer import spriteList,enemyList,enemiesToInit
import math
enemyArchetypes = []
FORWARD = True
BACKWARD = False

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
	#this should be called to create a new enemy
	def create(id):
		global spriteList
		archetype = enemyArchetypes[id]
		newEnemy = Enemy.clone(archetype)
		spriteList.append(newEnemy)
		enemyList.append(newEnemy)
		enemiesToInit.append(newEnemy)
		return newEnemy

	def clone(self):
		toReturn = Movable.clone(self)
		toReturn.id = self.id
		toReturn.behavior = self.behavior
		toReturn.initial = self.initial
		toReturn.path = []
		toReturn.pathindex = 0
		toReturn.direction = FORWARD
		toReturn.inited = False
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

	def update(self):
		self.behavior(self)
		#(Tile.Screen.queryScreen(self.px,self.py)).changeState("teststate")

def noBehavior(this):
	pass

def id0behavior(this):
	"""
	#head right if possible
	top = Tile.Screen.queryScreen(this.px,this.py-16)
	bottom = Tile.Screen.queryScreen(this.px,this.py+16)
	left = Tile.Screen.queryScreen(this.px-16,this.py)
	right = Tile.Screen.queryScreen(this.px+16,this.py)
	if (right is not None and Tile.Tile.isNice(right)):
		Movable.rawmove(this,0,0)
	"""
	if (len(Enemy.getPath(this))>0):
		toheadto = Enemy.getPath(this)[Enemy.getPathIndex(this)]
		deltx = toheadto.px-this.px
		delty = toheadto.py-this.py
		mag = math.sqrt(deltx*deltx+delty*delty)
		if mag>0:
			deltx/=mag
			delty/=mag
			Movable.changeVelocity(this,deltx,delty)


def id0initial(this):
	#here, our goal is to find the closest 'wall' and then
	#create a path that 'circles' it.  Then id0behavior will
	#just have the enemy follow that path.
	condition = lambda tile: (tile is not None) and (not tile.passable)
	condition2 = lambda tile: (tile is not None) and (not Tile.Tile.isNice(tile))
	closestwall = (Tile.Screen.findClosest(this.px,this.py,condition))
	if closestwall is not None:
		#closestwall.changeState("debug")
		walltohug = Tile.Screen.fillFind(closestwall.px,closestwall.py,condition2)
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
		for b in walltohugadjacencies:
			#b.changeState("debug")
			pass
		closestadjacent = walltohugadjacencies[0]#later on we'll add a calculation here
		lastadjacent = closestadjacent
		patharoundwall = []
		while True:
			isvalid = lambda tile: (Tile.Tile.loosely_adjacent(tile,lastadjacent) and not (tile in patharoundwall))
			possibilities = [x for x in walltohugadjacencies if isvalid(x)]
			if len(possibilities)==0:
				break
			patharoundwall.append(possibilities[0])
			lastadjacent = possibilities[0]
		for c in patharoundwall:
			c.changeState("debug")
			pass
		this.path = patharoundwall
		this.pathindex = 0
		this.direction = FORWARD


def initializeEnemies():
	global enemyArchetypes
	wizarddict = {"lookingleft":["SRPG_Wizard"]}
	enemyArchetypes.append(Enemy(wizarddict,0,0,0,id0behavior,id0initial))
	enemyArchetypes.append(Enemy(wizarddict,0,0,1,noBehavior,noBehavior))
