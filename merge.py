import os

# Define path of all my pgns
path = r'C:\Users\Malte\Desktop\PythonChessBot\pythonProject2023-24\chess_data'

# get relative paths of all files inside the directory
pgn_paths = os.listdir(path)

# define empty list
full_content = []

# iterate through all the files
# open them and assign all their content to a variable
for i in range(len(pgn_paths)):
    with open(path + '\\' + pgn_paths[i], 'r') as f:
        content = f.read()
        full_content += content 

# join all the content into one string
merged_string = ''.join(full_content)

# writes all combined content to a new file
with open('game_list.pgn', 'w') as f:
    f.write(merged_string)