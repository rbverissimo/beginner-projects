import math
import random


class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())  # choice from list
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False  # iterate until find a spot on the list of available_moves
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8)')
            # needs casting to int, but if it can't be cast - thrown an error
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again')

        return val


class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            # it will always take the center first because that's the smartest choice anyway
            square = 4
        else:
            # choose a move trying to maximize win
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        if state.current_winner == other_player:
            return {'position': None,
                    'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)
                    }
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # initializing it to the lowest possible
        else:
            best = {'position': None, 'score': math.inf}  # better initialize it to the maximum possible

        for possible_move in state.available_moves():
            # 1: make a move, try that spot
            state.make_move(possible_move, player)  # it takes a square and a letter

            # 2: recurse minimax to simulate a game after that move, hence the loop
            sim_score = self.minimax(state, other_player)  # alternate players

            # 3: undo the move, so that it can test other moves
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            # 4: update the dictionaries
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best
