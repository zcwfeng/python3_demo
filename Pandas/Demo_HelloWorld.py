# https://www.yiibai.com/pandas/python_pandas_quick_start.html
# Pandas处理以下三个数据结构 -
#
# 系列(Series)
# 数据帧(DataFrame)
# 面板(Panel)z
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
print("Hello, Pandas")
s = pd.Series([1,3,5,np.nan,6,8])

print(s)

dates = pd.date_range('20170101', periods=7)
print(dates)

print("--"*16)
df = pd.DataFrame(np.random.randn(7,4), index=dates, columns=list('ABCD'))
print(df)


df2 = pd.DataFrame({ 'A' : 1.,
                     'B' : pd.Timestamp('20170102'),
                     'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                     'D' : np.array([3] * 4,dtype='int32'),
                     'E' : pd.Categorical(["test","train","test","train"]),
                     'F' : 'foo' })

print(df2)


dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df[0:3])

print("========= 指定选择日期 ========")

print(df['20170102':'20170103'])


dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df.loc[dates[5]])



dates = pd.date_range('20170101', periods=7)
df = pd.DataFrame(np.random.randn(7,4), index=dates, columns=list('ABCD'))
print(df.head(10))
print("--------------" * 10)
print(df.tail(3))

print("三维数" * 10)
dates = pd.date_range('20170101', periods=7)
df = pd.DataFrame(np.random.randn(7,4), index=dates, columns=list('ABCD'))
print("index is :" )
print(df.index)
print("columns is :" )
print(df.columns)
print("values is :" )
print(df.values)


print("--统计摘要---" * 10)
dates = pd.date_range('20170101', periods=7)
df = pd.DataFrame(np.random.randn(7,4), index=dates, columns=list('ABCD'))
print(df.describe())

print("--调换数据---" * 10)
dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df.T)

print("--通过轴排序---" * 10)

dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df.sort_index(axis=1, ascending=False))

print("--按值排序---" * 10)

dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df.sort_values(by='B'))

print("--选择一列，产生一个系列---" * 10)
dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df['A'])

print("--选择通过[]操作符，选择切片行---" * 10)

dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df[0:3])

print("========= 指定选择日期 ========")

print(df['20170102':'20170103'])
print("--使用标签获取横截面---" * 10)
dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df.loc[dates[0]])

print("--通过标签选择多轴---" * 10)

dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df.loc[:,['A','B']])
print("--显示标签切片，包括两个端点---" * 10)
dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df.loc['20170102':'20170104',['A','B']])


print("------减少返回对象的尺寸(大小)-------" * 3)

dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df.loc['20170102',['A','B']])
print("------获得标量值，-------" * 3)
dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df.loc[dates[0],'A'])

print("------快速访问标量(等同于先前的方法)-------" * 3)

dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df.at[dates[0],'A'])


print("------通过传递的整数的位置选择-------" * 3)

dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df.iloc[3])


print("------通过整数切-------" * 3)

dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df.iloc[3:5,0:2])
print("------片通过整数位置的列表-------" * 3)

dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df.iloc[[1,2,4],[0,2]])
print("------明确切片行-------" * 3)
dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df.iloc[1:3,:])
dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df.iloc[:,1:3])

print("------要明确获取值-------" * 3)

dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df.iloc[1,1])
print("------要快速访问标量(等同于先前的方法)-------" * 3)
dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df.iat[1,1])
print("------使用单列的值来选择数据-------" * 3)
dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df[df.A > 0])
print("------从满足布尔条件的DataFrame中选择值-------" * 3)
dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df[df > 0])
print("------使用isin()方法进行过滤-------" * 3)
dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

df2 = df.copy()
df2['E'] = ['one', 'one','two','three','four','three']

print(df2)

print("============= start to filter =============== ")

print(df2[df2['E'].isin(['two','four'])])
