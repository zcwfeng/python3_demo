import matplotlib.pyplot as plt

figure = plt.figure()
axes1 = figure.add_subplot(2,1,1)
axes2 = figure.add_subplot(2,1,1)

axes1.plot([1,3,5,7],[4,9,6,8])
axes2.plot([1,2,4,5],[8,4,6,2])


plt.show()
# figure.show() 本来可以单独显示，但是有一个问题，没查到