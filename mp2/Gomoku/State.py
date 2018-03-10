import Board
import copy

class State(object):
#     Initialize a board and initial state;
    def __init__(self):
        self.board = Board()
        self.move = (self.board.dimension//2, self.board.dimension//2)

    def artificial_state(self, number):
        self.board.artificial_board(number)


        # Create a new state with move and player;
    def new_state(self, move, player):
        new = State()
        new.board = copy.deepcopy(self.board)
        new.move = new.board.make_move(move, player)
        if new.move = (-1, -1):
            return None
        return new

    # All transition functions for current state;
    # transitions will be passed to specific evaluation function;
    def transition(self, palyer):
        valid_moves = self.board.all_valid_moves()
        transition = []
        for move in valid_moves:
            new_state = self.new_state(move, player)
            transition.append((new_state, player) )

        return transition

    # Check whether current state is winning;
    def is_win(self):
        pass
