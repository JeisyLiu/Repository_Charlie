import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
fig.suptitle('3D coordinate')
fig.savefig('draw3DCoordinate.png')
show()