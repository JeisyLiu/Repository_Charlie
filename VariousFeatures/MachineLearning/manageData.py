import numpy
import scipy
import timeit
thelist = ['a', 'b', 'c', 'd']
alpha = numpy.array([0, 1, 2, 3, .4, .5, 'w', 'which'])
bravo = alpha.reshape((2, 4)).copy()
charlie = numpy.sum(2*2)
delta = numpy.genfromtxt("tmp.txt")

echo = numpy.array(thelist)

print ("\nthe alpha:")
print (alpha.reshape(2, 4))
print (echo.reshape((1, 4)))

print ("\nthe bravo:")
print (bravo)
print ("\nthe charlie:")
print (charlie)
print ("the delta")
print (delta)
print ("\nresult of numpy and scipy dot:")
print (numpy.dot is scipy.dot)