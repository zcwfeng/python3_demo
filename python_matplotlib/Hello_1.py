import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

# 排除警告信息
import warnings

from displayfunction import display

warnings.filterwarnings("ignore")

# 打印版本信息
# display(np.__version__)
# display(pd.__version__)
# display(mpl.__version__)

print(np.__version__)
print(pd.__version__)
print(mpl.__version__)

# matplotlib画图常见参数设置
mpl.rcParams["font.family"] = "SimHei"# 设置字体
mpl.rcParams["axes.unicode_minus"]=False# 用来正常显示负号
plt.rcParams['font.sans-serif']=['SimHei'] # 用来正常显示中文标签

# 嵌入式显示图形

# %matplotlib作用
#
# 是在使用jupyter notebook 或者 jupyter qtconsole的时候，才会经常用到%matplotlib，
# 也就是说那一份代码可能就是别人使用jupyter notebook 或者 jupyter qtconsole进行编辑的。
#
# 关于jupyter notebook是什么，可以参考这个链接：[Jupyter Notebook介绍、安装及使用教程][1]
# 而%matplotlib具体作用是当你调用matplotlib.pyplot的绘图函数plot()进行绘图的时候，或者生成一个figure画布的时候，
# 可以直接在你的python console里面生成图像。



# %matplotlib inline
plt.show()