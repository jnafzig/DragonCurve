
from dragon import dragon, smooth, interpolate, remove_repeated
import numpy as np
from fractions import Fraction
from plot import plot

initial = np.array([1, 1/2+1j/2, 0, 1/2-1j/2, 1])
level = 6

z = dragon(level, initial=initial)
z = remove_repeated(z)

#c = dragon(level)
#c = c[:len(c)//2+1]
#c = remove_repeated(c)
#c = smooth(interpolate(c))


class Point(complex):
    def _fraction(self):
        return (Fraction(self.real).limit_denominator(),
            Fraction(self.imag).limit_denominator())

    def __eq__(self, other):
        return self._fraction() == other._fraction()
    
    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash(self._fraction())


paths = []
for i in range(4):
    for j in range(-2,3):
        for k in range(-1,2):
            paths.append(np.exp(np.pi*1j*i/2)*z + j*1 + k*1j)

np.save('paths', paths)

index = {}

for path in paths:
    for p, q in zip(path[:-1], path[1:]):
        p = Point(p)
        q = Point(q)
        frozen_segment = frozenset((p,q))
        seglist0 = index.get(p, [])
        seglist1 = index.get(q, [])
        if frozen_segment not in seglist0:
            index[p] = seglist0 + [frozen_segment]
        if frozen_segment not in seglist1:
            index[q] = seglist1 + [frozen_segment]

paths = []

while len(index):
    p = None
    for point, seglist in index.items():
        if len(seglist) == 3:
            p = point
            break
    if not p:
        for point, seglist in index.items():
            if len(seglist) == 1:
                p = point
                break
            
    path = [complex(p.real,p.imag)]
    
    while p in index:
        pseglist = index.pop(p)
        seg = np.random.choice(pseglist)
    
        q = (set(seg) - set([p])).pop()
        qseglist = index.pop(q)
    
        pseglist.remove(seg)
        qseglist.remove(seg)
    
        if len(pseglist):
            index[p] = pseglist
        if len(qseglist):
            index[q] = qseglist
    
        path.append(complex(q.real,q.imag))
        p = q
    paths.append(np.array(path))

plot(paths, save=True)


