import numpy as np

def f1(z):
    return (1+1j)*z/2

def f2(z):
    return 1-(1-1j)*z/2

def dragon(level):
    if level == 0:
        return np.array([0,1])
    else:
        curve = dragon(level - 1)
        return np.array([f1(x) for x in curve] + [f2(x) for x in reversed(curve[:-1])])

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
