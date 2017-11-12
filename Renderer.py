import pygame
size = [640, 480]
SPRITE_SIZE = 16
pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
allSprites = {"test":pygame.image.load('resources/images/Test.bmp').convert()}

#Python is really annoying in how it handles importing global variables.
#Its impossible as far as I can tell to have all the variables initialized in
#an init(), which really grinds my gears.
