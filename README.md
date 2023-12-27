# pgnBasedChessBot
Python Project WiSe 2023/2024

**Data**

- chess_data contains downloaded file from Chess.com
- game_list.pgn contains all games merges with merge.py
- move_list.ogn contains all moves pairs with move number from pgn2movelist.py

**Download PGN data**

-> merge.py (Malte)


**Preprocessing into sequences of moves**

Preprocesses into format like this:
1. e4 c5
2. Nf3 d6

-> pgn2movelist.py (Malte)


**Recreate board states from move sequences** -> In progress

-> boardstates.py -> In  progress (Franzi)

**Model**

Input: flattened 6\*8\*8 board representations

-> RNN_model.py (Malte)

Output layer activation: Softmax
Output layer shape: 6\*8\*8
Loss: Categorical Crossentropy

**Training**

-> training.py -> In progress (Malte)

**User Interface stuff?**

???
