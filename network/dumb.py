import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

from utility.file_loader import *
from utility.constants import *
from inputs.input_formating import api_calls_proximity_matrix
from elementaire.basic_attributes import parse_elementary_attributes

model = keras.Sequential([
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(2, activation=tf.nn.softmax)
])

model.compile(optimizer=tf.train.AdamOptimizer(),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

files = file_loader()
for file in files:
    records = parse_sequences(file[0])
    data = parse_elementary_attributes(records)
labels = parse_label(LABEL_FILE_NAME)

model.fit(data, labels, 10)