import matplotlib.pyplot as plt
from pylab import *
import numpy as np
#figure1
fig=plt.figure()#make the coordinate disappear
fig.suptitle('Figure1')
#figure2
fig,a = plt.subplots(2,2)
fig.savefig('draw2DCoordinate.png')
#show the contain directly
#show()