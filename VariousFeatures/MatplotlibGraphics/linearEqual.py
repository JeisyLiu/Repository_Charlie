import numpy
from matplotlib import pyplot as plt

x = numpy.arange(1, 11)
y = 2 * x + 5
plt.title("grahpic demo")
plt.xlabel("x axis value")
plt.ylabel("y axis value")
plt.plot(x, y, "or")
#plt.plot(x, y) # draw a strate line
plt.bar(x, y)
plt.show()