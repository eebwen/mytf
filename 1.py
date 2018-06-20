# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 17:25:55 2018

@author: xxz
"""

import numpy as np
import matplotlib.pyplot as plt

def get_y(x):
    return x + 10 * np.sin(5 * x) + 7 * np.cos(4*x)

x = np.arange(0, 9, 0.005)
#y = np.exp(-x/2.) * np.sin(2*np.pi*x)
y = get_y(x)



fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y)
#ax.set_xlim(0, 10)
#ax.set_ylim(-1, 1)


x1 = np.arange(0, 9, 0.5)
ax.plot(x1, get_y(x1), 'go')
#ax.plot(x1, get_y(x1), 'go')
#ax.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 'go')
plt.show()
