"""Function to play with the loaded model"""
import chess
from model import ChessANN
from test_states import split_dims
from choose_move import get_best_move
# Comment out until paths are fixed
# from choose_move import eval_moves

# NEED ERROR HANDLING LIKE WITH: IF USER INPUT IN LEGAL_MOVES THEN 
# PUSH ELSE ASK AGAIN


# saved_model_Test_3_with_FIT
def play(model_name, color="black"):

    # Init model
    model_pred = ChessANN()
    # Build input dims
    model_pred.build((12, 8, 8))
    # Load weights from file
    model_pred.load_weights(f"models/{model_name}")

    board = chess.Board()
    print(board)

    # First move if white
    if color == "white":
        # Get user input as SAN notation
        user_input = input("Your move: ")
        board.push_san(user_input)
        print(board)

    # Permanently check if game has ended
    while board.outcome() == None:
        # Slice the board
        # Replace with Franzis function later
        sliced = split_dims(board)
        # Get prediction from model
        pred = model_pred.predict(sliced)
        # Execute best move
        # Replace with Franzis function later
        board.push(get_best_move(board, pred))
        print(board)

        # Users turn
        # Get user input as SAN notation
        user_input = input("Your move: ")
        board.push_san(user_input)
        print(board)
        
    return board.outcome()



