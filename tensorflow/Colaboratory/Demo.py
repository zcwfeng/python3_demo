# coding=utf-8
# 矩阵相加
import tensorflow as tf
import numpy as np

# with tf.Session():
#     input1 = tf.constant(1.0,shape=[2,3])
#     input2 = tf.constant(np.reshape(np.arange(1.0, 7.0, dtype=np.float32), (2, 3)))
#     output = tf.add(input1, input2)
#     result = output.eval()
#
# print(result)


import matplotlib.pyplot as plt

x = np.arange(20)
y = [x_i + np.random.randn(1) for x_i in x]
a, b = np.polyfit(x, y, 1)
plt.plot(x, y, 'o', np.arange(20), a*np.arange(20)+b, '-')
plt.show()
