import pygame
from const import *
from board import Board
from dragger import Dragger
class Game:
    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()
    def show_bg(self, surface):
        for row in range(rows):
            for col in range(cols):
                if(row + col) % 2 == 0 :
                    color = (234,235,200) # green
                else :
                    color = (119,154,88) # dark green
                rect = (col * SqSize,row * SqSize,SqSize,SqSize)
                pygame.draw.rect(surface,color,rect)    
    def show_pieces(self,surface):
        for row in range(rows):
            for  col in range(cols):
                # piece ?
                if self.board.squares[row][col].has_piece() :
                    piece = self.board.squares[row][col].piece 
                    #all pieces except dragger piece
                    if piece != self.dragger.piece:
                     piece.set_texture(size = 80)
                     img = pygame.image.load(piece.texture)
                     img_center = col * SqSize + SqSize // 2, row * SqSize + SqSize // 2
                     piece.texture_rect = img.get_rect(center = img_center)
                     surface.blit(img,piece.texture_rect)
    def show_moves(self,surface):
        if self.dragger.dragging:
            piece = self.dragger.piece
            for move in piece.moves:
                # color
                color = '#C86464' if (move.final.row + move.final.col) % 2 == 0 else '#C84646'
                #rect
                rect = (move.final.col * SqSize, move.final.row * SqSize, SqSize, SqSize)
                #blit
                pygame.draw.rect(surface,color,rect)
                                 