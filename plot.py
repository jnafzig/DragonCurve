import matplotlib.pyplot as plt
import numpy as np

def plot(paths, center=8 + 6j, scale = 2.25, border_width = 0.25, save=False):
    border = np.array([
        border_width*(1+1j),
        border_width*(-1+1j) + 2*center.real,
        border_width*(-1-1j) + 2*center,
        border_width*(+1-1j) + 2*center.imag*1j,
        border_width*(1+1j)])

    fig, ax = plt.subplots(figsize=(16,12))
    ax.set_position([0,0,1,1])
    ax.axis('off')
    for z in paths:
        z = scale*z + center
        line, = ax.plot(z.real,z.imag)

    ax.plot(border.real, border.imag)
    ax.set_xlim([0,16])
    ax.set_ylim([0,12])

    if save:
        plt.savefig('dragon.svg', format='svg')
    else:
        plt.show()

