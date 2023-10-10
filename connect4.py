import sys
import src.connect4_ui as connect4_ui


if 10 >= int(sys.argv[1]) >= 1 and 120 >= int(sys.argv[2]) >= 5:
    connect4_ui.run_game(int(sys.argv[1]), int(sys.argv[2]))
else:
    print("\nChoose a depth between 1 and 10 and max. waiting time between 5 and 120!\n")
