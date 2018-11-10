import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

from utility.file_loader import parse_label
from utility.constants import *

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(3561, 3561)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(2, activation=tf.nn.softmax)
])

model.compile(optimizer=tf.train.AdamOptimizer(),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
matrix = ()
labels = parse_label(LABEL_FILE_NAME)

model.fit(matrix, labels, 10)