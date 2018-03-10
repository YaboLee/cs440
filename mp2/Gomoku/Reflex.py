

class Reflex(object):

    def __init__(self, board, player):
        self.board = board
        self.current_player = player
        self.chain = {} # open_row4, broken_row4, open_row3, broken_row3, ...

    # Return next move for reflex agent;
    def evaluate(self):
        # print(player.symbol)
        all_pos = []
        for s in board.board:
            if board.board[s] == player.symbol:
                all_pos.append(s)
        all_pos = sorted(all_pos)
        return (2, 3)

    def exisiting_moves(self):
        symbol = None
        if "z" in self.current_player:
            symbol = string.ascii_lowercase
        else:
            symbol = string.ascii_uppercase

        exisiting_moves = []
        for m in self.board.board:
            if self.board.board[m] in symbol:
                exisiting_moves.append(m)
        return sorted(exisiting_moves, key=lambda x: (x[0], x[1]) )

    def chain_row(self):
        exisiting_moves = self.exisiting_moves()
        chain_row = []
        for m in exisiting_moves:
            temp = [m]
            x = m[0]
            y = m[1]
            while x + 1 < self.board.dimension:
                if (x+1, y) in exisiting_moves:
                    temp.append((x+1, y) )
                    exisiting_moves.remove((x+1, y) )
                    x += 1
                else:
                    break
            if len(temp) > 1:
                chain_row.append(temp)

        row2 = list(map(lambda x: x if len(x) == 2) )
        open_row2 = []
        broken_row2 = []
        for row in row2:
            if self.row_spot_valid((row[0]-1, row[1]) ) and self.row_spot_valid((row[0]+1, row[1]) ):
                open_row2.append(row)
            elif not self.row_spot_valid((row[0]-1, row[1]) ) and not self.row_spot_valid((row[0]+1, row[1]) ):
                continue # dead_row
            else:
                broken_row2.append(row)
        if open_row2:
            self.chain["open_row2"] = open_row2
        if broken_row2:
            self.chain["broken_row2"] = broken_row2

        row3 = list(map(lambda x: x if len(x) == 3) )
        open_row3 = []
        broken_row3 = []
        for row in row3:
            if self.row_spot_valid((row[0]-1, row[1]) ) and self.row_spot_valid((row[0]+1, row[1]) ):
                open_row3.append(row)
            elif not self.row_spot_valid((row[0]-1, row[1]) ) and not self.row_spot_valid((row[0]+1, row[1]) ):
                continue # dead_row
            else:
                broken_row3.append(row)
        if open_row3:
            self.chain["open_row3"] = open_row3
        if broken_row3:
            self.chain["broken_row3"] = broken_row3

        row4 = list(map(lambda x: x if len(x) == 4) )
        open_row4 = []
        broken_row4 = []
        for row in row4:
            if self.row_spot_valid((row[0]-1, row[1]) ) and self.row_spot_valid((row[0]+1, row[1]) ):
                open_row4.append(row)
            elif not self.row_spot_valid((row[0]-1, row[1]) ) and not self.row_spot_valid((row[0]+1, row[1]) ):
                continue # dead_row
            else:
                broken_row4.append(row)
        if open_row4:
            self.chain["open_row4"] = open_row4
        if broken_row4:
            self.chain["broken_row4"] = broken_row4


    def row_spot_valid(self, spot):
        if spot[0] >= 0 and spot[0] < self.board.dimension and self.board.board[spot] == ".":
            return True
        return False



    def chain_col(self):
        exisiting_moves = self.exisiting_moves()
        chain_col = []
        for m in exisiting_moves:
            temp = [m]
            x = m[0]
            y = m[1]
            while y + 1 < self.board.dimension:
                if (x, y+1) in exisiting_moves:
                    temp.append((x, y+1) )
                    exisiting_moves.remove((x, y+1) )
                    y += 1
                else:
                    break
            if len(temp) > 1:
                chain_row.append(temp)

        col2 = list(map(lambda x: x if len(x) == 2) )
        open_col2 = []
        broken_col2 = []
        for col in col2:
            if self.col_spot_valid((col[0], col[1]-1) ) and self.col_spot_valid((col[0], col[1]+1) ):
                open_col2.append(col)
            elif not self.col_spot_valid((col[0], col[1]-1) ) and not self.col_spot_valid((col[0], col[1]+1) ):
                continue # dead_row
            else:
                broken_col2.append(col)
        if open_col2:
            self.chain["open_col2"] = open_col2
        if broken_col2:
            self.chain["broken_col2"] = broken_col2

        col3 = list(map(lambda x: x if len(x) == 3) )
        open_col3 = []
        broken_col3 = []
        for col in col3:
            if self.col_spot_valid((col[0], col[1]-1) ) and self.col_spot_valid((col[0], col[1]+1) ):
                open_col3.append(col)
            elif not self.col_spot_valid((col[0], col[1]-1) ) and not self.col_spot_valid((col[0], col[1]+1) ):
                continue # dead_row
            else:
                broken_col3.append(col)
        if open_col3:
            self.chain["open_col3"] = open_col3
        if broken_col3:
            self.chain["broken_col3"] = broken_col3

        col4 = list(map(lambda x: x if len(x) == 4) )
        open_col4 = []
        broken_col4 = []
        for col in col4:
            if self.col_spot_valid((col[0], col[1]-1) ) and self.col_spot_valid((col[0], col[1]+1) ):
                open_col4.append(col)
            elif not self.col_spot_valid((col[0], col[1]-1) ) and not self.row_spot_valid((col[0], col[1]+1) ):
                continue # dead_row
            else:
                broken_col4.append(col)
        if open_col4:
            self.chain["open_col4"] = open_col4
        if broken_col4:
            self.chain["broken_col4"] = broken_col4


    def col_spot_valid(self, spot):
        if spot[1] >= 0 and spot[1] < self.board.dimension and self.board.board[spot] == ".":
            return True
        return False
