import numpy
import matplotlib.pyplot as mplp

x1 = numpy.arange(0, 10)
y1 = x1 * 2

k1 = numpy.polyfit(x1, y1, 1) # this is a monomial
print ("the slope and offset:", k1)

#ploting random dropped dots
x = numpy.zeros((20, ))
y = numpy.array([.1, 1, 1.6, 2.5, 3, 4, 5, 6, 10, 12, 15, 20, 40, 100, 300, 500, 1000, 5000, 20000, 90123])
z = numpy.full(20, 1)
for i in numpy.arange(20):
    x[i] = i + 1
    #y[i] = random.randrange(2, 100)
print (x)
print (y)
print(x.__len__())

mplp.plot(x, y, "ob")

#ploting the monomial
k = numpy.polyfit(x, y, 1)

for i in numpy.arange(20):
    z[i] = x[i] * k[0] + k[1]
mplp.plot(x, z, "r")

#ploting the polynomial
k = numpy.polyfit(x, y, 2)
linebravo = numpy.poly1d(k)
print (linebravo)
for i in numpy.arange(20):
    y[i] = linebravo(x[i])
mplp.plot(x, y, "g")

mplp.show()