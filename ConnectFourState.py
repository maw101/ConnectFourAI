class ConnectFourState:

    def __init__(self):
        self.BOARD_HEIGHT = 6
        self.BOARD_WIDTH = 7
        self.board = [[0 for y in range(self.BOARD_HEIGHT)] for x in range(self.BOARD_WIDTH)]
        self.column_height = [0 for col in range(self.BOARD_WIDTH)]
        self.move_count = 0

    def can_play_in_column(self, column_index):
        return self.column_height[column_index] < self.BOARD_HEIGHT

    def play_in_column(self, column_index):
        # store the players identifier in the free space at the lowest free space of the chosen column
        self.board[column_index][self.column_height[column_index]] = (self.move_count % 2) + 1
        self.column_height[column_index] += 1
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
        current_player_symbol = (self.move_count % 2) + 1  # get the current players symbol

        # if there are at least three counters in the column, check if the three closest
        #   to the top belong to the current player
        current_column_height = self.column_height[column_index]
        if (current_column_height >= 3) and \
                (self.board[column_index][current_column_height - 1] == current_player_symbol) and \
                (self.board[column_index][current_column_height - 2] == current_player_symbol) and \
                (self.board[column_index][current_column_height - 3] == current_player_symbol):
            return True  # current player will have four in a row

        move_x = column_index
        move_y = self.column_height[column_index]

        # check two horizontals and the four diagonals
        for y_change in [-1, 0, 1]:  # horizontal checked when = 0, otherwise checking diagonal
            number_in_a_row = 0
            for x_change in [-1, 1]:  # checks either side of current position
                x = move_x + x_change
                y = move_y + (x_change * y_change)
                while (x >= 0) and (x < self.BOARD_WIDTH) and \
                        (y >= 0) and (y < self.BOARD_HEIGHT) and \
                        (self.board[x][y] == current_player_symbol):
                    x += x_change
                    y += (x_change * y_change)
                    number_in_a_row += 1
            if number_in_a_row >= 3:
                return True
        return False

    def is_valid_column_input(self, column_index):
        return (column_index >= 0) and (column_index < self.BOARD_WIDTH)
