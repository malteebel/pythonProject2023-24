import numpy as np
import boardstates
import chess
from dim_functions import split_dims



# Franzis function
def eval_moves(board, pred):
    legal_moves = list(board.legal_moves)
    legal_states = []
    board_dict = boardstates.convert_to_dict(split_dims(board))
    for move in legal_moves:
        state = boardstates.convert_to_matrix(boardstates.make_move(board.san(move), board_dict, board.turn))
        legal_states.append(state)
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


test = boardstates.get_data("/Users/franziska-marieplate/Documents/5. Semester/Python/Chess/pythonProject2023-24/chess_data/all_games/game_363.pgn")
array_3d = np.random.rand(12, 8, 8)
#print(test[-1].legal_moves)
#print(list(test[-1].legal_moves))
print(get_best_move(test[-2], array_3d))
print(eval_moves(test[-2], array_3d))
