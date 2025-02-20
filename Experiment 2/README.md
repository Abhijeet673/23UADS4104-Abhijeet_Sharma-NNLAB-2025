<h2>Experiment 2</h2>
Program to implement a mul-layer perceptron (MLP) network with one hidden layer using numpy in Python using the demostration that it can learn the XOR Boolean function.

<h3>Model Description</h3>
The model contains a single hidden layer, an input layer and a ouput layer. The output layer contains a single perceptron and the hidden layer contains four perceptron. <br><br>
The four perceptrons are trained on the basis of boolean inputs using "Perceptron Learning Algorithm" where step function is used as activation function. <br><br>
After training each perceptron of hidden layer give positive output only for a single combination of boolean inputs. <br>
Finally the output perceptron is trained using the "Perceptron Learning Algorithm" where the inputs given are the outputs from 
each trained perceptron of the hidden layer & it gives the output mimicking the XOR function. 

<h3>Code Description</h3>

In the main function all four perceptrons from the hidden layer are trained against the XOR truth table inputs to give unique outputs.

Then the prediction of these inputs is then given as input to the final output perceptron and is trained to give the output values of XOR function. 

Finally the weights of the output perceptron, final prediction, accuracy and the classification matrix is printed. 

The Perceptron class models a simple binary classifier:

a. __init__(self, input_size, learning_rate=0.1, epochs=100): Initializes the perceptron with a random set of weights (including the bias) for the given input_size. The learning rate and number of training epochs are set as parameters.

b. activation(self, x): This function defines the activation function. It returns 1 if the input x is greater than or equal to zero, otherwise, it returns 0. This is a step function used to simulate a binary output.

c. predict(self, x): Given an input x, this method adds a bias term (1) and computes the dot product of the weights and input. It then applies the activation function to determine the output (either 0 or 1).

d. train(self, X, y): This function trains the perceptron on the provided input X and corresponding target labels y. It performs updates to the weights based on the perceptron learning rule:

If the actual output is 1 and the predicted output is 0, it adjusts the weights to increase the output.
If the actual output is 0 and the predicted output is 1, it decreases the weights.

e. evaluate(self, X, y): This method evaluates the model by making predictions on X, comparing them to the true labels y, and computing the accuracy as the percentage of correct predictions.
 
