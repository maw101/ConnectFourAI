from ConnectFourState import ConnectFourState

class ConnectFourCLI(ConnectFourState):
    def render(self):
        # print header
        header = ""
        for col_label in range(self.BOARD_WIDTH):
            header += str(col_label) + " "
        print(header)
        # print separator under header
        print(((self.BOARD_WIDTH * 2) - 1) * "-")
        # print grid
        for row in reversed(range(0, self.BOARD_HEIGHT)):
            row_string = ""
            for column in range(0, self.BOARD_WIDTH):
                row_string += str(self.board[column][row]) + " "
            print(row_string)