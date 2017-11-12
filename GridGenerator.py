
from Renderer import screen,size,clock,SPRITE_SIZE,GRID_SIZE,spriteList,gridList
from Sprite import Sprite
from random import random

def generateNewGrid(board, left, top, x, y):
    global gridList
    # first we need to create the first column.

    fittingGrid = gridList[0]
    foundGrid = True
    while foundGrid:
        fittingGrid = gridList[int(random()*len(gridList))]
        foundGrid = gridsCanBeUpDown(top,fittingGrid) and gridsCanBeLeftRight(left,fittingGrid)
        break

    return board.addToScreen(fittingGrid,x,y)

def gridsCanBeLeftRight(a,b):
    if (a is None) or (b is None):
        return True
    thereIsAPath = False
    for x in range(0,GRID_SIZE):
        thereIsAPath = thereIsAPath or (a.tiles[x][GRID_SIZE-1].passable and b.tiles[x][0].passable)
    return thereIsAPath

def gridsCanBeUpDown(a,b):
    if (a is None) or (b is None):
        return True
    thereIsAPath = False
    for x in range(0,GRID_SIZE):
        thereIsAPath = thereIsAPath or (a.tiles[GRID_SIZE-1][x].passable and b.tiles[0][x].passable)
    return thereIsAPath

#counts passable tiles on leftmost part of grid
def tilesInLeft(griddy):
    toReturn = 0
    for x in griddy.tiles:
        #this loops through the rows
        if x[0].passable:
            toReturn+=1
    return toReturn


#counts passable tiles on rightmost part of grid
def tilesInRight(griddy):
    toReturn = 0
    for x in griddy.tiles:
        #this loops through the rows
        if x[len(x)-1].passable:
            toReturn+=1
    return toReturn

#counts passable tiles on topmost part of grid
def tilesInTop(griddy):
    toReturn = 0
    for x in griddy.tiles[0]:
        #this loops through the rows
        if x.passable:
            toReturn+=1
    return toReturn

#counts passable tiles on bottommost part of grid
def tilesInBottom(griddy):
    toReturn = 0
    for x in griddy.tiles[len(griddy.tiles)-1]:
        #this loops through the rows
        if x.passable:
            toReturn+=1
    return toReturn
