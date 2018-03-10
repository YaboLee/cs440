import random

class Board(object):
#     Dimension is N*N, defalut = 7*7;
    def __init__(self, dimension=7):
        self.dimension = dimension
        self.board = {}
#         Initialize the board;
        for row in range(dimension):
            for col in range(dimension):
                self.board[(row, col)] = "."

    def artificial_board(self, number):
        if number == 1:
            self.board[(2, 0)] = "r"


    def print_board(self):
        for row in range(self.dimension-1, -1, -1):
            for col in range(self.dimension):
                print(self.board[(col, row)], end="   " )
            print("\n")

#     Move must be a tuple;
#     Player is an object;
    def make_move(self, move, player):
        if self.is_valid_move(move):
            self.board[move] = player.symbol
            return move
        else:
            return (-1, -1)

#     Move must be a tuple;
    def is_valid_move(self, move):
#         If the move goes out the board, return False;
        if move[0] < 0 or move[1] < 0 or move[0] >= self.dimension or move[1] >= self.dimension:
            return False
#         If there is no symbol;
        if self.board[move] == ".":
            return True
        else:
            return False

    def random_move(self):
        move = [random.randint(0, len(self.dimension)) for _ in range(2)]
#         If this is not a valid move, loop to get a valid;
#         It can be improved with given valid moves;?????
        while self.is_valid_move(move) is False:
            move = [random.randint(0, len(self.dimension)) for _ in range(2)]
        return tuple(move)

    def all_valid_moves(self):
        valids = []
        for row in range(self.dimension):
            for col in range(self.dimension):
                if self.board[(row, col)] == ".":
                    valids.append((row, col) )
        return valids
