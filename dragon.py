import numpy as np

def f1(z):
    return (1+1j)*z/2

def f2(z):
    return 1-(1-1j)*z/2

def area(z):
    z = np.array(z)
    return sum(z.imag*np.roll(z.real,1) - z.real*np.roll(z.imag,1))

def remove_repeated(z):
    c = []
    i = 0
    while i < len(z):
        n = np.where(z[i+1:] == z[i])
        if len(n[0]) > 0 and area(z[i:i+n[0][0]+2]) == 0:
            i += n[0][0] + 1
        else:
            c.append(z[i])
            i += 1
    return np.array(c)

def shift(z):
    i = z.index(1)
    return z[i:] + z[:i] + [1]

def dragon(level, initial=np.array([0,1])):
    if level == 0:
        return initial 
    else:
        curve = dragon(level-1, initial=initial) 
        #reverse = reversed(curve[:-1])
        reverse = curve
        curve = [f1(x) for x in curve] + [f2(x) for x in reverse]
        curve = shift(curve)
        return np.array(curve)

def interpolate(x, num_points=19):
    return np.concatenate([np.linspace(x1, x2, num_points, endpoint=False) 
            for x1, x2 in zip(x[:-1], x[1:])] + [np.array([x[-1]])])

def smooth(x, size=19):
    kernel = np.ones(size)/size
    return np.convolve(kernel, np.pad(x,size//2, mode='edge'), mode='valid')

if __name__=='__main__':
    import matplotlib.pyplot as plt
    import argparse

    parser = argparse.ArgumentParser(description="draw a dragon curve")
    parser.add_argument('level', type=int, help='dragon curve level')
    args = parser.parse_args()
    level = args.level

    z = dragon(level)

    z = smooth(interpolate(z))

    fig, ax = plt.subplots(figsize=(11,8.5),dpi=600)
    ax.set_position([0,0,1,1])
    ax.axis('off')
    ax.axis('equal')
    line, = ax.plot(z.real,z.imag,'k')
    line.set_linewidth(1)
    print(ax.get_xlim())
    print(ax.get_ylim())
    plt.show()
