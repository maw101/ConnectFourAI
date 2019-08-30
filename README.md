# Connect Four with AI

## AI Element
**NOTE: The AI element is currently under development.**

The current state of the AI Element is as follows:
* Utilises negamax recursive algorithm to score future moves from both players perspectives. Maximises the score for itself and minimising it for the opponent.
* Utilises Alpha-Beta Pruning to narrow the exploration window by taking into account previously explored moves.
* Scores moves from the centre outward as moves closer to the centre will be involved in more alignments.

Future plans for the AI element to optimise it further include:
* Anticipation of losing moves
* Iterative deepening
* The implementation of a transposition table for the cachine of moves

## Key Releases
* [Player Vs Player V1.0 Released with GUI and CLI Interfaces](https://github.com/maw101/ConnectFourAI/releases/tag/PvP-V1.0)


## Demos
### Player vs Player
[V1.0 Released with GUI and CLI Interfaces](https://github.com/maw101/ConnectFourAI/releases/tag/PvP-V1.0)
#### Graphical User Interface (GUI)
![](player_vs_player_gui_demo.gif)

#### Command Line Interface (CLI)
![](player_vs_player_cli_demo.gif)
