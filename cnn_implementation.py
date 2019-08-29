# -*- coding: utf-8 -*-
"""CNN implementation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nDMd8XvDgad0rxEJ0soWG-pPCFm9-VQm
"""

from keras.layers import *

from keras.models import Sequential

model =Sequential()

# CNN model
model.add(Conv2D(32,(3,3),activation='relu',input_shape=(28,28,1)))
model.add(MaxPool2D((2,2)))
model.add(Conv2D(64,(3,3),activation='relu'))
model.add(MaxPool2D((2,2)))
model.add(Conv2D(64,(3,3),activation='relu'))
model.add(Flatten())
model.add(Dense(64,activation='relu'))
model.add(Dense(10,activation='softmax'))
model.summary()

from keras.datasets import mnist
from keras.utils import to_categorical
(x_train,y_train),(x_test,y_test)=mnist.load_data()

def preprocess_data(x,y):
  x=x.reshape((-1,28,28,1))
  x=x/255.0
  y=to_categorical(y)
  return x,y

x_test,y_test=preprocess_data(x_test,y_test)
print(x_test.shape,y_test.shape)

x_train,y_train=preprocess_data(x_train,y_train)
print(x_train.shape,y_train.shape)

model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])

hist=model.fit(x_train,y_train,epochs=10,validation_split=0.1,batch_size=128)

output=model.predict(x_test)

import numpy as np

print(np.argmax(output[3]),np.argmax(y_test[3]))

