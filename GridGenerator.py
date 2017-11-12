
from Renderer import screen,size,clock,SPRITE_SIZE,GRID_SIZE,spriteList,gridList
from Sprite import Sprite
import Main

def generateNewGrid(left, top):
    fittingGrid = gridList[0]
    Main.board.addToScreen(fittingGrid)
    return fittingGrid