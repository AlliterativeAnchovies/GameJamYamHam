#Enemy are baddies that do bad stuff beccause they're mean.
from Movable import Movable
from Renderer import spriteList
enemyArchetypes = []

class Enemy(Movable):
  #takes in the arguments that create movable, as well as an id that
  #will define the enemy. (enemy's other stats loaded in from text file)
  #this should NOT be called on the outside
  def __init__(self,sprites,locationX,locationY,id,damage):
      Movable.__init__(self,sprites,locationX,locationY)
      self.id = id
      self.damage = damage
  #this should be called to create a new enemy
  def create(id):
      archetype = enemyArchetypes[id]
      newEnemy = Enemy(archetype.sprites,archetype.locationX,archetype.locationY,archetype.id,archetype.damage)
      spriteList.append(newEnemy)
      return newEnemy

  def clone(self):
      toReturn = Enemy.clone(self)
      toReturn.id = id
      toReturn.damage = damage

def initializeEnemies():
    global enemyArchetypes
    dummyspritedict = {"defaultstate":["test"]}
    enemyArchetypes.append(Enemy(dummyspritedict,0,0,0,0))
    enemyArchetypes.append(Enemy(dummyspritedict,0,0,1,0))
