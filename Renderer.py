import pygame,os
#set position of screen
screenposx = 0
screenposy = 0
os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (screenposx,screenposy)
os.environ['SDL_VIDEO_CENTERED'] = '0'
#create screen
SPRITE_SIZE = 16
GRID_SIZE = 8
pygame.init()
screenwidth, screenheight = pygame.display.Info().current_w, pygame.display.Info().current_h
size = [screenwidth, SPRITE_SIZE*GRID_SIZE*6]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
allSprites = {"test":pygame.image.load('resources/images/Test.bmp').convert()}

#Python is really annoying in how it handles importing global variables.
#Its impossible as far as I can tell to have all the variables initialized in
#an init(), which really grinds my gears.
