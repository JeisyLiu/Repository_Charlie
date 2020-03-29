import matplotlib.pyplot as plt 
import sklearn.linear_model as sl
import pandas as pd
import numpy as np

###### Draw a Triangle Curve
x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
s = np.sin(x)
c = np.cos(x)
plt.plot(x, s, color = 'blue', label = 'cos')
plt.plot(x, c, color = 'red', label = 'sin')
plt.legend(loc = 'upper_right', frameon = True)
plt.figure(figsize=(10, 9))


# use "plt.annotate()" to set up coordinate marking
ac = plt.gca() #get current access
ac.spines['right'].set_position(("data", 0)) #config spine
ac.spines['top'].set_color('red')

plt.show()