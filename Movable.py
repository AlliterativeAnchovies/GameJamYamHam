from Sprite import Sprite

class Movable(Sprite):
  def __init__(self,sprites,locationX,locationY):
    Sprite.__init__(self,sprites,locationX,locationY)
    self.vx = 0
    self.vy = 0
    self.pvx = 0 #previous velocity, stored to help out its snake followers
    self.pvy = 0
    self.follower = None #a Movable is a Snake.  This links to its follower

  def clone(self):
      toReturn = Sprite.clone(self)
      toReturn.vx = 0
      toReturn.vy = 0
      toReturn.pvx = 0
      toReturn.pvy = 0
      return toReturn

  def addFollower(self,follower):
    if self.follower is None:
      self.follower = follower
    else:
      self.follower.addFollower(follower)

  def changeVelocity(self,x,y):
    self.pvx = self.vx
    self.pvy = self.vy
    self.vx = x
    self.vy = y

  def move(self):
    self.px += self.vx
    self.py += self.vy
    if (self.vx != self.pvx or self.vy != self.pvy):#calculate if follower should change velocity
      if self.follower is not None:                 #I doubt this works yet, but hopefully it does
        self.follower.changeVelocity(self.pvx,self.pvy)
      self.pvx = self.vx
      self.pvy = self.vy
    self.follower.move();

  def update():
      pass
