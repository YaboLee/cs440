import sys
from Gomoku import *

def main():
    if len(sys.argv) != 3:
        sys.exit('Usage: %s <type of player_one: reflex/minimax/alphabeta/player>\
                 <type of player_two: reflex/minimax/alphabeta/player>' % sys.argv[0])

    game = Gomoku(sys.argv[1], sys.argv[2] )
    game.test_reflex_agent(1)
    # game.mode = int(input("Choose Mode: "))
    # game.start()


if __name__ == "__main__":
    main()
