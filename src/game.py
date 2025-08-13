import pygame
from const import *
from board import Board
from dragger import Dragger
from config import Config
class Game:
    def __init__(self):
        self.next_player = "white"
        self.board = Board()
        self.hovered_square =None
        self.dragger = Dragger()
        self.config = Config()
    def Show_last_move(self, surface):
        self.board.show_last_move(surface, self.config.theme)
    def show_hover(self,surface):
        if self.hovered_square:
            color  = (180,180,180)
            rect  = (self.hovered_square.col * SqSize,self.hovered_square.row * SqSize,SqSize,SqSize)
            pygame.draw.rect(surface,color,rect,width = 3)
    def set_hover(self,row,col):
        self.hovered_square = self.board.squares[row][col]
    def show_bg(self, surface):
        theme = self.config.theme
        for row in range(rows):
            for col in range(cols):
                #color
                color = theme.bg.light if (row + col) % 2 == 0 else theme.bg.dark
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
        theme = self.config.theme
        if self.dragger.dragging:
            piece = self.dragger.piece
            for move in piece.moves:
                # color
                color = theme.moves.light if (move.final.row + move.final.col) % 2 == 0 else theme.moves.dark
                #rect
                rect = (move.final.col * SqSize, move.final.row * SqSize, SqSize, SqSize)
                #blit
                pygame.draw.rect(surface,color,rect)
    def Change_theme(self):
        self.config.change_theme()          
    # next turn
    def next_turn(self):
        self.next_player = 'white' if self.next_player == 'black' else 'black'
