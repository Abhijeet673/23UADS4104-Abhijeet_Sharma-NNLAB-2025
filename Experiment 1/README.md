Experiment 1 - WAP to implement the Perceptron Learning Algorithm using numpy in Python. Evaluate performance of a single perceptron for NAND and XOR truth tables as input dataset.

The Python program implements the Perceptron Learning Algorithm using NumPy and evaluates the performance of a single perceptron on 
NAND and XOR truth tables as input datasets.

First, the truth tables for NAND and XOR are created using NumPy. The perceptron is then trained separately for both Boolean functions, 
and its accuracy is evaluated accordingly.

The weight updates occur within the train method of the Perceptron class, where the Perceptron Learning Algorithm is applied using a for loop. 
The loop iterates for a fixed number of epochs instead of running until convergence. This approach is chosen because the XOR function
is not linearly separable, which would otherwise lead to an infinite loop if a convergence condition were applied.

For training, we set the learning rate to 0.1 to ensure effective updates to the weights.


