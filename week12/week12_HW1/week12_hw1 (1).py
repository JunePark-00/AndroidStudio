# -*- coding: utf-8 -*-
"""week12-HW1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pVvRbhQQABIOpuTi3XO9uoIODOvmdrpe
"""

import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.layers import Dense
from keras.models import Sequential

from keras.datasets import mnist
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()
print("Training data shape : ", X_train.shape)
print("Training label shape : ", Y_train.shape)
print("Testing data shape : ", X_test.shape)
print("Testing label shape : ", Y_test.shape)

X_train = X_train.reshape(60000, 28*28).astype('float32')/255.0
X_test = X_test.reshape(10000, 28*28).astype('float32')/255.0
Y_train = keras.utils.to_categorical(Y_train, 10)
Y_test = keras.utils.to_categorical(Y_test, 10)

model = Sequential()
model.add(Dense(units=256, input_dim=(28*28), activation='relu'))
model.add(Dense(units=128 , activation='relu'))
model.add(Dense(units=64 , activation='relu'))
model.add(Dense(units=32 , activation='relu'))
model.add(Dense(units=10, activation='softmax'))
model.summary()

model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['accuracy'])

history = model.fit(X_train, Y_train, batch_size=100, epochs=30, validation_split=0.3)

loss, accuracy = model.evaluate(X_test, Y_test)
print(f"Test loss: {loss:.3}")
print(f"Test accuracy: {accuracy:.3}")

import matplotlib.pyplot as plt
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['training', 'validation'], loc='best')
plt.show()

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['training', 'validation'], loc='best')
plt.show()