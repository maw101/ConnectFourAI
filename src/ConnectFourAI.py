import random
import sys

from ConnectFourState import ConnectFourState
from copy import deepcopy


class ConnectFourAI:

    def __init__(self, board_width):
        self.column_order = [0 for x in range(0, board_width)]
        # array contains: middle element, element to left of middle, element to right of middle, element to left of
        #   element in index 1, ..., etc.
        midpoint = int(board_width / 2)
        index_at = 1
        add_value = 1
        self.column_order[0] = midpoint
        while index_at < board_width:
            if index_at % 2 == 0:  # even index
                multiplier = 1
            else:
                multiplier = -1
            self.column_order[index_at] = midpoint + (multiplier * add_value)
            if index_at % 2 == 0:  # even index
                add_value += 1
            index_at += 1

    def negamax_connect_four(self, game_state, alpha, beta):
        # check if game drawn
        if game_state.is_grid_full():
            return 0, None

        # check if we can win with the next move
        for column_index in range(0, game_state.BOARD_WIDTH):  # check each column
            if game_state.can_play_in_column(self.column_order[column_index]) and game_state.is_winning_move(
                    self.column_order[column_index]):
                # score based on number of moves left in the game
                #   most moves left means we have the quickest chance of winning if we play that move
                move_score = int((game_state.BOARD_WIDTH * game_state.BOARD_HEIGHT + 1 - game_state.move_count) / 2)
                return move_score, self.column_order[column_index]

        score_upper_bound = int((game_state.BOARD_WIDTH * game_state.BOARD_HEIGHT - 1 - game_state.move_count) / 2)
        if beta > score_upper_bound:
            beta = score_upper_bound  # update beta value
            if alpha >= beta:
                return beta, None  # prune exploration

        best_column = random.choice(ConnectFourAI.get_valid_columns(game_state))

        # calculate score for all possible future moves
        for column_index in range(0, game_state.BOARD_WIDTH):  # check each column
            if game_state.can_play_in_column(self.column_order[column_index]):
                copied_game_state = deepcopy(game_state)
                copied_game_state.play_in_column(self.column_order[column_index])  # play in current column
                # our score will be the opposite of our opponents
                score = (self.negamax_connect_four(copied_game_state, -beta, -alpha))[0]  # score
                score = -score
                if score >= beta:
                    return score, self.column_order[column_index]
                if score > alpha:
                    alpha = score
                    best_column = self.column_order[column_index]

        return alpha, best_column

    @staticmethod
    def get_valid_columns(game_state):
        valid_columns = []
        for column_index in range(0, game_state.BOARD_WIDTH):  # check each column
            if game_state.can_play_in_column(column_index):
                valid_columns.append(column_index)
        return valid_columns

    def solve(self, game_state, weak_solve=False):
        if weak_solve:
            return ConnectFourAI.negamax_connect_four(game_state, -1, 1)
        # set widest window possible
        board_size = game_state.BOARD_WIDTH * game_state.BOARD_HEIGHT
        alpha = -int(board_size / 2)
        beta = int(board_size / 2)
        return self.negamax_connect_four(game_state, alpha, beta)

    def get_column_to_play(self, game_state, weak_solve=False):
        return self.solve(game_state, weak_solve)