import matplotlib.pyplot as plt
import numpy as np
import cmath
from dragon import *

def plot_tesselate(z):
   #curves = np.array([z,z-1+1j,z+1+1j,z+1-1j,z-1-1j]).transpose()
   curves = np.array([z]).transpose()
   lines = plt.plot(curves.real,curves.imag)
   return lines

fig, ax = plt.subplots(figsize=(11,8.5),dpi=600)
ax.set_position([0,0,1,1])
ax.axis('off')
ax.axis('equal')

a = smooth(interpolate(dragon(10)))
b = smooth(interpolate(dragon(8)/2))
c = smooth(interpolate(dragon(6)/4))
d = smooth(interpolate(dragon(4)/8))
e = smooth(interpolate(dragon(4)/8))*cmath.exp(-cmath.pi*1j/2)+1/4

plot_tesselate(a)
plot_tesselate(b)
plot_tesselate(c)
plot_tesselate(d)
plot_tesselate(e)

plt.show()
