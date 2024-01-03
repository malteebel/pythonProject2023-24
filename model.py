"""Script containing the class of the model and all the parameters"""

import tensorflow as tf

# Add class that inherits from tf.keras.Model class
class ChessANN(tf.keras.Model):
    """This class inherits all traits from the tf.keras.Model class"""

    # Define init function to override inheritance of parents init 
    # function
    def __init__(self):
        """
        Initializes subclass of tf.keras.Model class, also creates 
        metrics for model optimization
        """

        # Make the ChessANN class inherit all methods and properties 
        # from the tf.keras.Model class
        super(ChessANN, self).__init__()

        # OPTIMIZER
        # Set optimizer in class
        self.optimizer = tf.keras.optimizers.Adam()

        # ERROR FUNCTION
        # Set MSE as loss function
        # Can also try MSLE and MAE
        # MAYBE Squared Error Per Element is better
        self.loss_function = tf.keras.losses.MeanSquaredError()

        # Set metrics in class
        self.metrics_list = [
            tf.keras.metrics.Mean(name="train_loss"),
            tf.keras.metrics.CategoricalAccuracy(name="train_acc"),
            tf.keras.metrics.Mean(name="test_loss"),
            tf.keras.metrics.CategoricalAccuracy(name="test_acc")]

        # Define model
        self.layer_1 = tf.keras.layers.Dense(units=64, activation="relu")
        self.layer_2 = tf.keras.layers.Dense(units=128, activation="relu")
        self.layer_3 = tf.keras.layers.Dense(units=256, activation="relu")
        self.dropout_4 = tf.keras.layers.Dropout(rate=0.2)
        self.batch_norm_5 = tf.keras.layers.BatchNormalization()
        self.layer_6 = tf.keras.layers.Dense(units=64, activation="relu")
        self.layer_7 = tf.keras.layers.Dense(units=128, activation="relu")
        self.layer_8 = tf.keras.layers.Dense(units=256, activation="relu")
        self.dropout_9 = tf.keras.layers.Dropout(rate=0.2)
        self.batch_norm_10 = tf.keras.layers.BatchNormalization()

        # Output layer with sigmoid activation
        self.out_11 = tf.keras.layers.Dense(12*8*8, activation="sigmoid")

        # Add a reshape layer to change the output shape to 12x8x8
        self.reshape_12 = tf.keras.layers.Reshape((12, 8, 8))


    # Use tf.function to increase speed
    @tf.function
    def call(self, x):
        """
        Activates the model and feeds information forward through
        the layers

        Args:
            x (tensor): data, all board states
        """

        # Ensure correct input shape
        x = tf.reshape(x,  [-1, 12*8*8])
        
        x = self.layer_1(x)
        x = self.layer_2(x)
        x = self.layer_3(x)
        x = self.dropout_4(x)
        x = self.batch_norm_5(x)
        x = self.layer_6(x)
        x = self.layer_7(x)
        x = self.layer_8(x)
        x = self.dropout_9(x)
        x = self.batch_norm_10(x)
        
        # Finally feed through output layer and reshape
        x = self.out_11(x)
        x = self.reshape_12(x)

        return x

    def reset_metrics(self):
        """Reset all the metrics, can be used after every epoch"""
        # Resets all metrics
        for metric in self.metrics:
            metric.reset_states()

    @tf.function
    def train_step(self, data):
        """
        Calculates the output and adjusts weights based on loss of
        one forward computation

        Args:
            data (tensor?): data that contains sequences

        Returns:
            dict: train metrics
        """
        # Split into x and target
        x, targets = data

        with tf.GradientTape() as tape:
            # Predict one target
            predictions = self(x, training=True)

            # Calculates loss of target & prediction relation + additional 
            # losses like regularization penalties
            loss = self.loss_function(targets, predictions) + tf.reduce_sum(self.losses)


        # Calculate gradients of the loss
        gradients = tape.gradient(loss, self.trainable_variables)

        # Update the models variables using optimizer and gradients
        self.optimizer.apply_gradients(zip(gradients, self.trainable_variables))

        # Update training loss metric
        self.metrics[0].update_state(loss)
        # Update training accuracy metric
        self.metrics[1].update_state(targets, predictions)

        # Return a dictionary mapping training metrics to current value
        return {metric.name: metric.result() for metric in self.metrics}
    
    @tf.function
    def test_step(self, data):
        """Calculates the output of one forward computation

        Args:
            data (tensor?): data that contains sequences

        Returns:
            dict: test metrics
        """
        # Split into x and targets
        x, targets = data
        
        # Predict one target without changing variables
        predictions = self(x, training=False)

        # Calculate test loss
        loss = self.loss_function(targets, predictions) + tf.reduce_sum(self.losses)
        
        # Update test loss
        self.metrics[2].update_state(loss)

        # Upadte testing accuracy
        self.metrics[3].update_state(targets, predictions)

        # Return a dictionary mapping testing metrics to current value
        return {metric.name: metric.result() for metric in self.metrics}