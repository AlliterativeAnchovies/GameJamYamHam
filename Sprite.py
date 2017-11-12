#This File Contains The Sprite Class
from Renderer import screen,SPRITE_SIZE,allSprites
import pygame

class Sprite:
    #Takes in:
    #sprites: a dictionary of lists of names of sprites.
    #   dictionary indexed by state names, like 'looking left','throwing projectile'
    #   and contains lists that represent the frames of its animations in that state
    #locationX,Y: position of the sprite
    def __init__(self,sprites,locationX,locationY):
        self.sprites = sprites
        self.animationframe = 0
        for state in self.sprites:
            self.curstate = state
            self.cursprite = self.sprites[state][0]#default to first state, first frame
            break
        self.px = locationX
        self.py = locationY
    #blits to the screen the current sprite at its location
    def draw(self):
        screen.blit(allSprites[self.cursprite],(self.px, self.py))
    #takes in one input, a string, which points to its new sprite in spriteDict
    def changeState(self,newState):
        self.curstate = self.sprites["newState"]
        self.cursprite = self.curstate[0]
        self.animationframe = 0

    def updateFrame(self):
        self.animationframe = (self.animationframe+1)%(len(self.sprites[self.curstate]))
        self.cursprite = self.curstate[animationframe]
