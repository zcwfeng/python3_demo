import pandas as pd
import numpy as np

data = np.random.rand(2,4,5)
p = pd.Panel(data)


data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)),
        'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)



# 2.2 从DataFrame对象的dict创建面板
# creating an empty panel

data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)),
        'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
# p = pd.Panel()

print(p)
