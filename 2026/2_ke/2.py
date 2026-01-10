from itertools import *
from itertools import product


xyzw = product((0,1), repeat=4)
print ('x y z w')

for x,y,z,w in xyzw:
    if ((w==z) or (not(y <= w) or (not x))) == 0:
        print(z,w,x,y)

