from keras.datasets import mnist
import numpy as np
from functions import *
import matplotlib.pyplot as plt


# (x_train, y_train), (x_test, y_test) = mnist.load_data()
#
# x_train = x_train.reshape(60000, 784) # 2次元配列を1次元に変換
# x_test = x_test.reshape(10000, 784)
# x_train = x_train.astype('float32')   # int型をfloat32型に変換
# x_test = x_test.astype('float32')

data = np.linspace(-100, 100, 10000)

a = relu(data)


plt.plot(data, a)
plt.xlim(-10, 10)
plt.ylim(-0.5, 1.5)
plt.show()
