from Board import *
from Player import *
from State import *

class Gomoku(object):
    # Always start with player_one, red symbol;
    def __init__(self, player_one, player_two):
        self.state = State(player_one) # initial state, current player is player_one;
        self.player_one = Player(player_one, first_or_second=1)
        self.player_two = Player(player_two, first_or_second=2)
        self.winner = None
        self.current = self.player_one
        self.oponent = self.player_two

    def is_over(self):
        # If there is a winner or no avaliable moves;
        if self.winner or not self.state.board.all_valid_moves():
            return True

    # Change the board to the given test model;
        # current = reflex agent, blue, first hand;
    def test_reflex_agent(self, number):
        self.state.artificial_state(number)
        self.current = self.player_two
        self.oponent = self.player_one
        self.state.board.print_board()

        move = self.current.get_move(self.state.board)
        new_state = self.state.new_state(move, self.current)
        new_state.board.print_board()
        # self.state.board.print_board()



    def play_with_reflex(self, first):
        pass
