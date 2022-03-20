# [Transfer Learning with VGG16 Convolutional Neural Network to Classify Traffic Signs](https://github.com/Amy-Reidy/Portfolio/blob/main/Traffic%20Sign%20Classifier%20with%20Transfer%20Learning%20Project/Poster%20for%20Transfer%20Learning%20Project.pdf)

![image](https://user-images.githubusercontent.com/73396449/157452389-8f33cf8d-4cfe-48ec-9b7b-8495d570ddb4.png)

As vehicles become more autonomous, there is an increasing demand in the automobile industry for driver assistance systems that can identify and classify road signs quickly and accurately. The aim of this project was to create a classifier, using a pre-trained convolutional neural network, that can effectively classify images from the **German Traffic Sign Recognition Benchmark dataset**. 

The convolutional base of the popular **VGG16 model** was used for feature extraction while the top fully connected layers were retrained with the GTSRB dataset and the hyperparameters were fine-tuned to further improve the model. The results show that the best-performing model in this experiment achieved an **accuracy of 82.98%**. As the dataset is quite imbalanced, future work could improve on this result by augmenting the images in the smaller classes to create a more balanced dataset.

The architecture of the best-performing model is shown below.

<img src="https://user-images.githubusercontent.com/73396449/157449841-3084082f-89e6-44d5-b87b-a9fa85a32a8a.png" height="400">
