# Imitating Chess ANN
## A programm that allows players to train against specific opponents

The following project was created as the Python Project WiSe 2023/2024 in the course **Introduction to Computer Programming (Python)** at the **University of Trento**. 

This project is able to convert downloaded *Chess.com* pgn files into a readable move-by-move format and train a customizable artificial neural network specific to one opponent and color as well as play the net in the console.

### File structure

![file_structure](https://github.com/malteebel/pythonProject2023-24/assets/110181759/2737ebcd-de54-4df1-bbad-86e1169f1344)

### How to use this tool

1. Clone this project
2. Install all the necessary packages (maybe link file here)
3. Go in to the **Chess.com archive** of the player you want to imitate, select advanced to choose the color you want your opponent to play and set the path of all files to the **downloaded_games** variable.
4. Execute the main script with the training variables set accordingly, for training **play_game** has to be set to *False*.
5. Execute the main script again with the playing variables set accordingly, for playing **player_color** indicates **YOUR** color. Set model_name to saved_model_[your config name]_with_FIT.
6. Input moves by typing the standard algebraic notation for it, e.g. e4.

### Model

![Model architecture](https://github.com/malteebel/pythonProject2023-24/assets/110181759/bc0efb23-b386-4fdc-887a-7595886a7867)


(Summary/Image here)

### Training

(Explanation here)
