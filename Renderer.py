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
SCREEN_WIDTH, RAW_SCREEN_HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
SCREEN_HEIGHT = SPRITE_SIZE*GRID_SIZE*6
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
allSprites = {"test":pygame.image.load('resources/images/Base Tile 1.bmp').convert()}
spriteList = []
preGridList = []
gridList = []
board = []

def loadSprites():
    getfiles = os.listdir('./resources/images')
    bmpfiles = [x for x in getfiles if x[len(x)-1]=='p']
    #assuming there is no file that ends in p in resources/images
    #print(bmpfiles)#to check what got printed
    for bmp in bmpfiles:
        allSprites[bmp] = 'resources/images/'+bmp+'/.bmp'
<<<<<<< HEAD
=======
def loadGrids():
    global board
    from Tile import Grid, Screen
>>>>>>> 4043a1640497390a19e55221a7317d9b1ae57654



#Python is really annoying in how it handles importing global variables.
#Its impossible as far as I can tell to have all the variables initialized in
#an init(), which really grinds my gears.
