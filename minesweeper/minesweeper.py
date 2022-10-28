import random
import re


class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        self.board = self.make_new_board()
        self.assign_values_to_board()

        self.dug = set()  # save tuples (0,0) to where the player have opened

    def make_new_board(self):
        # list of list 2D board:
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        # the board will be set as a bunch of nones instead of fields
        bombs_set = 0
        while bombs_set < self.num_bombs:
            loc = random.randint(0, self.dim_size ** 2 - 1)  # since the board is 10x10 for example, 99 choices
            row = loc // self.dim_size  # 99//10= 9
            col = loc % self.dim_size  # 99%10 = 9

            if board[row][col] == '*':
                continue

            board[row][col] = '*'
            bombs_set += 1

        return board

    def assign_values_to_board(self):
        # iterate over the board list, assign values based on bombs
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_num_neighbor_bombs(r, c)

    def get_num_neighbor_bombs(self, row, col):
        #  analyze neighbors to get the sum of the bombs in the neighbors
        # definition of neighbor: c-1 r, c r-1, c+1 r, c r+1 % == 1
        # cross neighboring: c-1 r-1, c-1 r+1, c+1 r+1, c+1 r-1  % == 2
        num_n_bombs = 0
        for r in range(max(0, row - 1), min(self.dim_size - 1, (row + 1)) + 1):  # max and min for balancing 0,0 or 9,9
            for c in range(max(0, col - 1), min(self.dim_size - 1, (col + 1)) + 1):
                if r == row and c == col:
                    continue
                if self.board[r][c] == '*':
                    num_n_bombs += 1

        return num_n_bombs

    def dig(self, row, col):
        # hit bomb -> game over, dig w/ neighbor bombs -> finish dig, dig w/ no neighbor bombs -> recurse
        self.dug.add((row, col))

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True

        for r in range(max(0, row - 1), min(self.dim_size - 1, (row + 1)) + 1):
            for c in range(max(0, col - 1), min(self.dim_size - 1, (col + 1 )) + 1):
                if (r, c) in self.dug:
                    continue
                self.dig(r, c)

        return True

    def __str__(self):
        # first off: create a board to print
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        # then print the numbers of how many bombs are there neighboring or a space
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if(row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '

        string_rep = ''  # return as the full representation of the board
        widths = []  # gets max column widths for printing

        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(len(max(columns, key=len)))

        indices = [i for i in range(self.dim_size)]
        indices_row = '  '
        cells = []
        #  this first loop creates the representation of the core of the board
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % col)
        indices_row += '  '.join(cells)
        indices_row += ' \n'
        # once it goes here the loop is going the print numbers for reference on the side of the board
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % col)
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size) # we need the str_len so that we can organize things
        # this last line combines everything into one single string to be returned
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep
        

def play(dim_size=10, num_bombs=10):
    # 1: create board and plat bombs
    board = Board(dim_size, num_bombs)
    # 2: print the board + take player move
    # 3: if location bomb - throw game over, if location not bomb open recursively
    # 4: check condition to win
    while len(board.dug) < (board.dim_size ** 2 - num_bombs):
        print(board)
        # RegEx for validation purposes during the input
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row,col: "))
        row, col = int(user_input[0]), int(user_input[-1])  # parse to int the first and last elements
        if row < 0 or row >= board.dim_size or col < 0 or col >= board.dim_size:
            print("Invalid. Try again")
            continue

        # by default, safe is true
        safe = board.dig(row, col)
        if not safe:
            break  # (game over)

    if safe:
        print("You won! Congrats!!")
    else:
        print("Game over :(")
        board.dug = [(r, c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)


if __name__ == '__main__':
    play()




