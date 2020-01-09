#!/usr/bin/env python3
# -- coding: utf-8 --

from mprime import *


class Field:
    def __init__(self, p=None, trust=False):
        if p is None:
            p = get_prime(256)
        else:
            if not trust:
                if not miller_rabin_test(p):
                    raise ValueError(f"{p} is a not prime")
        self.p = p

    def elements(self):
        for i in range(self.p):
            yield i


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def xy(self):
        return self.x, self.y

    def __str__(self):
        return str(self.xy())


class EllipticCurve:

    def __init__(self, field, params=None):
        if params is None:
            params = [1, 1]

        self.p = field.p
        self.a, self.b = params[0], params[1]
        self.zero = None

        if self.a == 0 and self.b == 0:
            raise ValueError("Singular curve, a = b = 0")
        if 4 * mpow(self.a, 3, self.p) + 27 * mpow(self.b, 2, self.p) % self.p == 0:
            raise ValueError("Singular curve, discriminant is zero")

    def is_on_curve(self, point):
        if point is None:
            return True
        if mpow(point.y, 2, self.p) == \
                (mpow(point.x, 3, self.p) + self.a * point.x + self.b) % self.p:
            return 1
        else:
            raise TypeError(f"Coordinates [{point.x}, {point.y}] do not define a point on Elliptic Curve")

    def get_point(self, x, y):
        point = Point(x % self.p, y % self.p)
        assert self.is_on_curve(point)
        return Point(x % self.p, y % self.p)

    def inverse(self, q):
        assert self.is_on_curve(q)
        return q.x, -q.y % self.p

    def add(self, q, z):
        assert self.is_on_curve(q)
        assert self.is_on_curve(z)

        if q is None:
            return z
        if z is None:
            return q

        if q.x == z.x and q.y != z.y:
            return self.zero

        if q.xy() == z.xy():
            m = ((3 * mpow(q.x, 2, self.p) + self.a) * mpow(2 * q.y, -1, self.p)) % self.p
        else:
            m = ((z.y - q.y) * mpow(z.x - q.x, -1, self.p)) % self.p
        x = (mpow(m, 2, self.p) - q.x - z.x) % self.p
        y = (z.y + m * (x - z.x)) % self.p

        r = Point(x, -y % self.p)
        assert self.is_on_curve(r)

        return r

    def mul(self, n, p):
        assert self.is_on_curve(p)

        result = None
        if n == 0:
            return None
        elif n < 0:
            p = self.inverse(p)
        while n:
            if n & 1:
                result = self.add(result, p)
            p = self.add(p, p)
            n >>= 1

        assert self.is_on_curve(result)
        return result

    def __repr__(self):
        return str(f"Elliptic Curve defined by y^2 = x^3 + "
                   f"{self.a}*x + {self.b} over Finite Field of size = {self.p}")


OSSL_PARAMS = {
    'G': Point(0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798,
               0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8),
    'p': 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f,
    'n': 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141,
    'a': 0,
    'b': 7,
    'h': 1
}

OSSL_CURVE = EllipticCurve(Field(OSSL_PARAMS['p']), [OSSL_PARAMS['a'], OSSL_PARAMS['b']])
