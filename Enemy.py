#Enemy are baddies that do bad stuff beccause they're mean.

class Enemy(Movable):
  #takes in the arguments that create movable, as well as an id that
  #will define the enemy. (enemy's other stats loaded in from text file)
  def __init__(self,sprites,locationX,locationY,id):
    Movable.__init__(self,sprites,locationX,locationY)
    self.id = id
