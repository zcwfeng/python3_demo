# coding=utf-8
import numpy as np
# array
a = [1,2,3,4]
b = np.array(a)


array_one = np.ones([10, 10])
array_zero = np.zeros([10, 10])
random1 = np.random.rand(10,10)
random2 = np.random.uniform(0,100)
random3 = np.random.randint(0,100)

def test(arr) :
    print(b.size)
    print(b.shape)
    print(b.ndim)
    print(b.dtype)


test(array_zero)

test(random1)


# 正态生成4行5列的二维数组
arr = np.random.normal(1.75, 0.1, (4, 5))
print(arr)
# 截取第1至2行的第2至3列(从第0行算起)
after_arr = arr[1:3, 2:4]
print(after_arr)
