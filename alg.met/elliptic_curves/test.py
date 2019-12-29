from elliptic import *

E = ellipticCurve(field(71), [-3, 2])
a = E.getPoint(2, 3)
b = E.getPoint(1, 1)

print (E.add(a, b))
