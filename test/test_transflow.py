# coding=utf-8
import tensorflow as tf
import numpy as np

def helloworld():
    print('------最简单的hello world')
    hello=tf.constant('hello transflow')
    sess=tf.Session()
    print(sess.run(hello))
    print('------最简单的计数器')
    a=tf.constant(3)
    b=tf.constant(4)
    print(sess.run(a+b))

    one=tf.constant(1)
    x=tf.Variable(0)
    y=tf.add(x,one)
    z=tf.assign(x,y)
    init=tf.global_variables_initializer()

    with tf.Session() as sess:
        sess.run(init)
        for _ in range(3):
            print('y=', sess.run(y),',z=', sess.run(z))


    print('计算器 也可以 同时取回多了操作执行的值 Fetch ')

    with tf.Session() as sess:
        sess.run(init)
        for _ in range(3):
            result = sess.run([y,z])
            print('result',result)






print('------最简单的人工智能应用')
# ------通过训练 得到 y = wx + b 中 权值w 和偏量b的结果
# 使用 NumPy 生成假数据(phony data), 总共 100 个点.
x_data=np.float32(np.random.rand(2,300))
y_data=np.dot([0.100,0.200],x_data) + 0.300
# print('y_data=',y_data)

# 构造一个线性模型
b = tf.Variable(tf.zeros([1]))
w = tf.Variable(tf.random_uniform([1,2],-1.0,1.0))
y = tf.matmul(w,x_data) + b

# print(x_data)
# 最小化方差
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)
print("loss=",loss)
print("train=",train)

# 初始化安装
init= tf.global_variables_initializer()

# 启动图
sess = tf.Session()
sess.run(init)


# 拟合平面
for step in range(0,30):
    sess.run(train)
    if step %2 == 0:
        print(step,sess.run(w),sess.run(b))
