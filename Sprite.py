#This File Contains The Sprite Class
from Renderer import screen,SPRITE_SIZE,allSprites
import pygame

class Sprite:
    def __init__(self,spriteNames,locationX,locationY):
        self.spriteDict = spriteNames
        for key in self.spriteDict:
            self.curSprite = key
            break
        self.px = locationX
        self.py = locationY
        self.spriteOn = 0
    def draw(self):
        screen.blit(allSprites[self.curSprite],(self.px, self.py))
    def changeSprite(self,newSprite):
        self.curSprite = newSprite
