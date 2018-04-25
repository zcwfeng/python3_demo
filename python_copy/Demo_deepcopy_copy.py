import copy
# d = {
#     'name' : ['An','Assan']
# }
# c = d.copy()
# dc = copy.deepcopy(d)
# d['name'] = ['an']
# print(c)
# print(d)
# print(dc)


d = {
    'name' : ['An','Assan']
}
c = d.copy()
dc = copy.deepcopy(d)
d['name'].append('shu')
print(c)
print(d)
print(dc)


seq = [1,2,3]
seq1 = seq
seq2 = copy.copy(seq)
seq3 = copy.deepcopy(seq)
seq.append(4)
seq2[2] = 5
print(seq,seq1,seq2,seq3)

import math
math.sa
