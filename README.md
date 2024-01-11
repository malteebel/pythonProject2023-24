# Imitating Chess ANN
## A programm that allows players to train against specific opponents

The following project was created as the Python Project WiSe 2023/2024 in the course **Introduction to Computer Programming (Python)** at the **University of Trento**. 

This project is able to convert downloaded *Chess.com* pgn files into a readable move-by-move format and train a customizable artificial neural network specific to one opponent and colour as well as play the net in the console.

### File structure
![alt text](https://github.com/malteebel/pythonProject2023-24/blob/main/file_structure.pgn?raw=true)
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
