<h1> Object 4 </h1> 
<h4>WAP to evaluate the performance of implemented three-layer neural network with
variations in activation functions, size of hidden layer, learning rate, batch size and
number of epochs.</h4>
<hr>


<h3>Description of the Model </h3>
<p> The model is trained for all the combinations of varying batch size and number of epochs. The batch sizes are : 1,10 & 100 and the number of epochs are 10,50 & 100. Below is the further description of the model. <hr>

<b>Data Preprocessing:</b>

Pixel values are scaled to the range [0, 1].
28x28 images are reshaped to 784-dimensional vectors.
Labels are converted to one-hot vectors for classification.
<hr><br>

<b>Model Architecture:</b>
<ul>
<li>Input Layer: 784 neurons (one for each pixel in the image).</li>
<li>Hidden Layer: 256 neurons with Xavier initialization and ReLU activation.</li>
<li>Output Layer: 10 neurons (one for each digit) with raw logits.</li>
<li>Activation: ReLU for the hidden layer.</li>
</ul><br>
<hr><br>

<b>Loss Function and Optimizer</b> 
<ul>
<li>Loss: Softmax cross-entropy loss is used to compare logits with one-hot encoded labels.</li>
<li>Optimizer: Adam optimizer with a learning rate of 0.1.</li>
</ul><br>
<hr>
<br>
<b>Training Mechanism:</b>
<ul> <li>
Trains over 50 epochs with batches of 10 samples.
Training can be paused and resumed via Ctrl+C (signal handler).
Loss is computed and averaged over each batch, and progress is displayed with a tqdm progress bar.</li>
</ul><br>

<hr><br>
<b>Performance Evaluation:</b>
<ul>
<li>
Accuracy is computed after each epoch using the test set.</li>
<li>Model predictions are compared to true labels to calculate accuracy.</li></ul><br>
<hr><br>
<b>Visualization:</b>
<ul>
<li>Loss Curve: Shows how loss changes over epochs.</li>
<li>Accuracy Curve: Plots accuracy over epochs.</li>
<li>Confusion Matrix: Visualizes classification performance across all 10 digits.</li>
</ul><br>
<hr><br>
<b>Test Accuration and Training time</b>
<ul>
<li>After training, the model's training time and final accuracy is computed on the test set.</li>
</ul><br>
<hr><br>