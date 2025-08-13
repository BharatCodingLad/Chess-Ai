import pygame
import sys
from const import *
from game import Game
from square import Square
from move import Move
class Main :
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Width,Height))
        pygame.display.set_caption("Chess AI")
        self.game = Game()
    def mainloop(self):
        game = self.game
        screen = self.screen
        dragger = self.game.dragger
        board = self.game.board
        while(True):
            game.show_bg(screen)
            game.Show_last_move(screen)
            game.show_moves(screen)
            game.show_hover(screen)
            game.show_pieces(screen)
            if dragger.dragging:
                dragger.update_blit(screen)
            for event in pygame.event.get():
                #click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
                    clicked_row = dragger.mouseY // SqSize
                    clicked_col = dragger.mouseX // SqSize
                    # if clicked square has a piece?
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        # valid piece color?
                        if piece.color == game.next_player:
                           board.calc_moves(piece,clicked_row,clicked_col)
                           dragger.save_initial(event.pos)
                           dragger.drag_piece(piece)
                           game.show_bg(screen)
                           game.Show_last_move(screen)
                           game.show_moves(screen)
                           game.show_pieces(screen)
                #mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    motion_row = event.pos[1] // SqSize
                    motion_col = event.pos[0] // SqSize
                    game.set_hover(motion_row,motion_col)
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        game.show_bg(screen)
                        game.Show_last_move(screen)
                        game.show_moves(screen)
                        game.show_hover(screen)
                        game.show_pieces(screen)
                        dragger.update_blit(screen)
                #click release
                elif event.type == pygame.MOUSEBUTTONUP:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        released_row = dragger.mouseY // SqSize
                        released_col = dragger.mouseX // SqSize
                        initial = Square(dragger.initial_row, dragger.initial_col)
                        final = Square(released_row, released_col)
                        move = Move(initial, final)
                        if board.valid_move(dragger.piece, move):
                            board.move(dragger.piece,move)
                            #show methods
                            game.show_bg(screen)
                            game.Show_last_move(screen)
                            game.show_pieces(screen)
                            game.next_turn()
                    dragger.undrag_piece()
                # key press
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_t:
                        game.Change_theme()
                        # Redraw everything with the new theme
                        game.show_bg(screen)
                        game.Show_last_move(screen)
                        game.show_moves(screen)
                        game.show_hover(screen)
                        game.show_pieces(screen)
                        pygame.display.update()
                #quit
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            pygame.display.update()        
                    
main = Main()
main.mainloop()