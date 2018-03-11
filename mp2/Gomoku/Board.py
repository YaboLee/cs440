import random

class Board(object):
#     Dimension is N*N, defalut = 7*7;
    def __init__(self, dimension=7):
        self.dimension = dimension
        self.board = {}
        # self.current_player_wb = {} # open_row3, broken_row3, open_row2, broken_row2, open
        # self.oppoent_player_wb = {}
#         Initialize the board;
        for row in range(dimension):
            for col in range(dimension):
                self.board[(row, col)] = "."


    def artificial_board(self, number):
        if number == 1:
            self.board[(2, 1)] = "b"
            self.board[(2, 2)] = "b"
            self.board[(2, 3)] = "b"
            self.board[(2, 4)] = "b"
            self.board[(3, 1)] = "R"
            self.board[(3, 3)] = "R"
            self.board[(4, 3)] = "R"
            self.board[(4, 4)] = "R"
            self.board[(6, 2)] = "R"
        if number == 2:
            self.board[(3, 0)] = "b"
            self.board[(2, 0)] = "b"
            self.board[(2, 1)] = "b"
            self.board[(3, 1)] = "R"
            self.board[(3, 2)] = "R"
            self.board[(3, 3)] = "R"
            self.board[(3, 4)] = "R"
        if number == 3:
            self.board[(1, 1)] = "b"
            self.board[(3, 2)] = "b"
            self.board[(2, 2)] = "R"
            self.board[(2, 3)] = "R"
            self.board[(2, 4)] = "R"
        else:
            self.board[(3, 1)] = "R"
            self.board[(2, 2)] = "R"
            self.board[(1, 3)] = "R"


    def print_board(self):
        for row in range(self.dimension-1, -1, -1):
            for col in range(self.dimension):
                print(self.board[(col, row)], end="   " )
            print("\n")

#     Move must be a tuple;
#     Player is an object;
    def make_move(self, move, player):
        if self.is_valid_move(move):
            self.board[move] = player.stones.pop(0)
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



    def find_wb(self, player):
        self.row_wb(player)
        self.col_wb(player)
        self.diag_wb(player)
        # print(row_wb)

    def row_wb(self, player):
        for row in range(self.dimension):
            for col in range(1, -1, -1):
                i = 1 # next i-th spot;
                count = 0 # how many my stones in this block;
                temp_block = []
                while i <= 5: # next four spot
                    # print(player.symbol)
                    # print(self.board[(col+i, row)])
                    if self.board[(col+i, row)] == ".":
                        temp_block.append((col+i, row))
                        # print(temp_block)
                    elif self.board[(col+i, row)] in player.symbol:
                        temp_block.append((col+i, row))
                        count += 1
                    else: # there is oponent in this block;
                        break
                    i += 1
                # print(temp_block, count)
                if count == 0: # there is no my stone in this block;
                    continue
                # print(temp_block)
                if len(temp_block) == 5: # there is no opponent
                    if count == 1:
                        player.winning_blocks["row1"].append(temp_block)
                        # print(temp_block)
                    elif count == 2:
                        player.winning_blocks["row2"].append(temp_block)
                    elif count == 3:
                        player.winning_blocks["row3"].append(temp_block)
                    elif count == 4:
                        player.winning_blocks["row4"].append(temp_block)
                    elif count == 5:
                        player.winning_blocks["row5"].append(temp_block)
        # print(player.winning_blocks)
        return player.winning_blocks

    def col_wb(self, player):
        for col in range(self.dimension):
            for row in range(0, 2):
                i = 1 # next i-th spot;
                count = 0 # how many my stones in this block;
                temp_block = []
                while i <= 5: # next four spot
                    if self.board[(col, row+i)] == ".":
                        temp_block.append((col, row+i))
                    elif self.board[(col, row+i)] in player.symbol:
                        temp_block.append((col, row+i))
                        count += 1
                    else: # there is oponent in this block;
                        break
                    i += 1
                if count == 0: # there is no my stone in this block;
                    continue
                if len(temp_block) == 5: # there is no opponent
                    if count == 1:
                        player.winning_blocks["col1"].append(temp_block)
                    elif count == 2:
                        player.winning_blocks["col2"].append(temp_block)
                    elif count == 3:
                        player.winning_blocks["col3"].append(temp_block)
                    elif count == 4:
                        player.winning_blocks["col4"].append(temp_block)
                    elif count == 5:
                        player.winning_blocks["col5"].append(temp_block)


    def diag_wb(self, player):
        pos = [(2, 0), (2, 1), (2, 2), (1, 0), (1, 1), (1, 2), (0, 0), (0, 1), (0,2)]

        for p in pos:
            i = 1
            temp_block = [p]
            count = 0
            while i <= 4:
                if self.board[(p[0]+i, p[1]+i)] == ".":
                    temp_block.append((p[0]+i, p[1]+i) )
                elif self.board[(p[0]+i, p[1]+i)] in player.symbol:
                    temp_block.append((p[0]+i, p[1]+i))
                    count += 1
                else: # there is oponent in this block;
                    break
                i += 1
                # print(temp_block)
            if count == 0: # there is no my stone in this block;
                continue
            if len(temp_block) == 5: # there is no opponent
                if count == 1:
                    player.winning_blocks["diag1"].append(temp_block)
                elif count == 2:
                    player.winning_blocks["diag2"].append(temp_block)
                elif count == 3:
                    player.winning_blocks["diag3"].append(temp_block)
                elif count == 4:
                    player.winning_blocks["diag4"].append(temp_block)
                elif count == 5:
                    player.winning_blocks["diag5"].append(temp_block)
