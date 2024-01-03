import tensorflow as tf
from keras.callbacks import EarlyStopping
import tqdm
import datetime
from model import ChessANN

def training_loop_man(train_ds, test_ds, epochs, config_name):

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




