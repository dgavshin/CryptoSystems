from mlib.mprime import *

class field:
    def __init__(self, p = getPrime(256)):
        self.p = p

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def xy(self):
        return (self.x, self.y)

    def __str__(self):
        return (str(self.xy()))

class ellipticCurve:

    def __init__(self, f = field(), p = [1, 1]):
        assert type(p) == list
        assert type(f) == field
        assert 4 * mpow(p[0], 3, f.p) + 27 * mpow(p[1], 2, f.p) != 0

        self.p = f.p
        self.a = p[0] % self.p
        self.b = p[1] % self.p

    def getPoint(self, x, y):
        return Point(x % self.p, y % self.p)

    def y(self, x):
        if a and b:
            return (mpow(x, 3, p) + self.a * x  + self.b ) % self.p

    def add(self, Q, P):
        assert type(Q) == Point and type(P) == Point
        if Q == P:
            m = ((3 * mpow(Q.x, 2, self.p) + self.a) // (2 * Q.y)) % self.p
        else:
            m = ((P.y - Q.y) // (P.x - Q.x)) % self.p
        x = (mpow(m, 2, self.p) - Q.x - P.x) % self.p
        y = (P.y + m * (x - P.x)) % self.p
        return Point(x, y)

    def bits(self, n):
        while n:
            yield n & 1
            n >>= 1

    def mul(self, n, P):
        result = (0, 0)

        for bit in bits(n):
            if bit == 1:
                result = add(result, P)
            P = add(P, P)
        return result


    
