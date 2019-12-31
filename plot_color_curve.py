import matplotlib.pyplot as plt
import matplotlib as mp
import numpy as np
import cmath
from dragon import *

cmap = mp.cm.get_cmap('viridis')

def plot(z):
   curves = np.array([z]).transpose()
   c = np.linspace(0,1, len(curves))
   colors = cmap(c)
   print(colors)
   lines = plt.scatter(curves.real,curves.imag, c=colors, marker=None,linewidth=.02)
   return lines

fig, ax = plt.subplots(figsize=(11,8.5),dpi=600)
ax.set_position([0,0,1,1])
ax.axis('off')
ax.axis('equal')

a = smooth(interpolate(dragon(10)))

plot(a)

plt.show()
