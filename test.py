# %%
import matplotlib
from matplotlib import pyplot as plt

# Default parameters for plots
matplotlib.rcParams['font.size'] = 20
matplotlib.rcParams['figure.titlesize'] = 20
matplotlib.rcParams['figure.figsize'] = [9, 7]
matplotlib.rcParams['font.family'] = ['STKaiTi']
matplotlib.rcParams['axes.unicode_minus'] = False
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import datasets, layers, optimizers
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
print(tf.__version__)


def preprocess(x, y):
    print('!!!')
    # [b, 28, 28], [b]
    print(x.shape, y.shape)
    x = tf.cast(x, dtype=tf.float32) / 255.
    x = tf.reshape(x, [-1, 28 * 28])
    y = tf.cast(y, dtype=tf.int32)
    # y = tf.one_hot(y, depth=10)

    return x, y


# %%
(x, y), (x_test, y_test) = datasets.mnist.load_data()
x= x[:6]
y= y[:6]

print('x:', x.shape, 'y:', y.shape, 'x test:', x_test.shape, 'y test:', y_test)
# %%
batchsz = 3
train_db = tf.data.Dataset.from_tensor_slices((x, y))
train_db = train_db.shuffle(4)
train_db = train_db.batch(batchsz)
train_db = train_db.map(preprocess)
train_db = train_db.repeat(3)
print(type(train_db))
for i,j in train_db:
    print(j,'@@@@@@@@@')
# %%

test_db = tf.data.Dataset.from_tensor_slices((x_test, y_test))
test_db = test_db.shuffle(1000).batch(batchsz).map(preprocess)

print(next(iter(train_db))[1])
print(next(iter(train_db))[1])
print(next(iter(train_db))[1])
print(next(iter(train_db))[1])



# %%
# def main():
#     # learning rate
#     lr = 1e-2
#     accs, losses = [], []
#
#     # 784 => 512
#     w1, b1 = tf.Variable(tf.random.normal([784, 256], stddev=0.1)), tf.Variable(tf.zeros([256]))
#     # 512 => 256
#     w2, b2 = tf.Variable(tf.random.normal([256, 128], stddev=0.1)), tf.Variable(tf.zeros([128]))
#     # 256 => 10
#     w3, b3 = tf.Variable(tf.random.normal([128, 10], stddev=0.1)), tf.Variable(tf.zeros([10]))
#
#     for step, (x, y) in enumerate(train_db):
#         print(step, ': ', y, '.....')
#
#         # [b, 28, 28] => [b, 784]
#         x = tf.reshape(x, (-1, 784))
#
#         with tf.GradientTape() as tape:
#
#             # layer1.
#             h1 = x @ w1 + b1
#             h1 = tf.nn.relu(h1)
#             # layer2
#             h2 = h1 @ w2 + b2
#             h2 = tf.nn.relu(h2)
#             # output
#             out = h2 @ w3 + b3
#             # out = tf.nn.relu(out)
#
#             # compute loss
#             # [b, 10] - [b, 10]
#             loss = tf.square(y - out)
#             # [b, 10] => scalar
#             loss = tf.reduce_mean(loss)
#
#         grads = tape.gradient(loss, [w1, b1, w2, b2, w3, b3])
#         for p, g in zip([w1, b1, w2, b2, w3, b3], grads):
#             p.assign_sub(lr * g)



if __name__ == '__main__':
    # main()
    pass