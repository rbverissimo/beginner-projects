import random


class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        self.board = self.make_new_board()

        self.dug = set()  # save tuples (0,0) to where the player have opened

    def make_new_board(self):
        # list of lists 2D board:
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        # the board will be set as a bunch of nones instead of fields
        bombs_set = 0
        while bombs_set < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)  # since the board is 10x10 for example, 99 choices
            row = loc // self.dim_size
            col = loc % self.dim_size


def play(dim_size=10, num_bombs=10):
    # 1: create board and plat bombs
    # 2: print the board + take player move
    # 3: if location bomb - throw game over, if location not bomb open recursively
    # 4: check condition to win
    pass