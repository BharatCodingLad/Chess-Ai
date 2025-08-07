from const import *
from square import Square
from piece import *
from dragger import *
from move import Move
class Board:
    def __init__(self):
        self.squares = [[0,0,0,0,0,0,0,0] for col in range(cols)]
        self._create()
        self._add_pieces("white")
        self._add_pieces("black")
        self.last_move = None
    def calc_moves(self,piece,row,col):
        # this is going to calculate the moves a selected piece
        piece.moves = [] 
        def pawn_moves(row,col):
            # 2 moves
            if piece.moved:
                steps = 1
            else :
                steps = 2
            # vertical moves
            start = row + piece.dir
            end = row + (piece.dir * (1+steps))
            for mov_row in range(start,end,piece.dir):
                if Square.in_range(mov_row,col):
                    if self.squares[mov_row][col].isempty():
                        # create initial and final sqaures
                        initial = Square(row,col)
                        final = Square(mov_row,col)
                        move = Move(initial,final)
                        piece.add_move(move)
                    # mean we are blocked    
                    else :  
                        break  
                else :
                    break
            # diagonal move    
            move_row = row+piece.dir
            move_col = [col-1,col+1]
            for possible_col in move_col:
                if Square.in_range(move_row,possible_col):
                    if self.squares[move_row][possible_col].has_rival_piece(piece.color):
                        # create initial and final sqaures
                        initial = Square(row,col)
                        final = Square(move_row,possible_col)
                        move = Move(initial,final)
                        piece.add_move(move)
        def straightLine_moves(incrs):
            for incr in incrs:
                row_incr,col_incr = incr
                possible_row = row + row_incr
                possible_col = col + col_incr
                #while True
                while True:
                  if Square.in_range(possible_row,possible_col):
                    intitial = Square(row,col)
                    final = Square(possible_row,possible_col)
                    move = Move(intitial,final)
                    if self.squares[possible_row][possible_col].isempty():   
                        #create a new move 
                        piece.add_move(move)
                    if self.squares[possible_row][possible_col].has_rival_piece(piece.color):
                        piece.add_move(move)  
                        break
                    if self.squares[possible_row][possible_col].has_team_piece(piece.color):
                        break
                  else : break       
                  possible_row += row_incr
                  possible_col += col_incr    
        def kinght_moves(row,col):
            #8 moves
            possible_moves = [
                (row-2,col-1),(row-2,col+1),
                (row+2,col-1),(row+2,col+1),
                (row-1,col-2),(row-1,col+2),
                (row+1,col-2),(row+1,col+2)
            ]
            for possible in possible_moves:
                possible_row , possible_col = possible
                if Square.in_range(possible_row,possible_col):
                    if self.squares[possible_row][possible_col].isempty_or_rival(piece.color):
                         # create a square of a move
                        initial = Square(row,col)
                        final = Square(possible_row,possible_col) # piece = piece
                        # move
                        move =Move(initial,final)
                        #append new valid move
                        piece.add_move(move)
        def king_moves():
            adjs = [
                (row-1,col-1),(row-1,col),(row-1,col+1),
                (row,col-1),(row,col+1),
                (row+1,col-1),(row+1,col),(row+1,col+1)
            ]    
            for moves in adjs:
                possible_row,possible_col = moves
                if Square.in_range(possible_row,possible_col):
                    if self.squares[possible_row][possible_col].isempty_or_rival(piece.color):
                        initial = Square(row,col)
                        final = Square(possible_row,possible_col)
                        move = Move(initial,final)
                        piece.add_move(move) 
                    if self.squares[possible_row][possible_col].has_team_piece(piece.color):
                        continue             
        if piece.name == "pawn":
            pawn_moves(row,col)
        elif piece.name == "knight":
            kinght_moves(row,col)
        elif piece.name == "bishop":
            straightLine_moves([(-1,1),(-1,-1),(1,1),(1,-1)])
        elif piece.name == "rook":
            straightLine_moves([(1,0),(-1,0),(0,1),(0,-1)])
        elif piece.name == "queen":
            straightLine_moves([(-1,1),(-1,-1),(1,1),(1,-1),(1,0),(-1,0),(0,1),(0,-1)])
        elif piece.name == "king":
            king_moves()
    def _create(self):
        for row in range(rows):
            for col in range(cols):
                self.squares[row][col] = Square(row,col)
    def _add_pieces(self,color):
        if color == "white":
            row_pawn,row_other = (6,7)
        else :
            row_pawn,row_other = (1,0)
        for col in range(cols):
            self.squares[row_pawn][col] = Square(row_pawn,col,Pawn(color)) # pawns   
        #knights
        self.squares[row_other][1] = Square(row_other,1,Knight(color))
        self.squares[row_other][6] = Square(row_other,6,Knight(color))
        #bishops
        self.squares[row_other][2] = Square(row_other,2,Bishop(color))
        self.squares[row_other][5] = Square(row_other,5,Bishop(color))
        #rooks
        self.squares[row_other][0] = Square(row_other,0,Rook(color))
        self.squares[row_other][7] = Square(row_other,7,Rook(color))
        #quuen and king
        self.squares[row_other][3] = Square(row_other,3,Queen(color))
        self.squares[row_other][4] = Square(row_other,4,King(color))
    def move(self,piece,move):
        initial = move.initial
        final = move.final
        self.squares[initial.row][initial.col].piece = None  
        self.squares[final.row][final.col].piece = piece
        piece.moved = True
        piece.moves = []
        piece.clear_moves()
        self.last_move = move
    def valid_move(self,piece,move):
           return move in piece.moves
    def __eq__(self,other):
        return self.initial == other.initial and self.final == other.final
    def clear_moves(self):
        self.moves = []