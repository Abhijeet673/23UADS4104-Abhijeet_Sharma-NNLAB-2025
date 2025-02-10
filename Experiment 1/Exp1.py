import numpy as np


class Perceptron:
    def __init__(self, input_size, learning_rate=0.1, epochs=100):
        self.weights = np.random.randn(input_size + 1)  # +1 for bias
        self.learning_rate = learning_rate
        self.epochs = epochs

    def activation(self, x):
        return 1 if x >= 0 else 0

    def predict(self, x):
        x = np.insert(x, 0, 1)  # Add bias term
        return self.activation(np.dot(self.weights, x))

    def train(self, X, y):
        X = np.c_[np.ones((X.shape[0], 1)), X]  # Add bias column
        #converged = False
        #while not converged :
            #converged = True
        for epoch in range(self.epochs):
            for i in range(X.shape[0]):
                y_pred = self.activation(np.dot(self.weights, X[i]))
                if y[i]==1 and y_pred==0:
                    self.weights += self.learning_rate * X[i]
                    #converged = False
                elif y[i]==0 and y_pred==1 :
                    self.weights -= self.learning_rate * X[i]
                    #converged = False
        # yaha xor ke case me convergence kabhi nhi aega toh ye infinitely chalega so applying the epoch condition
        # is better.
    def evaluate(self, X, y):
        correct = 0
        for i in range(len(X)):
            if self.predict(X[i]) == y[i]:
                correct += 1
        return correct / len(X)


# NAND and XOR truth tables
nand_X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
nand_y = np.array([1, 1, 1, 0])  # NAND output

xor_X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
xor_y = np.array([0, 1, 1, 0])  # XOR output

# Train and evaluate Perceptron for NAND
nand_perceptron = Perceptron(input_size=2)
nand_perceptron.train(nand_X, nand_y)
nand_accuracy = nand_perceptron.evaluate(nand_X, nand_y)
print(f"NAND Perceptron Accuracy: {nand_accuracy * 100:.2f}%")

# Train and evaluate Perceptron for XOR
xor_perceptron = Perceptron(input_size=2)
xor_perceptron.train(xor_X, xor_y)
xor_accuracy = xor_perceptron.evaluate(xor_X, xor_y)
print(f"XOR Perceptron Accuracy: {xor_accuracy * 100:.2f}%")
