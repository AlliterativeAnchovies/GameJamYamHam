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
def loadSprites():
    getfiles = os.listdir('./resources/images')
    bmpfiles = [x for x in getfiles if x[len(x)-1]=='p']
    #assuming there is no file that ends in p in resources/images
    #print(bmpfiles)#to check what got printed
    for bmp in bmpfiles:
        allSprites[bmp] = 'resources/images/'+bmp+'/.bmp'
def loadGrids():
    from Tile import Grid,Tile
    getfiles = os.listdir('./resources/grids')
    bmpfiles = [x for x in getfiles if x[len(x)-1]=='p']
    bmpimages = []
    for image in bmpfiles:
        relevantImage = pygame.image.load('resources/grids/'+image)
        relevantPixels = pygame.PixelArray(relevantImage)
        tileList = []
        for i in range(0,GRID_SIZE):
            tileRow = []
            for j in range(0,GRID_SIZE):
                pixelcolor = (relevantPixels[i][j]<<8)>>8 #shifting so that we get rid of alpha values
                if (pixelcolor==0x00ffffff):
                    dummyspritedict = {"defaultstate":["Base Tile 1"]}
                    tiletoappend = Tile(dummyspritedict,0,0,True,False)
                    tileRow.append(tiletoappend)
                elif (pixelcolor==0x00000000):
                    dummyspritedict = {"defaultstate":["Test"]}
                    tiletoappend = Tile(dummyspritedict,0,0,False,True)
                    tileRow.append(tiletoappend)
                else:
                    print("Error!  This is not a valid pixel color: ")
                    print(pixelcolor)
            tileList.append(tileRow)
        gridList.append(Grid(tileList,0,0))
loadSprites()
loadGrids()

#Python is really annoying in how it handles importing global variables.
#Its impossible as far as I can tell to have all the variables initialized in
#an init(), which really grinds my gears.
