import numpy as np

BOARD_SIZE = 19
# The shape of a small aero is
# X X H X X
# X X O X X
# O O O O O
# X X O X X
# X O O O X
# The shape of a big aero is
# X X X H X X X
# X X X O X X X
# X X X O X X X
# O O O O O O O
# X X X O X X X
# X X X O X X X
# X O O O O O X

class board:
    index_of_board = 0
    list_of_board = []

    def __init__(self):
        self.board = np.array([[0 for i in range(0, BOARD_SIZE)]for j in range(0, BOARD_SIZE)])
        # 0 for empty, 1 for body of aero, 2 for head of aero
        # 3 for hit but empty, 4 for hit but body, 5 for hit and head
        self.ready = False
        # set aero before ready and shoot aero after ready
        self.index = board.index_of_board
        self.num_of_aero = 0
        board.index_of_board += 1
        board.list_of_board.append(self)

    def set_small_aero(self, x, y, d):
        if self.ready:
            return False
        # x and y for position and d for direction
        # 0 for up, 1 for down, 2 for left, 3 for right
        if x < 2 or y < 2 or x + 3 > BOARD_SIZE or y + 3 > BOARD_SIZE:
            return False
        if sum(self.board[x,y-2:y+3]) + sum(self.board[x-2:x+3,y]) != 0:
            return False
        if d == 0:
            if self.board[x-2][y] != 0:
                return False
        elif d == 1:
            if self.board[x+2][y] != 0:
                return False
        elif d == 2:
            if self.board[x][y-2] != 0:
                return False
        elif d == 3:
            if self.board[x][y+2] != 0:
                return False
        else:
            return False
        self.num_of_aero += 1
        self.board[x,y-2:y+3] = 1
        self.board[x-2:x+3,y] = 1
        if d == 0:
            self.board[x-2,y] = 2
            self.board[x+2,y-1:y+2] = 1
        elif d == 1:
            self.board[x+2,y] = 2
            self.board[x-2,y-1:y+2] = 1
        elif d == 2:
            self.board[x,y-2] = 2
            self.board[x-1:x+2,y+2] = 1
        else:
            self.board[x,y+2] = 2
            self.board[x-1:x+2,y-2] = 1
        return True

    def set_big_aero(self, x, y, d):
        if self.ready:
            return False
        # x and y for position and d for direction
        # 0 for up, 1 for down, 2 for left, 3 for right
        if x < 3 or y < 3 or x + 4 > BOARD_SIZE or y + 4 > BOARD_SIZE:
            return False
        if sum(self.board[x,y-3:y+4]) + sum(self.board[x-3:x+4,y]) != 0:
            return False
        if d == 0:
            if self.board[x-3][y] != 0:
                return False
        elif d == 1:
            if self.board[x+3][y] != 0:
                return False
        elif d == 2:
            if self.board[x][y-3] != 0:
                return False
        elif d == 3:
            if self.board[x][y+3] != 0:
                return False
        else:
            return False
        self.num_of_aero += 1
        self.board[x,y-3:y+4] = 1
        self.board[x-3:x+4,y] = 1
        if d == 0:
            self.board[x-3,y] = 2
            self.board[x+3,y-2:y+3] = 1
        elif d == 1:
            self.board[x+3,y] = 2
            self.board[x-3,y-2:y+3] = 1
        elif d == 2:
            self.board[x,y-3] = 2
            self.board[x-2:x+3,y+3] = 1
        else:
            self.board[x,y+3] = 2
            self.board[x-2:x+3,y-3] = 1
        return True
    
    def shoot(self, x, y):
        if self.board[x][y] < 3:
            self.board[x][y] += 3
            if self.board[x][y] == 5:
                self.num_of_aero -= 1
            return True
        else:
            return False
    
    def display_all(self):
        print("The board of player %d is"%self.index)
        print(self.board)
    
    def display_shoot(self):
        print("The shootboard of player %d is"%self.index)
        shoot_board = np.where(self.board < 3, 0, self.board)
        print(shoot_board)