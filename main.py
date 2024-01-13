import play
import preprocessing
import training_functions

# PLAYING SETTINGS
play_game = True
play_color = "white"
model_name = "saved_model_black_final"

# TRAINING SETTINGS
train_model = False
train_color = "black"
downloaded_games = "chess_data/downloaded_games"
epochs = 50
config_name = "black_final"

if play_game:
    play.play(model_name, play_color)
elif train_model:

    train_ds, test_ds = preprocessing.preprocessing(downloaded_games, train_color)

    training_functions.training_loop_fit(
        train_ds=train_ds,
        test_ds=test_ds,
        epochs=epochs,
        config_name=config_name)
    
