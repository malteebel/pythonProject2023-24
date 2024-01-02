"""
This Script takes the list of all games and creates new files, 
one with all moves played total and one file with moves for each 
game(including move number)
"""
import re

path = "chess_data\game_list.pgn"

def separate_games(pgn_path):
    """
    This function takes a pgn file of combined games, reads it and splits
    it into a list of games 

    Args:
        pgn_path (string): string of path to pgn file

    Returns:
        games (list): list of games as string type
    """

    # Opens pgn of all games and loads it into content
    with open(pgn_path, "r") as f:
        content = f.read()
    
    # Uses non greedy matching to only match one game at a time
    games = re.findall(r'(\[Event ".*?)(?=\[Event "|$)', content, re.DOTALL) 
    # Regex matches everything that starts with[Event " until the next 
    # time it occurs or the string ends (last match is not included)

    return games


def separate_moves(game):
    """
    This function takes a single game and extracts all the moves in a format like this:
    '1. e4 e6', '2. c4 d5'

    Args:
        game (string): A single chess.com game most likely from the separate_games function

    Returns:
        combined_moves (list): list of all combined moves including move number
    """
    # Extract the moves from the game text, removing headers and additional annotations
    moves_text = re.sub(r'\[.*?\]', '', game)  # Remove headers
    # Regex matches every character between two square brackets (excludes linebreaks)
    moves_text = re.sub(r'{[\s\S]*?}', '', moves_text)  # Remove comments/time
    # Regex matches every character between two curly brackets, need new variation
    # because comments can have line breaks

    # Strips text of all whitespaces
    moves_text = moves_text.strip()

    # Splitting the moves into 1. 2. etc. keeps the move pairs
    individual_moves = re.split(r'\d+\.\s+', moves_text)
    # Regex matches a number then a dot with minimum 1 whitespace after

    # Cleaning each move string 
    combined_moves = []
    # Skip the first empty split
    for i, move in enumerate(individual_moves[1:], start=1):
        
        # Removes whitespaces before and after the move
        move = move.strip()

        # If there is still a move available
        if move:
            # Splitting move number, whites move and blacks move
            moves = move.split()

            # Fist element is white move
            white_move = moves[0]
            # Second element is the faulty move number, e.g. 1...
            # Third element is blacks move, sometimes white has one move more
            black_move = moves[2] if len(moves) > 2 else ""
            
            # Combining whites and blacks moves with the enumerated move number
            combined_moves.append(f"{i}. {white_move} {black_move}")

    return combined_moves



# Separate all games
games = separate_games(path)


# Creates a file for EACH game
for i, game in enumerate(games):
    # Extract moves from the game
    moves = separate_moves(game)

    # Filenames for EACH game with enumeration
    new_path = f"chess_data\\all_games\game_{i+1}.pgn"

    # Write moves of all games to DIFFERENT files called game_{i}.pgn
    with open(new_path, "w") as f:
        for move in moves:
            f.write(move + "\n")


# BAM double list comprehension, get all the moves from all games into
# ONE variable
all_moves = [move for game in games for move in separate_moves(game)]

# Writes all moves with a new line into a new file called movelist.pgn 
with open("chess_data\move_list.pgn", "w") as f:
    for move in all_moves:
        f.write(move + "\n")
