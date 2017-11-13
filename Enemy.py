#Enemy are baddies that do bad stuff beccause they're mean.
from Movable import Movable
import Tile
from Renderer import spriteList,enemyList
enemyArchetypes = []

class Enemy(Movable):
  	#takes in the arguments that create movable, as well as an id that
  	#will define the enemy. (enemy's other stats loaded in from text file)
  	#this should NOT be called on the outside
	def __init__(self,sprites,locationX,locationY,id,behavior,initial):
		Movable.__init__(self,sprites,locationX,locationY)
		self.id = id
		self.behavior = behavior
		self.initial = initial
	#this should be called to create a new enemy
	def create(id,x,y):
		global spriteList
		archetype = enemyArchetypes[id]
		newEnemy = Enemy.clone(archetype)
		spriteList.append(newEnemy)
		enemyList.append(newEnemy)
		newEnemy.changePosition(x,y)
		newEnemy.initial(newEnemy)
		return newEnemy

	def clone(self):
		toReturn = Movable.clone(self)
		toReturn.id = self.id
		toReturn.behavior = self.behavior
		toReturn.initial = self.initial
		return toReturn

	def update(self):
		self.behavior(self)
		#(Tile.Screen.queryScreen(self.px,self.py)).changeState("teststate")

def noBehavior(this):
	pass

def id0behavior(this):
	#head right if possible
	top = Tile.Screen.queryScreen(this.px,this.py-16)
	bottom = Tile.Screen.queryScreen(this.px,this.py+16)
	left = Tile.Screen.queryScreen(this.px-16,this.py)
	right = Tile.Screen.queryScreen(this.px+16,this.py)
	if (right is not None and Tile.Tile.isNice(right)):
		Movable.rawmove(this,0,0)

def id0initial(this):
	#here, our goal is to find the closest 'wall' and then
	#create a path that 'circles' it.  Then id0behavior will
	#just have the enemy follow that path.
	condition = lambda tile: tile is not None and not tile.passable
	tilefound = (Tile.Screen.findClosest(this.px,this.py,condition))
	if tilefound is not None:
		tilefound.changeState("debug")
	pass

def initializeEnemies():
	global enemyArchetypes
	wizarddict = {"lookingleft":["SRPG_Wizard"]}
	enemyArchetypes.append(Enemy(wizarddict,0,0,0,id0behavior,id0initial))
	enemyArchetypes.append(Enemy(wizarddict,0,0,1,noBehavior,noBehavior))
