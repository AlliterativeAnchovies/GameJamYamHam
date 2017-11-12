#Friendlies are segments of the player's snake
from Movable import Movable
from Renderer import spriteList
class Friendly(Movable):
  def __init__(self,sprites,locationX,locationY):
    Movable.__init__(self,sprites,locationX,locationY)
    spriteList.append(self)
