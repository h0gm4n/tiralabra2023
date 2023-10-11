# User Manual

## How to set up the game

Install dependencies:
> pip install -r requirements.txt

## How to run the game

The maximum depth used by the algorithm determines the AI's difficulty. Choose between 1-8. \
(Note: 7 and especially 8 take a lot more time than smaller depths)

The AI utilizes iterative deepening, which means that the depth for the AI's each move is \
determined by the amount of time the player is willing to wait for each move. \
For example, if the player sets the maximum waiting time to 30 seconds, the AI stops going \
deeper if the calculations take more than 30 seconds.

Choose the maximum calculation time between 5-60 seconds.

Run:
> python connect4.py [maximum depth] [maximum calculation time]