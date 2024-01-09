import play
import preprocessing
import model
import training_functions

play_game = False
train_model = True
train_color = "black"
train_path = "chess_data/downloaded_games"
epochs = 50
config_name = "Test_4"

if play_game:
    play.play("saved_model_Test_3_with_FIT", "white")
elif train_model:

    train_ds, test_ds = preprocessing.preprocessing(train_path, train_color)

    training_functions.training_loop_fit(
        train_ds=train_ds,
        test_ds=test_ds,
        epochs=epochs,
        config_name=config_name)
