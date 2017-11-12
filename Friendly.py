#Friendlies are segments of the player's snake
from Movable import Movable
class Friendly(Movable):
  def __init__(self,sprites,locationX,locationY):
    Movable.__init__(self,sprites,locationX,locationY)
