# BearBot

**BearBot** is a web application that allows a user to interact with a bot, providing information and identifying different types of bears.

We used a Convoltional Neural Net with the model summary as follows. The Model can be found [here](https://colab.research.google.com/drive/1bEDJMK19cd0RJ4m3J6FHoq6uZCYqTvZN?usp=sharing)

Model: "sequential_1"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
sequential (Sequential)      (None, 159, 159, 3)       0         
_________________________________________________________________
rescaling (Rescaling)        (None, 159, 159, 3)       0         
_________________________________________________________________
conv2d (Conv2D)              (None, 159, 159, 16)      448       
_________________________________________________________________
max_pooling2d (MaxPooling2D) (None, 79, 79, 16)        0         
_________________________________________________________________
conv2d_1 (Conv2D)            (None, 79, 79, 32)        4640      
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 39, 39, 32)        0         
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 39, 39, 64)        18496     
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 19, 19, 64)        0         
_________________________________________________________________
flatten (Flatten)            (None, 23104)             0         
_________________________________________________________________
dense (Dense)                (None, 256)               5914880   
_________________________________________________________________
dense_1 (Dense)              (None, 4)                 1028      
=================================================================
Total params: 5,939,492
Trainable params: 5,939,492
Non-trainable params: 0
_________________________________________________________________
 
Technologies used: HTML, CSS, RASA, Gatsby, Amazon AWS cloud, Python and Convolutional Neural Networks

# Video Walkthrough

Here's a walkthrough of the application:

<img src='https://github.com/Xxyumi-hub/BearBot/blob/master/Gif3.gif' title='Video Walkthrough' width='' alt='Gif Video Walkthrough of the application' />
