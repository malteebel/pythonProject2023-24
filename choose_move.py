import numpy as np
# Comment out until paths are fixed
# import boardstates
import chess
from test_states import split_dims


# Franzis function
# Malte: Why need color???
def eval_moves(board, pred, white=True):
    legal_moves = list(board.legal_moves)
    legal_states = []
    for move in legal_moves:
        legal_states.append(boardstates.makeMove(move, board, white))
    all_dist = []
    for move in legal_moves:
        dist = np.linalg.norm(pred - move)
        all_dist.append(dist)
    best_move = legal_moves[np.argmin(all_dist)]
    return(best_move)

# Maltes function
def get_best_move(board, prediction):

    legal_moves = list(board.legal_moves)
    all_dist = []
    for move in range(len(legal_moves)):
        board.push(legal_moves[move])
        split = split_dims(board)
        dist = np.linalg.norm(prediction - split)
        all_dist.append(dist)
        board.pop()
    
    min_dist_idx = all_dist.index(min(all_dist))
    print
    best_move = legal_moves[min_dist_idx]
    print(best_move)

    return best_move


