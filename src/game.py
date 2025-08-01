import pygame
from const import *
class Game:
    def __init__(self):
        pass
    def show_bg(self, surface):
        for row in range(rows):
            for col in range(cols):
                if(row + col) % 2 == 0 :
                    color = (234,235,200) # green
                else :
                    color = (119,154,88) # dark green
                rect = (col * SqSize,row * SqSize,SqSize,SqSize)
                pygame.draw.rect(surface,color,rect)    