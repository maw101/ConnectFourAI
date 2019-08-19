import pygame
import sys
import math
from ConnectFourState import ConnectFourState


class ConnectFourGUI(ConnectFourState):
    def __init__(self):
        super().__init__()
        self.SQUARE_SIZE = 200
        self.WINDOW_WIDTH = self.BOARD_WIDTH * self.SQUARE_SIZE
        self.WINDOW_HEIGHT = (self.BOARD_HEIGHT + 1) * self.SQUARE_SIZE
        self.WINDOW_SIZE = (self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        pygame.init()
        self.window = pygame.display.set_mode(self.WINDOW_SIZE)

    def play_game(self):
        ConnectFourState()
        game_over = False

        pygame.display.flip()
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("Player " + str((self.move_count % 2) + 1) + " choose your column on the GUI")
                    column_index = int(math.floor(event.pos[0] / self.SQUARE_SIZE))
                    print(column_index)
                    
                    # if self.is_valid_column_input(column_index) and self.can_play_in_column(column_index):
                    #     if self.is_winning_move(column_index):
                    #         print("Player " + str((self.move_count % 2) + 1) + " has WON!")
                    #         game_over = True
                    #     self.play_in_column(column_index)
                    # else:
                    #     # as play_in_column not called, move_count not incremented so player can play again
                    #     print("Invalid Column Entered")
                    #
                    # self.render()
                    #
                    # if (not game_over) and self.is_grid_full():
                    #     print("DRAW! Grid is Full")
                    #     game_over = True

    def render_grid(self):
        board_colour = (51, 153, 255)
        black = (0, 0, 0)
        radius = int((self.SQUARE_SIZE - 20) / 2)
        for row in reversed(range(0, self.BOARD_HEIGHT)):
            for column in range(0, self.BOARD_WIDTH):
                pygame.draw.rect(self.window, board_colour, (column * self.SQUARE_SIZE, (row + 1) * self.SQUARE_SIZE, self.SQUARE_SIZE-1, self.SQUARE_SIZE-1))
                pygame.draw.circle(self.window, black, (int((column + 0.5) * self.SQUARE_SIZE), int((row + 1.5) * self.SQUARE_SIZE)), radius)