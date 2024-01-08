import numpy as np
import boardstates
import chess
def eval_moves(board, pred, white=True):
    legal_moves = list(board.legal_moves)
    legal_states = []
    for move in legal_moves:
        legal_states.append(boardstates.make_move(move, board, white))
    all_dist = []
    for move in legal_moves:
        dist = np.linalg.norm(pred - move)
        all_dist.append(dist)
    best_move = legal_moves[np.argmin(all_dist)]
    return(best_move)




