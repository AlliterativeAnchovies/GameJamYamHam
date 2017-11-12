
from Renderer import screen,size,clock,SPRITE_SIZE,GRID_SIZE,spriteList,gridList,board
from Sprite import Sprite

def generateNewGrid(left, top):
    global board, gridList
    fittingGrid = gridList[0]
    board.addToScreen(fittingGrid)
    return fittingGrid
