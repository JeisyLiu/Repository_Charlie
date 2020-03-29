import matplotlib as mpl 
import matplotlib.pyplot as plt 
import sklearn.linear_model as skl
import sklearn.model_selection as skm
import pandas as pd
import numpy as np


class LineBuilder:
    def __init__(self, points, line):
        self.times = 0
        self.points = points
        self.line = line
        self.xs = list(points.get_xdata())
        self.ys = list(points.get_ydata())
        self.cid = points.figure.canvas.mpl_connect('button_press_event', self)
        self.reg = skl.LinearRegression()

    def __call__(self, event):
        if self.times < 10:
            print ('click', event)
            if event.inaxes!=self.points.axes: return
            self.xs.append(event.xdata)
            self.ys.append(event.ydata)
            self.points.set_data(self.xs, self.ys)
            self.points.figure.canvas.draw()
            self.times += 1
        else :
            #TODO draw linear regression
            
            X = np.array([self.xs])
            Y = np.array([self.ys])
            X = np.reshape(X, (10, 1))
            Y = np.reshape(Y, (10, 1))
            print (X)
            print (Y)
            
            reg = self.reg.fit(X, Y)
            print ('Linear trained')
            print (reg.predict(X))
            self.line.set_data(X, reg.predict(X))
            self.line.figure.canvas.draw()
            

# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.set_title('click to build points segments')
plt.title('click draw points')
points, = plt.plot([], [], 'go')
line, = plt.plot([], [], 'r')
linebuilder = LineBuilder(points, line)

plt.show()