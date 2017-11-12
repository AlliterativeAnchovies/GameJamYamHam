
from Renderer import screen,size,clock,SPRITE_SIZE,GRID_SIZE,spriteList,gridList,board
from Sprite import Sprite
from random import random

def generateNewGrid(left, top, x, y):
    global board, gridList
    # first we need to create the first column.
    fittingGrid = gridList[0]
    while foundGrid:
        fittingGrid = gridList[random()*len(gridList)]
        foundGrid = gridsCanBeUpDown(top,fittingGrid) and gridsCanBeLeftRight(left,fittingGrid)
    board.addToScreen(fittingGrid,x,y)
    return fittingGrid

def gridsCanBeLeftRight(a,b):
    thereIsAPath = False
    for x in range(0,GRID_SIZE):
        thereIsAPath = thereIsAPath or a[x][GRID_SIZE-1].passable and b[x][0].passable
    return thereIsAPath

def gridsCanBeUpDown(a,b):
    thereIsAPath = False
    for x in range(0,GRID_SIZE):
        thereIsAPath = thereIsAPath or a[GRID_SIZE-1][x].passable and b[0][x].passable
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
