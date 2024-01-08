"""
This script contains both training functions one using the .fit() and
.compile() method of the high level tensorflow library. The manual 
loop does not use this method to allow for a more precise training 
approach.

THE MANUAL LOOP IS CURRENTLY NOT WORKING.
"""

import tensorflow as tf
from keras.callbacks import EarlyStopping, TensorBoard
import datetime
import tqdm
from model import ChessANN

def training_loop_fit(train_ds, test_ds, epochs, config_name):
    """
    This function compiles the model with set loss function and 
    optimizer and fits is to the fed data.

    Args:
        train_ds (tf.data.Dataset): training dataset
        test_ds (tf.data.Dataset): test dataset
        epochs (int): number of epochs training
        config_name (string): Name of the training configuration
    """

    # Log paths for tensorboard
    log_path = f"logs/fit/{config_name}"

    # Initialize model
    model = ChessANN()

    # Add early stopping to save training time if model is not 
    # learning
    early_stopping = EarlyStopping(
        monitor='val_test_loss', patience=10, 
        restore_best_weights=True)
    
    # Add tensorboard to help visualize loss, open tensorboard before
    # training using: tensorboard --logdir logs/fit
    tensorboard_callback = TensorBoard(
        log_dir=log_path, histogram_freq=3)
    
    # Compile model with set metrics 
    model.compile(optimizer="Adam", loss="MSE", metrics=['loss', 'accuracy'])

    # Fit model directly to data with early stopping callback
    model.fit(
        train_ds,
        epochs=epochs,
        validation_data=test_ds,
        callbacks=[early_stopping, tensorboard_callback])
    
    # Save the weights of the model (does not save optimizer state 
    # and is therefore not optimal for loading and continiuing 
    # training), used for predictions
    model.save_weights(f"models/saved_model_{config_name}", save_format="tf")


def training_loop_man(train_ds, test_ds, epochs, config_name):
    """
    UNFINISHED AND NOT WORKING

    Args:
        train_ds (_type_): _description_
        test_ds (_type_): _description_
        epochs (_type_): _description_
        config_name (_type_): _description_
    """

    # Time for logging
    time = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

    # Log paths for tensorboard
    train_log_path = f"logs/{config_name}/{time}/train"
    test_log_path = f"logs/{config_name}/{time}/val"

    # Summary writers for metrics
    train_summary_writer = tf.summary.create_file_writer(train_log_path)
    test_summary_writer = tf.summary.create_file_writer(test_log_path)

    


    # Initialize and ?build? model
    model = ChessANN()
    model.build(input_shape=(12, 8, 8))

    for epoch in range(epochs):
        print(f"Epoch {epoch + 1}:")

        # Training
        for data in tqdm.tqdm(train_ds):
            model.metrics = model.train_step(data)

            # Logging metrics to log file for tensorboard
            with train_summary_writer.as_default():
                tf.summary.scalar(f"{model.metrics[0].name}", 
                                  model.metrics[0].result(), step=epoch)
                tf.summary.scalar(f"{model.metrics[1].name}", 
                                  model.metrics[1].result(), step=epoch)
                
        print(f"{model.metrics[0].name}: {model.metrics[0].result()}")
        print(f"{model.metrics[1].name}: {model.metrics[1].result()}")

        model.reset_metrics()

        # Testing
        for data in test_ds:
            model.metrics = model.test_step(data)

            # Logging metrics to log file for tensorboard
            with test_summary_writer.as_default():
                tf.summary.scalar(f"{model.metrics[2].name}", 
                                  model.metrics[2].result(), step=epoch)
                tf.summary.scalar(f"{model.metrics[3].name}", 
                                  model.metrics[3].result(), step=epoch)
                
        print(f"{model.metrics[2].name}: {model.metrics[2].result() }")
        print(f"{model.metrics[3].name}: {model.metrics[3].result()}")

    # Reset all metrics
    model.reset_metrics()
    print("\n")

    # Saves model
    # model.save(f"models\EPOCHS{epochs}_{time}", save_format="tf")
