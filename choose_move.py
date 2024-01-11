import numpy as np
import boardstates
import chess
from dim_functions import split_dims


# Franzis function
def eval_moves(board, pred):
    legal_moves = list(board.legal_moves)
    legal_states = []
    for move in legal_moves:
        legal_states.append(boardstates.make_move(move, split_dims(board), board.turn))
    all_dist = []
    for state in legal_states:
        dist = np.linalg.norm(pred - state)
        all_dist.append(dist)
    best_move = legal_moves[np.argmin(all_dist)]
    return (best_move)

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
    best_move = legal_moves[min_dist_idx]
    print(best_move)

    return best_move


