"""
This script gathers all the downloaded chess data from chess.com and merges 
them into a single file named game_list.pgn for easier preprocessing
"""

import os

# Define path of all my pgns
path = r'..\pythonProject2023-24\chess_data\downloaded_games'

# Get relative paths of all files inside the directory
pgn_paths = os.listdir(path)

# Define empty list
full_content = []

# Iterate through all the files
# Open them and assign all their content to a variable
for i in range(len(pgn_paths)):
    with open(path + '\\' + pgn_paths[i], 'r') as f:
        content = f.read()
        full_content += content 

# Join all the content into one string
merged_string = ''.join(full_content)

# Writes all combined content to a new file
with open('chess_data\game_list.pgn', 'w') as f:
    f.write(merged_string)