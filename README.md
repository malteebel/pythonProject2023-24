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

![image](https://github.com/malteebel/pythonProject2023-24/assets/110181759/56ca29e4-5ef5-42d7-8683-08fddaccdb8d)

We decided to implement a classical feed forward model without convolution. Since our focus was not on the model creation we did not worry about overfitting or quality of the dataset. The data consists of roughly 280 games for each color which is just way too little to for a model to learn the underlying concepts of chess. 

### Training

We implemented a basic training loop with the .compile and .fit methods from the high level tensorflow/keras api. We also started implementing a manual training loop on the low level api for higher customizability. This manual training loop currently **does not work** due to shape errors but can easily be customized depending on the model chosen. We trained the current models on 50 epochs but with callbacks on the loss of the test set.

It proved difficult to assess the quality of the model, we believed that loss was best due to our absolute calculation.

### Notes

We refrained from using some existing libraries and functions to showcase our basic python skills. 

### Outlook

Possible continiuation of this work could be:
1. Testing different model architectures 
2. Improving model quality and hyperparameter optimization
3. Use a pretrained model to then refine it with a small dataset
4. Rework some functions to increase speed of preprocessing and training
5. Add a random factor to the move to increase varaibility
