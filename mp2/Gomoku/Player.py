from Reflex import *
# import Minimax
# import Alphabeta
import string

class Player(object):
#     Name determines evaluation function;
#     Symbol determines display; r or b;
    def __init__(self, name, first_or_second):
        if first_or_second == "1":
            self.symbol = string.ascii_lowercase
            self.stones = list(string.ascii_lowercase)
        else:
            self.symbol = string.ascii_uppercase
            self.stones = list(string.ascii_uppercase)
        self.name = name
        self.winning_blocks = {
                                "row1": [],
                                "row2": [],
                                "row3": [],
                                "row4": [],
                                "row5": [],
                                "col1": [],
                                "col2": [],
                                "col3": [],
                                "col4": [],
                                "col5": [],
                                "diag1": [],
                                "diag2": [],
                                "diag3": [],
                                "diag4": [],
                                "diag5": []
                                }


#     According to the type of player, determine next move;
    def get_move(self, board, opponent):
        if self.name == "reflex":
            r = Reflex(board, self, opponent)
            return r.evaluate()

        if self.name == "minimax":
            return Minimax.evaluate(board, self)

        if self.name == "alphabeta":
            return Alphabeta.evaluate(board, self)

        if self.name == "player":
            move = input("Player move(two digits with space between them:  )")
            return tuple(map(int, move.split() ) )

    def __str__(self):
        return "Player name: " + self.name + " Player symbol: " + self.symbol
