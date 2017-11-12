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
	#blits to the screen the current sprite at its location
	def draw(self):
		#print(allSprites)
		#blitto.blit(allSprites[self.cursprite+'.bmp'],(self.px, self.py),pygame.rect.Rect((0,0,SPRITE_SIZE, SPRITE_SIZE)),pygame.BLEND_RGBA_MAX)#This gives trippy thingy
		#blitto.blit(allSprites[self.cursprite+'.bmp'],(self.px, self.py),pygame.rect.Rect((0,0,SPRITE_SIZE, SPRITE_SIZE)),pygame.BLEND_RGBA_ADD)#This gives fade-to-white
		screen.blit(allSprites[self.cursprite+'.bmp'],(self.px, self.py))
		if ((tick[0])%self.tickrate==0):#update animation
			self.updateFrame()
	#takes in one input, a string which is the name of the state we're changing it to
	def changeState(self,newState):
		self.curstate = self.sprites["newState"]
		self.cursprite = self.curstate[0]
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
