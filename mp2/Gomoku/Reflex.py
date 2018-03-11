

class Reflex(object):

    def __init__(self, board, player, opponent):
        self.board = board
        self.current_player = player
        self.opponent = opponent
        self.chain = {} # open_row4, broken_row4, open_row3, broken_row3, ...

    # Return next move for reflex agent;
    def evaluate(self):
        self.board.find_wb(self.current_player)
        self.board.find_wb(self.opponent)
        print(self.current_player.winning_blocks, self.current_player.symbol)
        print(self.opponent.winning_blocks, self.opponent.symbol)
        
        return (0, 0)
