from screen import *
from square import Square
from piece import *

class Board:

    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(columns)]

        self._create()
        self._add_pieces("white")
        self._add_pieces("black")



    def _create(self):

        for row in range(rows):
            for col in range(columns):
                self.squares[row][col] = Square(row,col)


    def _add_pieces(self, color):
        if color == "white":
            row_pawns, row_otherpieces = (6,7)
        else:
            row_pawns, row_otherpieces = (1,0)
            
            #creating the pawns
        for col in range(columns):
            self.squares[row_pawns][col] = Square(row_pawns, col, Pawn(color))

            #making the knights
        self.squares[row_otherpieces][1] = Square(row_otherpieces, 1, Knight(color))
        self.squares[row_otherpieces][6] = Square(row_otherpieces, 6, Knight(color))

            #making the bishops
        self.squares[row_otherpieces][2] = Square(row_otherpieces, 2, Bishop(color))
        self.squares[row_otherpieces][5] = Square(row_otherpieces, 5, Bishop(color))

        #rooks
        self.squares[row_otherpieces][0] = Square(row_otherpieces, 0, Rook(color))
        self.squares[row_otherpieces][7] = Square(row_otherpieces, 7, Rook(color))

       #queen
        self.squares[row_otherpieces][3] = Square(row_otherpieces, 1, Queen(color))

       #the king
        self.squares[row_otherpieces][4] = Square(row_otherpieces, 1, King(color))







