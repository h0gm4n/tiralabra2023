
The program is divided into four python files. Connect4_ai.py has the AI's functionality i.e. the implementation of the minimax algorithm and alpha-beta pruning.
Connect4_ui.py has the user interface and the pygame loop. Connect4_utils.py has some of the functionality that several files use.
Constants.py has all constants. The game is executed through connect4.py.

The gameplay doesn't allow the player yet to choose the AI's difficulty i.e. the depth of the minimax algorithm calls.
This could be a future feature. Also, the heuristic scoring system may be flawed and hasn't yet been tested well enough to give the best results.
I have also noticed that the minimax algorithm's process time takes a lot longer when focused in the right edge of the board.

ChatGPT has been used to help the calculation and analyzation of the code's time complexity.

Sources: \
https://www.youtube.com/watch?v=MMLtza3CZFM \
https://connect4.gamesolver.org/


## Time Complexity

The time complexity is O(d^b), where d = depth and b = amount of branches \
The amount of branches (sqrt(7) < b < 7) depends on the chosen column - left side generating less branches \
and right side generating more,