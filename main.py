import play
import preprocessing
import training_functions

# PLAYING SETTINGS
play_game = False
play_color = "black"
model_name = "saved_model_Mixed_Test_02"

# TRAINING SETTINGS
train_model = True
train_color = "white"
downloaded_games = "chess_data/downloaded_games"
epochs = 50
config_name = "Mixed_Test_02"

if play_game:
    play.play(model_name, play_color)
elif train_model:

    train_ds, test_ds = preprocessing.preprocessing(downloaded_games, train_color)

    training_functions.training_loop_fit(
        train_ds=train_ds,
        test_ds=test_ds,
        epochs=epochs,
        config_name=config_name)
    
