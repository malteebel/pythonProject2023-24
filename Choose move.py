import numpy as np
import boardstates
import chess
import preprocessing
import test_states
def eval_moves(board, pred):
    legal_moves = list(board.legal_moves)
    legal_states = []
    for move in legal_moves:
        legal_states.append(boardstates.make_move(move, preprocessing.split_dims(board), board.turn))
    all_dist = []
    for move in legal_moves:
        dist = np.linalg.norm(pred - move)
        all_dist.append(dist)
    best_move = legal_moves[np.argmin(all_dist)]
    return(best_move)





