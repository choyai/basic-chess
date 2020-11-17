import numpy as np
from enum import Enum
class Color(Enum):
    LIGHT = 0
    DARK = 1

class Square:    

    def __init__( self,  value, x, y ):
        self.value = value
        self.color = (x + y) % 2
        self.x = x
        self.y = y

    def __repr__( self ):
        return str(self.value) + ' ' + str((x, y))
        
class Chessboard:

    def __init__(self):
        self.squares = []
        self.state = np.zeros((8, 8))
        
        for i in range(8):
            for j in range(8):
                square = Square(0, i, j)
                self.squares.append(square)

    def __repr__(self):
        return self.state.__repr__()