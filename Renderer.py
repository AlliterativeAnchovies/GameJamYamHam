import pygame

pygame.init()
SPRITE_SIZE = 16
size = [640, 480]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('My Game')
clock = pygame.time.Clock()
allSprites = {"test":pygame.image.load('resources/images/Base Tile 1.bmp')}
