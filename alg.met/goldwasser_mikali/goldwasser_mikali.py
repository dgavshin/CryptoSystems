#!/usr/bin/env python3
# -- coding: utf-8 --

from mprime import *
from base64 import b64decode, b64encode
from Crypto.Util.number import bytes_to_long, long_to_bytes


def bits(x):
        while x:
            yield x
            x >>= 1


class Generate:

    def __init__(self, b = None):
        if b is None:
            b = 1024
        self.q, self.p = get_prime(b // 2, "root"), get_prime(b // 2, "root")
        self.n = self.p * self.q
        self.x = self.n - 1

        self.pubkey = (self.n, self.x)
        self.privkey = (self.p, self.q)

    def encrypt(self, m):
        cipher = b""
        m = bytes_to_long(m.encode("utf-8"))
        cipher = []
        for i in bin(m)[2:]:
            y = randint(1, self.n - 1)
            if i == '1':
                cipher.append(mpow(y, 2, self.n) * self.x % self.n)
            else:
                cipher.append(mpow(y, 2, self.n))
        return cipher

    def decrypt(self, c):
        m = "".join(['0' if jacobi(x, self.p) == 1 else '1' for x in c])
        return long_to_bytes(int(m, 2)).decode()

e = Generate()
c = e.encrypt("Very secret message! Be careful")
print (c)
m = e.decrypt(c)
print (m)
