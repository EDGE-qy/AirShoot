import board
import os
import numpy as np

NUM_OF_PLAYER = 2

class game:
    def __init__(self, mode=0):        
        if mode == 0: # 0 for PVP mode
            self.boards = [board.board() for i in range(NUM_OF_PLAYER)]
            self.win = NUM_OF_PLAYER
        else:
            raise ValueError("PVE mode is not finished!")
    
    def set_aero(self, pid):
        while True:
            print("Player %d\nPlease set your first small aero."%pid)
            x = int(input("x:"))
            y = int(input("y:"))
            d = int(input("d:"))
            if isinstance(x, int) and isinstance(y, int) and isinstance(d, int):
                if self.boards[pid].set_small_aero(x, y, d):
                    break
        self.boards[pid].display_all()
        while True:
            print("Player %d\nPlease set your second small aero."%pid)
            x = int(input("x:"))
            y = int(input("y:"))
            d = int(input("d:"))
            if isinstance(x, int) and isinstance(y, int) and isinstance(d, int):
                if self.boards[pid].set_small_aero(x, y, d):
                    break
        self.boards[pid].display_all()
        while True:
            print("Player %d\nPlease set your big aero."%pid)
            x = int(input("x:"))
            y = int(input("y:"))
            d = int(input("d:"))
            if isinstance(x, int) and isinstance(y, int) and isinstance(d, int):
                if self.boards[pid].set_big_aero(x, y, d):
                    break
        self.boards[pid].display_all()

    def shoot(self, pid):
        # XOR converts 1 and 0, but not work where more players
        while True:
            print("Player %d\nPlease shoot."%pid)
            x = int(input("x:"))
            y = int(input("y:"))
            if isinstance(x, int) and isinstance(y, int):
                if self.boards[pid^1].shoot(x, y):
                    if self.boards[pid^1].board[x][y] == 3:
                        print("You missed.")
                    elif self.boards[pid^1].board[x][y] == 4:
                        print("You hit part of the body!")
                    elif self.boards[pid^1].board[x][y] == 5:
                        print("You hit one of the head!")
                    self.boards[pid^1].display_shoot()
                    break
    
    def play(self):
        print("Please set aero.")
        self.set_aero(0)
        input("Press enter to switch.")
        os.system("cls")
        self.set_aero(1)
        print("Aero set. Please begin to shoot.")
        input("Press enter to switch.")
        os.system("cls")
        pid = 0
        while True:
            self.shoot(pid)
            if self.boards[pid^1].num_of_aero == 0:
                print("Player %d wins! Congratulations!"%pid)
                break
            else:
                input("Press enter to switch.")
                os.system("cls")
            pid ^= 1