import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(12, 8))
ax = Axes3D(fig)

# 生成X，Y
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X,Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)

# height value
Z = np.sin(R)

# 绘图
# rstride（row）和cstride(column)表示的是行列的跨度
ax.plot_surface(X, Y, Z, 
                rstride=1,  # 行的跨度
                cstride=1,  # 列的跨度
                cmap=plt.get_cmap('rainbow')  # 颜色映射样式设置
               )

# offset 表示距离zdir的轴距离
ax.contourf(X, Y, Z, zdir='z', offest=-2, cmap='rainbow')
ax.set_zlim(-2, 2)

plt.show()
