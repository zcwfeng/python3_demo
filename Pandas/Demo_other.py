import pandas as pd
import numpy as np


s = pd.Series(list('abc'))
s = s.isin(['a', 'c', 'e'])
print (s)

df = pd.DataFrame(np.random.randn(6, 4), columns=['one', 'two', 'three',
'four'],index=list('abcdef'))

print (df)
print ("=============================================")
print (df.ix[['b', 'c', 'e']])


df = pd.DataFrame(np.random.randn(6, 4), columns=['one', 'two', 'three',
'four'],index=list('abcdef'))
print (df)
print("=============================================")
print (df.reindex(['b', 'c', 'e']))

df = pd.DataFrame(np.random.randn(6, 4), columns=['one', 'two', 'three',
'four'],index=list('abcdef'))

print (df)
print("=====================================")
print (df.ix[[1, 2, 4]])
print("=====================================")
print (df.reindex([1, 2, 4]))
