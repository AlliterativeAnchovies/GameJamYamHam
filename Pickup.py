from Sprite import Sprite

class Pickup(Sprite):
  #takes all the information as a sprite, and also a function to perform
  #when passed over
  def __init__(self,sprites,locationX,locationY,on_collision):
    Sprite.__init__(self,sprites,locationX,locationY)
    self.on_collision = on_collision
   
  def collide(self,player):
    self.on_collision(player)
