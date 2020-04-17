from ConnectFourCLI import ConnectFourCLI
from ConnectFourGUI import ConnectFourGUI
from ConnectFourAI import ConnectFourAI

game = ConnectFourCLI()
ai = ConnectFourAI(game.BOARD_WIDTH)
game.play_sequence_of_moves('71523214715215162525')
#game.render()
#print(ai.solve(game))
game.play_game()

#gameGUI = ConnectFourGUI()
#gameGUI.render_grid()
#gameGUI.play_game()