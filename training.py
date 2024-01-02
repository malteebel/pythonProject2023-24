# Load the TensorBoard notebook extension

import tensorflow as tf
import tqdm
import datetime
from model import *

def training_loop(optimizer, depth, train_ds, test_ds, epochs, config_name):

    time = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

    train_log_path = f"logs\{config_name}\{time}\\train"
    test_log_path = f"logs\{config_name}\{time}\\val"

    # Summary writers
    train_summary_writer = tf.summary.create_file_writer(train_log_path)
    test_summary_writer = tf.summary.create_file_writer(test_log_path)


    # Init model
    model = ChessANN(optimizer, depth)
    model.build(input_shape=(12, 8, 8))

    for epoch in range(epochs):
        print(f"Epoch {epoch + 1}:")

        # Training
        for data in tqdm.tqdm(train_ds):
            metrics = model.train_step(data)

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
            metrics = model.test_step(data)

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
    model.save(f"models\DEPTH_{depth}_EPOCHS{epochs}_{time}"
               , save_format="tf")




