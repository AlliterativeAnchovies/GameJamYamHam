#This File Contains The Sprite Class
from Renderer import screen
import pygame

class Sprite:
    def __init__(self,spriteNames,locationX,locationY):
        self.spriteDict = spriteNames
        self.px = locationX
        self.py = locationY
        self.spriteOn = 0
    def draw(self):
        pygame.draw.rect(screen, (0,0,0), (100, 100, 100, 100))
