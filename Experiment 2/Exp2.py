import numpy as np

# Activation functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Multi-Layer Perceptron class
class MLP:
    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.1):
        self.learning_rate = learning_rate

        # Initialize weights and biases with small random values
        self.input_hidden_weights = np.random.randn(input_size, hidden_size)
        self.hidden_output_weights = np.random.randn(hidden_size, output_size)
        self.hidden_bias = np.random.randn(hidden_size)
        self.output_bias = np.random.randn(output_size)

    def forward(self, X):
        # Input to Hidden Layer
        self.hidden_input = np.dot(X, self.input_hidden_weights) + self.hidden_bias
        self.hidden_output = sigmoid(self.hidden_input)

        # Hidden to Output Layer
        self.final_input = np.dot(self.hidden_output, self.hidden_output_weights) + self.output_bias
        self.final_output = sigmoid(self.final_input)

        return self.final_output

    def train(self, X, y, epochs=10000):
        for epoch in range(epochs):
            # Forward Pass
            output = self.forward(X)

            # Compute Error
            error = y - output

            # Backpropagation
            output_gradient = error * sigmoid_derivative(output)
            hidden_error = output_gradient.dot(self.hidden_output_weights.T)
            hidden_gradient = hidden_error * sigmoid_derivative(self.hidden_output)

            # Update weights and biases
            self.hidden_output_weights += self.hidden_output.T.dot(output_gradient) * self.learning_rate
            self.output_bias += np.sum(output_gradient, axis=0) * self.learning_rate
            self.input_hidden_weights += X.T.dot(hidden_gradient) * self.learning_rate
            self.hidden_bias += np.sum(hidden_gradient, axis=0) * self.learning_rate

            if epoch % 1000 == 0:
                loss = np.mean(np.abs(error))
                print(f"Epoch {epoch}, Loss: {loss:.4f}")

    def predict(self, X):
        return self.forward(X)

# XOR dataset
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Initialize MLP with 2 input neurons, 2 hidden neurons, and 1 output neuron
mlp = MLP(input_size=2, hidden_size=2, output_size=1)
mlp.train(X, y)

# Predictions
predictions = mlp.predict(X)
predictions = (predictions > 0.5).astype(int)  # Convert probabilities to 0 or 1

# Display XOR truth table with predictions
print("\nXOR Truth Table Predictions:")
print(" X1  X2  |  y_actual  y_pred")
print("---------------------------")
for i in range(len(X)):
    print(f" {X[i][0]}   {X[i][1]}  |     {y[i][0]}        {predictions[i][0]}")
