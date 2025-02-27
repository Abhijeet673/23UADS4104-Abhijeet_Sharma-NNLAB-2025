<h1>Object 3</h1>
<h4>Program to implement a three-layer neural network using Tensor flow library (only, no
keras) to classify MNIST handwritten digits dataset. Demonstrate the implementation
of feed-forward and back-propagation approaches.</h4>

<h3>Description of the Model </h3>

Implementation of a simple Feedforward Neural Network (FNN) from scratch using only TensorFlow to classify handwritten digits from the MNIST dataset.
This model consists of following three layers :-

<b>a. Input Layer :</b> The input consists of 28×28 grayscale images, which are converted into a vector of size 784 representing each pixel value. 

<b>b. Hidden Layer :</b> A fully connected layer with 128 neurons. This layer uses sigmoid function as an activation function.

<b>c. Output Layer :</b> A fully connected layer with 10 neurons one for each digit class. Uses the Softmax activation function to produce class probabilities.

The loss function used here is Sparse Categorical Crossentropy where the number of epochs are 20 with batch size 32. Adam optimizer is used to update weights.

<h3>Code description  :- </h3>

<b>a. Defining Model Parameters :</b> 

hidden_units: Number of neurons in the hidden layer.

output_size: Number of output classes (digits 0-9, so 10 neurons).

W1 & b1: Weights and biases for the hidden layer.

W2 & b2: Weights and biases for the output layer.

Weights are initialized randomly, and biases are initialized to zero.

<b>b. Defining the Forward Pass</b>

The output of the neural network is calculated here.
The input x is multiplied by W1, added to b1, and passed through a sigmoid activation function.
The hidden layer output is then passed through W2 and b2, and the final layer uses softmax activation to produce class probabilities.

<b>c. Defining Loss Function and Optimizer </b>

Computes the categorical cross-entropy loss, which is used for classification tasks.
Since labels are integers (0-9), sparse categorical crossentropy is used instead of categorical crossentropy.
Uses the Adam optimizer to adjust the weights and biases during training.

<b>d.  Training the Model</b>

The model is trained for 20 epochs.

A batch size of 32 means training is done in mini-batches of 32 samples.

Loop is initialised through 20 epochs of training.
For each batch:
Predictions are computed using forward_pass(x_batch).
After which loss is calculated.

Then gradients of the loss w.r.t. model parameters is calculated.

Finally model parameters are updated using gradient descent.
The loss is captures to track progress.

At the end of each epoch, the average loss is printed and stored in loss_history.

<b>e. Model Evaluation </b>

Predications are made on the test datasets.
Accuracy is calculated by checking how many predictions match the true labels.

<b>f. Plotting the Loss Curve </b>

Loss over epochs is visualised using the loss curve. 

<h3>My Comments</h3>

<ol>
<li>The model may take a lot of time to train (for e.g. more than 3 minutes (for 20 epochs, 32 batch size) on a 6gb vram GPU <i>(Nvidia RTX 4050 laptop GPU)</i>). So requires a decent hardware for better training time. </li>
<br>

<li>Instead of using the sigmoid function as activation function, rectified linear unit (ReLu) function can be used which is comparatively simple and hence improves training time. </li>
<br>
<li>More layer can be added to learn complicated patterns and improve accuracy. </li>
</ol>


