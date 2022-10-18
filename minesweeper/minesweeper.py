

class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        self.board = self.make_new_board()

        self.dug = set()  # save tuples (0,0) to where the player have opened

    def make_new_board(self):
        # list of lists 2D board: 
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]


def play(dim_size=10, num_bombs=10):
    # 1: create board and plat bombs
    # 2: print the board + take player move
    # 3: if location bomb - throw game over, if location not bomb open recursively
    # 4: check condition to win
    pass