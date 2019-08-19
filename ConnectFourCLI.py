from ConnectFourState import ConnectFourState


class ConnectFourCLI(ConnectFourState):
    def render(self):
        print()  # print blank line
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
                if self.board[column][row] == 0:
                    row_string += "- "
                else:
                    row_string += str(self.board[column][row]) + " "
            print(row_string)
        print()  # print blank line

    def play_game(self):
        ConnectFourState()
        game_over = False
        while not game_over:
            column_index = int(input("Player " + str((self.move_count % 2) + 1) + " enter your column: "))
            if self.is_valid_column_input(column_index) and self.can_play_in_column(column_index):
                self.play_in_column(column_index)
            else:
                # as play_in_column not called, move_count not incremented so player can play again
                print("Invalid Column Entered")
            self.render()



