import numpy as np

class ConnectFourState:

    def __init__(self):
        self.BOARD_HEIGHT = 6
        self.BOARD_WIDTH = 7
        self.current_position = np.zeros(1, dtype=np.uint64)[0]
        self.mask = np.zeros(1, dtype=np.uint64)[0]
        self.move_count = 0

    def can_play_in_column(self, column_index):
        return (self.mask & self.__top_mask(column_index)) == 0 # empty position there

    def play_in_column(self, column_index):
        self.current_position ^= self.mask  # switch the bits of current and opponent
        self.mask |= self.mask + self.__bottom_mask(column_index)  # add extra bit for played position to mask
        self.move_count += 1
        

    def play_sequence_of_moves(self, sequence):
        # process each digit in the sequence
        for digit in sequence:
            column_index = int(digit) - 1  # each digit is one-based
            if (column_index < 0) or (column_index >= self.BOARD_WIDTH) or \
                    (not self.can_play_in_column(column_index)) or self.is_winning_move(column_index):
                return None
            self.play_in_column(column_index)
        return len(sequence)

    def is_winning_move(self, column_index):
        position = self.current_position
        position |= (self.mask + self.__bottom_mask(column_index)) & self.__column_mask(column_index)
        return self.__test_alignment(position)

    def is_grid_full(self):
        return (self.BOARD_WIDTH * self.BOARD_HEIGHT) == self.move_count

    def is_valid_column_input(self, column_index):
        return (column_index >= 0) and (column_index < self.BOARD_WIDTH)

    def get_key(self):
        return self.current_position + self.mask
    
    def get_as_2d_board(self):
        current_player_symbol = (self.move_count % 2) + 1  # get the current players symbol
        opponent_player_symbol = int(not (current_player_symbol - 1)) + 1
        opponent_bitboard = self.mask & ~(self.current_position)
        
        board = [[0 for y in range(self.BOARD_HEIGHT)] for x in range(self.BOARD_WIDTH)]
        # iterate over all positions in the bitboard
        for row in reversed(range(0, self.BOARD_HEIGHT)):
            actual_row_index = (self.BOARD_HEIGHT - 1) - row
            for column in range(0, self.BOARD_WIDTH):
                position_index = np.uint64((column * self.BOARD_WIDTH) + row)
                # check if position empty
                if ((self.mask >> position_index) & np.uint64(1)) == 0:
                    board[column][actual_row_index] = '-'
                
                # determine player who has a counter in this position
                else:
                    if ((self.current_position >> position_index) & np.uint64(1)) == 1:
                        board[column][actual_row_index] = str(current_player_symbol)
                    elif ((opponent_bitboard >> position_index) & np.uint64(1)) == 1:
                        board[column][actual_row_index] = str(opponent_player_symbol)
                    
        return board

    def __test_alignment(self, position):
        # test horizontal
        m = np.uint64(position & (position >> np.uint64(self.BOARD_HEIGHT + 1)))
        if m & (m >> np.uint64(2 * (self.BOARD_HEIGHT + 1))):
            return True
        
        # test vertical
        m = np.uint64(position & (position >> np.uint64(1)))
        if m & (m >> np.uint64(2)):
            return True
        
        # test first diagonal
        m = np.uint64(position & (position >> np.uint64(self.BOARD_HEIGHT)))
        if m & (m >> np.uint64(2 * (self.BOARD_HEIGHT))):
            return True
        
        # test second diagonal
        m = np.uint64(position & (position >> np.uint64(self.BOARD_HEIGHT + 2)))
        if m & (m >> np.uint64(2 * (self.BOARD_HEIGHT + 2))):
            return True
        
        return False

    def __top_mask(self, column):
        return np.uint64((np.int64(1) << (self.BOARD_HEIGHT - 1)) << (column * (self.BOARD_HEIGHT + 1)))
    
    def __bottom_mask(self, column):
        return np.uint64(np.int64(1) << (column * (self.BOARD_HEIGHT + 1)))
                
    def __column_mask(self, column):
        return np.uint64(((np.int64(1) << self.BOARD_HEIGHT) - 1) << (column * (self.BOARD_HEIGHT + 1)))
