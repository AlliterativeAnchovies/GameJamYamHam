#Enemy are baddies that do bad stuff beccause they're mean.
from Movable import Movable
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

def initializeEnemies():
	global enemyArchetypes
	wizarddict = {"lookingleft":["SRPG_Wizard"]}
	enemyArchetypes.append(Enemy(wizarddict,0,0,0,None))
	enemyArchetypes.append(Enemy(wizarddict,0,0,1,None))
