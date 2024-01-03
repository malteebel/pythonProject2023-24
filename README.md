# pgnBasedChessBot
Python Project WiSe 2023/2024

**Scripts**

-> boardstates.py (Franzi)

-> merge.py (Malte)

-> model.py (Malte)

-> pgn2movelist.py (Malte)

-> test_states.py (Malte)

-> training.py (Malte)

**Data**

The folder chess_data contains all the data accociated with the original data. The original data is in the subfolder downloaded_games. The pgn file game_list.pgn contains a list of all games, merged with the script merge.py. The pgn file move_list.pgn contains all moves played in all games with the move number in a format like this:

1. e4 c5
2. Nf3 d6

Every pgn file in the all_games folder contains all moves in the same notation of one game.


**Data handling**

First download data from Chess.com from one player with the desired piece color. Then use the merge.py to merge all games.

-> merge.py (Malte)

-> pgn2movelist.py (Malte)


**Recreate board states from move sequences** -> In progress

-> boardstates.py -> In  progress (Franzi)

OR for now

-> test_states.py (Malte)

**Model**

Input: flattened 12\*8\*8 board representations

-> model.py (Malte)

Output layer activation: Sigmoid
Output layer shape: 6\*8\*8
Loss: MSE (for now) or Element Wise Squared Error

**Training**

-> training.py -> In progress (Malte)

**User Interface stuff?**

???
