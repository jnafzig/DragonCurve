from dragon import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def get_curves(level):
    curves = []
    for i in range(level+1):
        z = dragon(i)
        z = interpolate(smooth(interpolate(z)), num_points=pow(2,level-i))
        curves.append(z)
    return curves
            
def get_func(curves):
    def z(t):
        if t >= len(curves)-1:
            return curves[-1]
        elif t <= 0:
            return curves[0]
        i, t = divmod(t, 1)
        return (1-t)*curves[int(i)] + t*curves[int(i)+1]
    return z

def timesmooth(x, size=19):
    kernel = np.ones(size)/size
    conv = lambda m: np.convolve(kernel, np.pad(m,size//2, mode='edge'), mode='valid')
    return np.apply_along_axis(conv, axis=0, arr=x)

level = 12 
curves = get_curves(level)
curves = [1-curve[::-1].real+curve[::-1].imag*1j for curve in reversed(curves[1:])] + curves[2:]

z = get_func(curves) 

fig, ax = plt.subplots(figsize=(128,72),dpi=10)
ax.set_position([0,0,1,1])
ax.axis('off')
ax.axis('equal')

zval = z(0)
line, = ax.plot(zval.real, zval.imag, 'k', linewidth=24)
ax.set_xlim([-.5,1.5])
ax.set_ylim([-0.4,0.8])

nframes = 3200
#tspace = np.concatenate([np.linspace(0,len(curves)-1,nframes-1,endpoint=False),
#                         np.linspace(len(curves)-1,0,nframes,endpoint=True)])
tspace = 4*(1.2-np.cos(2*np.pi*np.linspace(0,15,nframes)/15))*np.sin(2*np.pi * np.linspace(0,15,nframes)) + float(len(curves)-1)/2

curves = np.array([z(t) for t in tspace])
curves = timesmooth(curves, size=5)


def animate(i):
    zval = curves[i]
    line.set_xdata(zval.real)  # update the data.
    line.set_ydata(zval.imag)  # update the data.
    return line,


ani = animation.FuncAnimation(
    fig, animate, frames=nframes, interval=16 )

#ani.save("dragon.mp4")
plt.show()
