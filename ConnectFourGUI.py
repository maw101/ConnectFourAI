import pygame
import sys
from ConnectFourState import ConnectFourState


class ConnectFourGUI(ConnectFourState):
    def __init__(self):
        super().__init__()
        self.SQUARE_SIZE = 200
        self.WINDOW_WIDTH = self.BOARD_WIDTH * self.SQUARE_SIZE
        self.WINDOW_HEIGHT = self.BOARD_HEIGHT * self.SQUARE_SIZE + 1
        self.WINDOW_SIZE = (self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        pygame.init()
        window = pygame.display.set_mode(self.WINDOW_SIZE)

        while True:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("")
