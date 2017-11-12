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
screen = pygame.display.set_mode(size,pygame.SRCALPHA, 32)
blitto = pygame.Surface(size, pygame.SRCALPHA, 32)
blitto.convert_alpha()
clock = pygame.time.Clock()
allSprites = {}
spriteList = []
preGridList = []
gridList = []
tick = [0]
enemyList = []

def loadSprites():
    getfiles = os.listdir('./resources/images')
    bmpfiles = [x for x in getfiles if x[len(x)-1]=='p']
    #assuming there is no file that ends in p in resources/images
    #print(bmpfiles)#to check what got printed
    for bmp in bmpfiles:
        #allSprites[bmp] = (pygame.image.load('resources/images/'+bmp)).convert_alpha()
        literallystupid = (pygame.image.load('resources/images/'+bmp)).convert_alpha()
        shutup = pygame.Surface((SPRITE_SIZE,SPRITE_SIZE), pygame.SRCALPHA, 32)
        shutup.blit(literallystupid,(0, 0))
        ihatemylife = pygame.PixelArray(literallystupid)
        for pythonsucks in range(SPRITE_SIZE):
            for screwpython in range(SPRITE_SIZE):
                if ihatemylife[pythonsucks][screwpython]<=0x00ffffff:
                    dontjudgeme = shutup.get_at((pythonsucks,screwpython))
                    shutup.set_at((pythonsucks,screwpython),(dontjudgeme.r,dontjudgeme.g,dontjudgeme.b,dontjudgeme.a))
        allSprites[bmp] = shutup
        """#This code proves that it is reading in pixels with alpha values
        pix = pygame.PixelArray(allSprites[bmp])
        for x in pix:
            for y in x:
                if y>0x00ffffff:#contains alpha
                    print("Alpha found!")
        """


#Python is really annoying in how it handles importing global variables.
#Its impossible as far as I can tell to have all the variables initialized in
#an init(), which really grinds my gears.
