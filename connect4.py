import sys
import src.connect4_ui as connect4_ui


if 8 >= int(sys.argv[1]) >= 1:
    connect4_ui.run_game(int(sys.argv[1]))
else:
    print("\nChoose a depth/difficulty between 1 and 8!\n")
