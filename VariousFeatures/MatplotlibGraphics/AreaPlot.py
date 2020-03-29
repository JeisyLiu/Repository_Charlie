import numpy as np
import matplotlib.pyplot as plt

year_n_1 = [1.5, 3, 10, 13, 22, 36, 30, 33, 24.5, 15, 6.5, 1.2]
year_n = [2, 7, 14, 17, 20, 27, 30, 38, 25, 18, 6, 1]

plt.fill_between(np.arange(12), year_n_1, color="lightpink",
                 alpha=0.5, label='year N-1')
plt.fill_between(np.arange(12), year_n, color="skyblue",
                 alpha=0.5, label='year N')

plt.legend()
plt.show()