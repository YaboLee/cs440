import Board

# Return next move for reflex agent;
def evaluate(board, symbol):
    all_pos = []
    for s in board.board:
        if board.board[s] == symbol:
            all_pos.append(s)
    all_pos = sorted(all_pos)
    return (2, 3)
