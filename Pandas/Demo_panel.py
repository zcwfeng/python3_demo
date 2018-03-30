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


data = np.random.rand(2,4,5)
p = pd.Panel(data)

data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)),
        'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print(p)
print(p['Item1'])
print(p.major_xs(1))
print(p.minor_xs(1))


print(p.axes)
print("is the outher empty?:" , p.empty)
s = pd.Series(np.random.randn(4))
print(s)
print("\nThe dimensions of the object:",s.ndim)
print ("\nThe size of the object:",s.size)
print ("\nThe actual data series is:",s.values)
print ("\nThe first two rows of the data series:",s.head(2))

d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

# Create a DataFrame
df = pd.DataFrame(d)
print("\norigin data :\n",df)
print ("\nThe transpose of the data series is:\n",df.T)


print ("\nRow axis labels and column axis labels are:\n",df.axes)

print ("\nThe data types of each column are:\n",df.dtypes)

print ("\nThe shape of the object is:\n",df.shape)
print ("\nThe total number of elements in our object is:\n",df.size)
print ("\nThe actual data in our data frame is:\n",df.values)


d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}

#Create a DataFrame
df = pd.DataFrame(d)
print(df.sum())
print(df.sum(1))

print(df.mean())

print(df.std())

print(df.describe())

print(df.describe(include=['object']))

print(df. describe(include='all'))
