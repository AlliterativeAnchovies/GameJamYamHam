#This File Contains The Sprite Class
from Renderer import SPRITE_SIZE,allSprites,tick,screen
import pygame

class Sprite:
	#Takes in:
	#sprites: a dictionary of lists of names of sprites.
	#   dictipythonary indexed by state names, like 'looking left','throwing projectile'
	#   and contains lists that represent the frames of its animations in that state
	#locationX,Y: position of the sprite
	def __init__(self,sprites,locationX,locationY):
		self.sprites = sprites
		self.animationframe = 0
		self.tickrate = 1
		for state in self.sprites:
			self.curstate = state
			self.cursprite = self.sprites[state][0]#default to first state, first frame
			#print(self.cursprite)
			break
		self.px = locationX
		self.py = locationY

	#changes the tickrate
	def setTickrate(self,t):
		self.tickrate = t

	def draw_with_offset(self,x,y):
		screen.blit(allSprites[self.cursprite+'.bmp'],(self.px+x, self.py+y))
		if ((tick[0])%self.tickrate==0):#update animation
			self.updateFrame()
	#blits to the screen the current sprite at its location
	def draw(self):
		self.draw_with_offset(0,0)

	#takes in one input, a string which is the name of the state we're changing it to
	def changeState(self,newState):
		self.curstate = newState
		self.cursprite = self.sprites[self.curstate][0]
		self.animationframe = 0
	#increments the animation frame of the sprite
	def updateFrame(self):
		self.animationframe = (self.animationframe+1)%(len(self.sprites[self.curstate]))
		self.cursprite = self.sprites[self.curstate][self.animationframe]
	#teleports the sprite to a new position
	def changePosition(self,newPositionX,newPositionY):
		self.px = newPositionX
		self.py = newPositionY

	def clone(self):
		toReturn = Sprite(self.sprites,self.px, self.py)
		toReturn.setTickrate(self.tickrate)
		return toReturn
