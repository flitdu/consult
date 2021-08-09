
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


class MyDense(layers.Layer): # 自定义网络层
    def __init__(self, inp_dim, outp_dim):
        super(MyDense, self).__init__()