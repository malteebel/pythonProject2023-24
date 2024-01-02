"""Script containing the class of the model and all the parameters"""
import tensorflow as tf

# Check for GPU support and Cuda/cuDNN installation
# print(tf.config.list_physical_devices('GPU'))

class ChessANN(tf.keras.Model):
    """This class inherits all traits from the tf.keras.Model class"""

    # Define init function to override inheritance of parents init 
    # function so we can add optimizer and depth
    def __init__(self, optimizer, depth):
        """
        Initializes subclass of tf.keras.Model class, also creates 
        metrics for model optimization

        Args:
            optimizer (string): Optimizer being used for training
            depth (int): number of LSTM cells
        """

        # Make the ChessANN class inherit all methods and properties 
        # from the tf.keras.Model class
        super(ChessANN, self).__init__()

        # Set optimizer in class
        self.optimizer = optimizer

        # Set metrics in class
        self.metrics_list = [
            tf.keras.metrics.Mean(name="train_loss"),
            tf.keras.metrics.CategoricalAccuracy(name="train_acc"),
            tf.keras.metrics.Mean(name="test_loss"),
            tf.keras.metrics.CategoricalAccuracy(name="test_acc")]
        
        # ERROR FUNCTION
        # Set MSE as loss function
        # Can also try MSLE and MAE
        # MAYBE Squared Error Per Element is better
        self.loss_function = tf.keras.losses.MeanSquaredError()

        # Initialize a list that can contain all layers for depth arg
        self.layer_list = []

        # Build model based on depth
        for _ in range(depth):
            # Dense layers with relu activation
            layer = tf.keras.layers.Dense(units=64, activation="relu")
            self.layer_list.append(layer)

        # Output layer with sigmoid activation
        self.out = tf.keras.layers.Dense(12*8*8, activation="sigmoid")

        # Add a reshape layer to change the output shape to 12x8x8
        self.reshape = tf.keras.layers.Reshape((12, 8, 8))


    # Use tf.function to increase speed
    # @tf.function
    def call(self, x):
        """
        Activates the model and feeds information forward through
        the layers

        Args:
            x (tensor): data, all board states
        """
        x = tf.reshape(x,  [-1, 12*8*8])

        # Go through layer list depending on depth
        for layer in self.layer_list:
            x = layer(x)
        
        # Finally feed through output layer
        x = self.out(x)
        x = self.reshape(x)

        return x

    def reset_metrics(self):
        """Reset all the metrics, can be used after every epoch"""
        # Resets all metrics
        for metric in self.metrics:
            metric.reset_states()

    # @tf.function
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