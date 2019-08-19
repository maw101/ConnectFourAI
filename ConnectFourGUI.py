import pygame
import sys
import math
from ConnectFourState import ConnectFourState


class ConnectFourGUI(ConnectFourState):
    def __init__(self):
        super().__init__()
        self.SQUARE_SIZE = 200
        self.WINDOW_WIDTH = int(self.BOARD_WIDTH * self.SQUARE_SIZE)
        self.WINDOW_HEIGHT = int((self.BOARD_HEIGHT + 1.5) * self.SQUARE_SIZE)
        self.WINDOW_SIZE = (self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        self.BACKGROUND_COLOUR = (64, 64, 64)  # dark grey
        pygame.init()
        self.window = pygame.display.set_mode(self.WINDOW_SIZE)
        self.window.fill(self.BACKGROUND_COLOUR)  # set background to be dark grey

    def play_game(self):
        player_colours = ('Red', 'Yellow')  # player 1 = red; player 2 = yellow
        # initilise new game
        ConnectFourState()
        game_over = False

        self.display_message(player_colours[self.move_count % 2] + " place your counter")
        self.render_grid()

        # play game
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEMOTION:
                    # want to draw a counter above the current column if can play there
                    # draw a rectangle at the top to hide previous renders
                    pygame.draw.rect(self.window, self.BACKGROUND_COLOUR, (0, int(0.5 * self.SQUARE_SIZE), self.WINDOW_WIDTH, int(1.5 * self.SQUARE_SIZE)))
                    # determine colour of the current players counter
                    if (self.move_count % 2) + 1 == 1:
                        colour = (255, 0, 0)  # red
                    else:
                        colour = (255, 255, 0)  # yellow
                    pygame.draw.circle(self.window, colour, (event.pos[0], int(((1.5 * self.SQUARE_SIZE) / 2) + (0.25 * self.SQUARE_SIZE))), int((self.SQUARE_SIZE - 20) / 2))
                    self.render_grid()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.display_message(player_colours[(self.move_count + 1) % 2] + " place your counter")
                    column_index = int(math.floor(event.pos[0] / self.SQUARE_SIZE))

                    if self.is_valid_column_input(column_index) and self.can_play_in_column(column_index):
                        if self.is_winning_move(column_index):
                            self.display_message("Player " + str((self.move_count % 2) + 1) + " has WON!")
                            game_over = True
                        self.play_in_column(column_index)
                    else:
                        # as play_in_column not called, move_count not incremented so player can play again
                        self.display_message("Cannot Place in Column #" + str(column_index + 1))

                    if (not game_over) and self.is_grid_full():
                        self.display_message("DRAW! Grid is Full")
                        game_over = True

                    self.render_grid()
        pygame.time.wait(2500)


    def display_message(self, text):
        # hide previous message
        pygame.draw.rect(self.window, self.BACKGROUND_COLOUR, (0, 0, self.WINDOW_WIDTH, int(0.5 * self.SQUARE_SIZE)))
        # prepare and render new message
        text_font = pygame.font.Font('freesansbold.ttf', 50)
        text_surface = text_font.render(text, True, (255, 255, 255))
        text_rectangle = text_surface.get_rect()
        text_rectangle.center = (int(self.WINDOW_WIDTH / 2), int(self.SQUARE_SIZE / 4))
        self.window.blit(text_surface, text_rectangle)
        pygame.display.update()


    def render_grid(self):
        board_colour = (51, 153, 255)
        radius = int((self.SQUARE_SIZE - 20) / 2)
        for row in reversed(range(0, self.BOARD_HEIGHT)):
            for column in range(0, self.BOARD_WIDTH):
                pygame.draw.rect(self.window, board_colour, (column * self.SQUARE_SIZE, ((self.BOARD_HEIGHT - row) * self.SQUARE_SIZE) + int(0.5 * self.SQUARE_SIZE), self.SQUARE_SIZE-1, self.SQUARE_SIZE-1))
                if self.board[column][row] == 0:
                    colour = self.BACKGROUND_COLOUR
                elif self.board[column][row] == 1:
                    colour = (255, 0, 0)  # red
                else:
                    colour = (255, 255, 0)  # yellow
                # add the circle to our render
                pygame.draw.circle(self.window, colour, (int((column + 0.5) * self.SQUARE_SIZE), self.WINDOW_HEIGHT - int((row + 0.5) * self.SQUARE_SIZE)), radius)
        pygame.display.update()