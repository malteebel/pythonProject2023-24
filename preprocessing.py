"""
This script gathers all the downloaded chess data from chess.com 
and merges them into a single file named game_list.pgn for easier 
preprocessing.

It also takes the list of all games and creates new files, one with
all moves played total and one file with moves for each game 
(including the move number)

These were once the scripts merge.py and pgn2movelist.py, they are
now merged.
"""

import os
import tensorflow as tf
from regex_functions import separate_games, separate_moves
from dim_functions import split_dims, merge_dims, create_datasets, states_from_pgn
from boardstates import get_data
from sklearn.model_selection import train_test_split


def preprocessing(path_downloaded_games="chess_data/downloaded_games", color="black"):
    """
    Handles the preprocessing off the data 

    Args:
        path_downloaded_games (str): Defaults to "chess_data/downloaded_games".
    """

    # Get relative paths of all files inside the directory
    pgn_paths = os.listdir(f"{path_downloaded_games}/{color}")

    # Define empty list
    full_content = []

    # Iterate through all the files
    # Open them and assign all their content to a variable
    for i in range(len(pgn_paths)):
        with open(path_downloaded_games + "/" + color + "/" + pgn_paths[i], 'r') as f:
            content = f.read()
            full_content += content 

    # Join all the content into one string
    merged_string = ''.join(full_content)

    # Writes all combined content to a new file
    with open("chess_data/game_list.pgn", "w") as f:
        f.write(merged_string)



    path_movelist = "chess_data/game_list.pgn"

    # Separate all games
    games = separate_games(path_movelist)

    # Error handling if folder already exists
    try:
        # Create the new all_games directory
        os.mkdir(f"chess_data/all_games")
    except OSError:
        print("all_games already exists")

    try:
        # Create new directory according to the color
        os.mkdir(f"chess_data/all_games/{color}")
    except OSError:
        print(f"all_games/{color} already exists")


    # Creates a file for EACH game
    for i, game in enumerate(games):
        # Extract moves from the game
        moves = separate_moves(game)

        # Filenames for EACH game with enumeration
        new_path = f"chess_data/all_games/{color}/game_{i+1}.pgn"

        # Write moves of all games to DIFFERENT files called game_{i}.pgn
        with open(new_path, "w") as f:
            for move in moves:
                f.write(move + "\n")


    # BAM double list comprehension, get all the moves from all games into
    # ONE variable
    all_moves = [move for game in games for move in separate_moves(game)]

    # Writes all moves with a new line into a new file called movelist.pgn 
    with open("chess_data/move_list.pgn", "w") as f:
        for move in all_moves:
            f.write(move + "\n")


    # This chunk creates all_states list with representations from all 
    # games
    path = "chess_data/all_games"
    all_states = []

    for i in range(len(os.listdir(path))):

        current_file =  f"chess_data/all_games/{color}/game_{i+1}.pgn"
        # New function
        board_states = get_data(current_file)
        # Old function
        # board_states = states_from_pgn(current_file)

        all_states.append(board_states)



    # This creates the datasets
    inputs, targets = create_datasets(all_states, color)

    # This splits the datasets into Training and Testing
    x_train, x_test, y_train, y_test = train_test_split(inputs, targets, test_size=0.2)

    train_ds = tf.data.Dataset.from_tensor_slices((x_train, y_train))
    test_ds = tf.data.Dataset.from_tensor_slices((x_test, y_test))

    return train_ds, test_ds