'''
import os
import bs4
import time
import numpy as np
import scipy
import testb
import server
import pyautogui'''

import timeit
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

points = [(3.28,0.00),(4.00,0.50),(4.40,1.0),(4.60,1.52),(5.00,2.5),(5.00,3.34),(4.70,3.8), (4.50,3.96),(4.20,4.0),(3.70,3.90),(3.00,3.5),(2.00,2.9)]

data = np.array(points)

tck,ss = interpolate.splprep(data.transpose(), s=0)
unew = np.arange(0, 1.01, 0.01)
out = interpolate.splev(unew, tck)

print (unew)
#plt.plot(out[0], out[1], color='r')
plt.plot(data[:,0], data[:,1], 'ob')
#plt.plot(testb.distanceList, testb.sortedpati, 'r')
plt.title("Distance from Wuhan rated to infected number")
plt.xlabel("distance (kilometer)")
plt.ylabel("infected people (person)")
plt.show()