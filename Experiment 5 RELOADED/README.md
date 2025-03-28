
<h1>Object 5</h1>
<h4> WAP  to  train  and  evaluate  a  convolutional  neural  network  using  Keras  Library  to 
classify  MNIST  fashion  dataset.  Demonstrate  the  effect  of  filter  size,  regularization, 
batch size and optimization algorithm on model performance. </h4>
<hr>

<h3>Description of the model:-</h3>

<p>This model applies convolutional neural network (CNN) architecture designed for the Fashion MNIST dataset. It consists of four convolutional blocks, each containing two Conv2D layers followed by MaxPooling, Dropout, and Batch Normalization to enhance regularization and stability. The number of filters increases from 64 → 128 → 256 → 512 across the blocks, helping the model learn hierarchical features.

After the convolutional layers, the model has a Flatten layer to convert feature maps into a 1D vector, followed by a 512-neuron Dense layer with ReLU activation. The final output layer consists of 10 neurons with a softmax activation for multi-class classification.</p>

<hr>

<h3>Description of the code:-</h3>

The whole code is similar to that used in Experiment 5 except the hyper parameter values and the architecture which has been mentioned in the previous block. 
<hr>
<h3>My Comments :-</h3>

<ul>
<li>The maximum test accuracy achieved is 93.67.</li>
<li>The for loop indicates that the code was meant to run on different combinations of the hyperparameters but contain only the combination which gives best results.<br>
By observing the enormous number of experiments as can also be seen from "Experiment 5", it is apparent that all the remaining hyperparameter combinations are not improving the results keeping in mind that the time comsumed was considerable. So the rest of the combinations were deprecated from the final code which were present in "Experiment 5" to advoid wasting time.
<li> Apart from the visible improvements in the accuracy this model also performs better in avoiding overfitting which was present in models.