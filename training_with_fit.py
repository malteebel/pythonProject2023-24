import tensorflow as tf
from keras.callbacks import EarlyStopping, TensorBoard
import datetime
from model import ChessANN

def training_loop_fit(train_ds, test_ds, epochs, config_name):

    # Time for logging
    time = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

    # Log paths for tensorboard
    log_path = f"logs/fit/{config_name}"

    # Initialize and ?build? model
    model = ChessANN()

    # Add early stopping to save training time
    early_stopping = EarlyStopping(
        monitor='val_test_loss', patience=10, 
        restore_best_weights=True)
    
    # Add tensorboard to help visualize loss
    tensorboard_callback = TensorBoard(
        log_dir=log_path, histogram_freq=3)
    
    # Compile model
    model.compile(optimizer="Adam", loss="MSE", metrics=['loss', 'accuracy'])

    # Fit model directly to data
    model.fit(
        train_ds,
        epochs=epochs,
        validation_data=test_ds,
        callbacks=[early_stopping, tensorboard_callback])
    
    model.save_weights(f"saved_model_{config_name}", save_format="tf")