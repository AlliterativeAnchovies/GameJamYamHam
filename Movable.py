from Sprite import Sprite
from Renderer import SPRITE_SIZE

class Movable(Sprite):
	def __init__(self,sprites,locationX,locationY):
		Sprite.__init__(self,sprites,locationX,locationY)
		#self.vx = 0
		#self.vy = 0
		#self.pvx = 0 #previous velocity, stored to help out its snake followers
		#self.pvy = 0
		self.movingto = None
		self.backlog = None #If recieves a move command while still moving, goes here
		self.follower = None #a Movable is a Snake.  This links to its follower
		self.smoothtransitioncounter = 0#from 0-1 representing sprite inbetween thingies

	def clone(self):
		toReturn = Sprite.clone(self)
		"""
		toReturn.vx = 0
		toReturn.vy = 0
		toReturn.pvx = 0
		toReturn.pvy = 0
		"""
		toReturn.movingto = None
		toReturn.backlog = None
		toReturn.smoothtransitioncounter = 0
		toReturn.follower = None
		return toReturn

	def addFollower(self,follower):
		if self.follower is None:
			self.follower = follower
		else:
			self.follower.addFollower(follower)

	"""
	def changeVelocity(self,x,y):
		self.pvx = self.vx
		self.pvy = self.vy
		self.vx = x
		self.vy = y
	"""

	def rawmove(self,x,y):
		self.px+=x
		self.py+=y


	def movesnap(self,x,y):
		import Tile
		if ((x==y or x==-y)and x is not 0):
			print("Error: Moving Diagonally Not Allowed")
		if (not (x==0 or x==1 or x==-1)) or (not (y==0 or y==1 or y==-1)):
			print("Error: May not move more than 1 space at a time")
		else:
			if self.movingto is not None:
				self.backlog = Tile.Screen.queryScreen(int(self.px+x*SPRITE_SIZE),int(self.py+y*SPRITE_SIZE))
			else:
				self.movingto = Tile.Screen.queryScreen(int(self.px+x*SPRITE_SIZE),int(self.py+y*SPRITE_SIZE))

	def draw(self):
		if self.movingto is not None:
			offx = int((self.movingto.px-self.px)*self.smoothtransitioncounter)
			offy = int((self.movingto.py-self.py)*self.smoothtransitioncounter)
			Sprite.draw_with_offset(self,offx,offy)
		else:
			Sprite.draw(self)

	"""
	def move(self):
		self.px += self.vx
		self.py += self.vy
		if (self.vx != self.pvx or self.vy != self.pvy):#calculate if follower should change velocity
			if self.follower is not None:				 #I doubt this works yet, but hopefully it does
				self.follower.changeVelocity(self.pvx,self.pvy)
			self.pvx = self.vx
			self.pvy = self.vy
		if self.follower is not None:
			self.follower.move();
	"""

	def update(self):
		if (self.movingto is not None):
			self.smoothtransitioncounter+=0.1
			if (self.smoothtransitioncounter>=1):
				self.smoothtransitioncounter=0
				self.px = self.movingto.px
				self.py = self.movingto.py
				self.movingto=self.backlog
				self.backlog=None
