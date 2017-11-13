#Enemy are baddies that do bad stuff beccause they're mean.
from Movable import Movable
import Tile
from Renderer import spriteList,enemyList
enemyArchetypes = []

class Enemy(Movable):
  	#takes in the arguments that create movable, as well as an id that
  	#will define the enemy. (enemy's other stats loaded in from text file)
  	#this should NOT be called on the outside
	def __init__(self,sprites,locationX,locationY,id,behavior):
		Movable.__init__(self,sprites,locationX,locationY)
		self.id = id
		self.behavior = behavior
	#this should be called to create a new enemy
	def create(id):
		global spriteList
		archetype = enemyArchetypes[id]
		newEnemy = Enemy.clone(archetype)
		spriteList.append(newEnemy)
		enemyList.append(newEnemy)
		return newEnemy

	def clone(self):
		toReturn = Movable.clone(self)
		toReturn.id = self.id
		toReturn.behavior = self.behavior
		return toReturn

	def update(self):
		self.behavior(self)
		#(Tile.Screen.queryScreen(self.px,self.py)).changeState("teststate")

def id0behavior(this):
	top = Tile.Screen.queryScreen(this.px,this.py-16)
	bottom = Tile.Screen.queryScreen(this.px,this.py+16)
	left = Tile.Screen.queryScreen(this.px-16,this.py)
	right = Tile.Screen.queryScreen(this.px+16,this.py)
	if (right is not None and Tile.Tile.isNice(right)):
		Movable.rawmove(this,1,0)

def initializeEnemies():
	global enemyArchetypes
	wizarddict = {"lookingleft":["SRPG_Wizard"]}
	enemyArchetypes.append(Enemy(wizarddict,0,0,0,id0behavior))
	enemyArchetypes.append(Enemy(wizarddict,0,0,1,None))
