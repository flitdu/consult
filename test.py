
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import Sequential

layers_num=2  # 堆叠两次
network = Sequential([])
for _ in range(layers_num):
    network.add(layers.Dense(3))
    network.add(layers.ReLU())
network.build(input_shape=(None, 4))
print(network.summary())

"""
 ⭕️     |       |       |
 ⭕️     |       |       |
 ⭕️     |       |       |
 ⭕️     |       |       |
 ⭕️     |       |       |
 ⭕️     |       |       |
 ⭕️     |       |       |
 ⭕️     |       |       |
 ⭕️     |       |       |
 ⭕️     |       |       |
input   


"""


import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, Sequential, losses, optimizers, datasets

# 创建4层全连接
model = keras.Sequential([
    layers.Dense(256, activation='relu'),
    layers.Dense(256, activation='relu'),
    layers.Dense(256, activation='relu'),
    layers.Dense(10, activation='relu'),

])
model.build(input_shape=(4,784))
model.summary()




input_shape = (1, 28, 28, 3)
x = tf.random.normal(input_shape)
y = tf.keras.layers.Conv2D(
    1, 3, input_shape=input_shape)(x)  # filters： 2， kernel_size: 3
