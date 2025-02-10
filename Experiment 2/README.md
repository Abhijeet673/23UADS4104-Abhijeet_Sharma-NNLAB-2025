Experiment 2 - Program to implement a mul-layer perceptron (MLP) network with one hidden layer using numpy in Python using the demostration that it can learn the XOR Boolean function.


The Python program implements a Multi-Layer Perceptron (MLP) using NumPy to learn the XOR Boolean function.

First, the XOR truth table is created as the input dataset. The MLP consists of two input neurons, two hidden neurons, and one output neuron. The network uses the sigmoid activation function for both the hidden and output layers.

During training, the forward propagation step computes the activations from input to output, while backpropagation adjusts the weights using the gradient of the error. The training loop runs for a fixed number of epochs (10,000) with a learning rate of 0.1 to optimize performance.

Finally, the trained MLP predicts the XOR outputs, ensuring that the results match the expected truth table. The predictions are formatted to clearly display the actual vs. predicted values for better readability. 
