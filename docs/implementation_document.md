
The program is divided into four python files. Connect4_ai.py has the AI's functionality i.e. the implementation of the minimax algorithm, alpha-beta pruning and iterative deepening.
Connect4_ui.py has the user interface and the pygame loop. Connect4_utils.py has some of the functionality that several files use.
Constants.py has all constants. The game is executed through connect4.py.

One major flaw remains in the AI: the minimax algorithm's process time takes a lot longer when focused in the right edge of the board.

ChatGPT has been used to help implement iterative deepening to the minimax algorithm.

Sources: \
https://www.youtube.com/watch?v=MMLtza3CZFM \
https://connect4.gamesolver.org/


## Time Complexity

The time complexity is O(d^b), where d = depth and b = amount of branches \
The amount of branches (sqrt(7) < b < 7) depends on the chosen column - left side generating less branches \
and right side generating more.
