"""This script can create board states from pgn games"""

import os
import numpy as np
import random
import chess
import chess.pgn

def random_board(max_depth=50):
    """
    This function can instantiate a random board configuration
    starting from the opening position

    Args:
        max_depth (int, optional): Maximum amount of moves played on 
        both sides. Defaults to 50.

    Returns:
        board (chess.Board()): random board state
        target (chess.Board()): state of board including 
        next/opponents move
    """

    # Initialize the board and target board
    board = chess.Board()
    target_board = chess.Board()

    # randomize the depth of moves
    depth = random.randrange(0, max_depth)

    # Loop creating random state
    for _ in range(depth):
        # List of all legal moves
        all_moves = list(board.legal_moves)
        # Picks one random move
        random_move = random.choice(all_moves)

        # Execute the move on both boards
        board.push(random_move)
        target_board.push(random_move)

        # Check if game is over
        if board.is_game_over() or target_board.is_game_over():
            break
    
    # Add another move to target board
    next_moves = list(board.legal_moves)
    random_next = random.choice(next_moves)
    target_board.push(random_next)

    # Check also for target board
    if board.is_game_over() or target_board.is_game_over():
        return board, None

    # Return both boards
    return board, target_board


def split_dims(board):
    """Splits board into different piecemaps

    Creates 6 boardstates containing only one type of piece

    Args:
        board (chess.Board()): board state

    Returns:
        board6d (list (nested)): Stacked matrix of all piecemaps
    """
    # Inits all maps as empty
    board6d = np.zeros((6, 8, 8), dtype=np.float32)

    # Iterate through all pieces 
    for piece in chess.PIECE_TYPES:
        # For all squares that the pice is on and its white
        for square in board.pieces(piece, chess.WHITE):
            # np.unravel_index turns memory coordinate back 
            # into an actual coordinate 
            idx = np.unravel_index(square, (8, 8))
            # Assigns 1 to piece
            board6d[piece - 1][7 - idx[0]][idx[1]] = 1

        # For all squares that the piece is on and its black
        for square in board.pieces(piece, chess.BLACK):
            idx = np.unravel_index(square, (8, 8))
            # Assigns -1 to piece
            board6d[piece - 1][7 - idx[0]][idx[1]] = -1

    # Returns the stacked matrix
    return board6d

def merge_dims(board6d):
    """
    Merges 6 dimensional board representation into a chess.Board() 
    board

    Args:
        board6d (list (nested)): 6d board representation

    Returns:
        board (chess.Board()): visual board representation
    """
    # Inits an empty board without any pieces
    board = chess.Board(None)
    
    # Iterate through all pieces
    for piece in chess.PIECE_TYPES:
        # Iterate through all rows and colums while accessing the 
        # layer corresponding to the piece type
        for row_idx, row in enumerate(board6d[piece - 1]):
            for col_idx, val in enumerate(row):
                # White pieces
                if val == 1:
                    square = chess.square(col_idx, 7 - row_idx)
                    board.set_piece_at(square, chess.Piece(piece, chess.WHITE))
                # Black pieces
                elif val == -1:
                    square = chess.square(col_idx, 7 - row_idx)
                    board.set_piece_at(square, chess.Piece(piece, chess.BLACK))
    
    # Returns a chess.Board() board
    return board

def states_from_pgn(pgn_path):
    """
    Turns all moves from one game pgn into a visual representation

    Args:
        pgn_path (string): path to pgn file of one game

    Returns:
        board_states (list): list of visual representations of all 
        states in one game 
    """
    board_states = []

    # Open the PGN file of one game
    with open(pgn_path) as pgn_file:
        # Read the next game from the PGN file
        game = chess.pgn.read_game(pgn_file)

        # Initialize a board in starting position
        board = game.board()
        # Iterate through all moves
        for move in game.mainline_moves():
            # Make the move
            board.push(move)
            # Append a copy of the current board state to the list
            board_states.append(board.copy())

    return board_states


# This chunk creates all_states list with representations from all 
# games
path = r"all_games"
all_states = []

for i in range(len(os.listdir(path))):

    current_file =  f"all_games\game_{i+1}.pgn"
    board_states = states_from_pgn(current_file)

    all_states.append(board_states)