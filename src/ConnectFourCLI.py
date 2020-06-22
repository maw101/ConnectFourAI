from ConnectFourState import ConnectFourState
from ConnectFourAI import ConnectFourAI

class ConnectFourCLI(ConnectFourState):
    def render(self):
        board = self.get_as_2d_board()
        
        print()  # print blank line
        # print header
        header = ""
        for col_label in range(self.BOARD_WIDTH):
            header += str(col_label) + " "
        print(header)
        # print separator under header
        print(((self.BOARD_WIDTH * 2) - 1) * "-")
        # print grid
        for row in range(0, self.BOARD_HEIGHT):
            row_string = ""
            for column in range(0, self.BOARD_WIDTH):
                row_string += board[column][row] + ' '
                    
            print(row_string)
        print()  # print blank line

    def play_game(self):
        ai = ConnectFourAI(self.BOARD_WIDTH)
        ConnectFourState()
        game_over = False
        self.render()
        while not game_over:
            if (self.move_count % 2) + 1 == 1:
                column_index = int(input("Player " + str((self.move_count % 2) + 1) + " enter your column: "))
            else:
                result = ai.solve(self)
                column_index = result[1]
                print('AI Player (Player ' + str((self.move_count % 2) + 2) + ') has chosen to play in column #' + str(column_index))

            if self.is_valid_column_input(column_index) and self.can_play_in_column(column_index):
                if self.is_winning_move(column_index):
                    print("Player " + str((self.move_count % 2) + 1) + " has WON!")
                    game_over = True
                self.play_in_column(column_index)
                
            else:
                # as play_in_column not called, move_count not incremented so player can play again
                print("Invalid Column Entered")

            # re-render grid
            self.render()

            if (not game_over) and self.is_grid_full():  # draw
                print("DRAW! Grid is Full")
                game_over = True



