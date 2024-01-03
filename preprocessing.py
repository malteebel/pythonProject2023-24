"""This script gathers all the downloaded chess data from chess.com 
and merges them into a single file named game_list.pgn for easier 
preprocessing.

It also takes the list of all games and creates new files, one with
all moves played total and one file with moves for each game 
(including the move number)

These were once the scripts merge.py and pgn2movelist.py, they are
now merged.
"""

import os
from regex_functions import separate_games, separate_moves


# Define path of all my pgns
path_downloaded_games = "chess_data/downloaded_games"

# Get relative paths of all files inside the directory
pgn_paths = os.listdir(path_downloaded_games)

# Define empty list
full_content = []

# Iterate through all the files
# Open them and assign all their content to a variable
for i in range(len(pgn_paths)):
    with open(path_downloaded_games + '/' + pgn_paths[i], 'r') as f:
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

# Create the new all_games directory
games_dir = os.mkdir("chess_data/all_games")


# Creates a file for EACH game
for i, game in enumerate(games):
    # Extract moves from the game
    moves = separate_moves(game)

    # Filenames for EACH game with enumeration
    new_path = f"chess_data/all_games/game_{i+1}.pgn"

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