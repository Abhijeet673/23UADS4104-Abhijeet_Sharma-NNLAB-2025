<h1>Object 7</h1>
<h4>  WAP to retrain a pretrained imagenet model to classify a medical image dataset.  </h4>
<hr>



<h3>My Comments</h3>
<ol><li>The architecture referred from the OpenAI ChatGPT was giving around 72% test accuracy.</li>
<li>On modifying the classifier portion of the architecture there was not much improvement in the model accuracy (~1%).</li>
<li>However the significant improvement in the accuracy is observed when the output from the last convolutional block (from layer 24 to 30) is unfreezed and included in the training process.</li>  
<li>The prospect of changing the dropout rate and exploring batch normalisation for improving the test accuracy has not been extensively explored and there might be a possibility of finding even a better architecture by thinking in this direction. 
</ol>









