# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

fig, ax = plt.subplots()

# 从[0, 2*np.pi]以0.01为间隔，形成一个列表
x = np.arange(0, 2*np.pi, 0.01)
# 这里只需要列表的第一个元素，所以就用逗号“,”加空白的形式省略了列表后面的元素
line, = ax.plot(x, np.sin(x))

def animate(i):
    line.set_ydata(np.sin(x + i/100))
    return line,

def init():
    line.set_ydata(np.sin(x))
    # 这里由于仅仅需要列表的第一个参数，所以后面的就直接用空白省略了
    return line,

ani = animation.FuncAnimation(fig=fig,
                              func=animate,  # 动画函数
                              frames=100,   # 帧数
                              init_func=init,  # 初始化函数
                              interval=20,  # 20ms
                              blit=True)

plt.show()
