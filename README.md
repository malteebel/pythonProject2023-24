# pgnBasedChessBot
Python Project WiSe 2023/2024

## Scripts

-> boardstates.py (Franzi)

-> model.py (Malte)

-> preprocessing.py (Malte)

-> regex_functions.py (Malte)

-> test_states.py (Malte)

-> training.py (Malte)

## Data

The folder chess_data contains all the data accociated with the original data. The original data is in the subfolder downloaded_games. The pgn file game_list.pgn contains a list of all games. The pgn file move_list.pgn contains all moves played in all games with the move number in a format like this:

1. e4 c5
2. Nf3 d6

Every pgn file in the all_games folder contains all moves in the same notation of one game.

## How to use this script

**Data handling**

First download data from Chess.com from one player with the desired piece color. Then use the preprocessing.py script to get all relevant data for the model.


**Recreate board states from move sequences** -> In progress

-> boardstates.py -> In  progress (Franzi)

OR for now

-> test_states.py (Malte)

**Model**

(Summary/Image here)

**Training**

**User Interface stuff?**

???
