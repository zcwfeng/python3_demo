
import pickle
import os
import os.path
test_data = ['Save me!', 123.456, True]

f = open('test.data', 'w')
pickle.dump(test_data, f.buffer)
f.close()


f2 = open('test.data')
data = f2.read()
print(data)
f2.close()
