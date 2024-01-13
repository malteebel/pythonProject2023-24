import numpy as np
import boardstates
import chess
from dim_functions import split_dims



# Franzis function
#function to compare our output with the legal moves, choosing the move that is closest to our output probability-distribution
def eval_moves(board, pred):
    #ceate a lsit with all legal moves
    legal_moves = list(board.legal_moves)
    legal_states = []
    #convert our current boardstate into a dictionary
    board_dict = boardstates.convert_to_dict(split_dims(board))
    #create a new boardstate out of all legal-move notations
    for move in legal_moves:
        state = boardstates.convert_to_matrix(boardstates.make_move(board.san(move), board_dict, board.turn))
        legal_states.append(state)
    all_dist = []
    #calculate the distance of these new board-states to our probability-matrix
    for state in legal_states:
        dist = np.linalg.norm(pred - state)
        all_dist.append(dist)
    #choose the move that results in a board-matrix that is closest to our probability matrix
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


