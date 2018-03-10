import Reflex
import Minimax
import Alphabeta

class Player(object):
#     Name determines evaluation function;
#     Symbol determines display; r or b;
    def __init__(self, name, symbol):
        self.symbol = symbol
        self.name = name

#     According to the type of player, determine next move;
    def get_move(self, board):
        if self.name == "agent":
            return Reflex.evaluate(board, self.symbol)

        if self.name == "minimax":
            return Minimax.evaluate(board)

        if self.name == "alphabeta":
            return Alphabeta.evaluate(board)

        if self.name == "player":
            move = input("Player move(two digits with space between them:  )")
            return tuple(map(int, move.split() ) )

    def __str__(self):
        return "Player name: " + self.name + " Player symbol: " + self.symbol
