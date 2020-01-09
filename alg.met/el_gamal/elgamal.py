#!/usr/bin/env python3
# -- coding: utf-8 --

from binascii import hexlify, unhexlify
from mprime import *


class Generate:

    def __init__(self, b=1024):
        self.p = get_prime(b, "safe")
        self.g = get_primitive_root(self.p, [2, (self.p - 1) // 2])
        self.x = randint(2, self.p - 1)

        self.y = mpow(self.g, self.x, self.p)

    def decrypt(self, a, b, unhex=False):
        p = self.p
        x = self.x

        m = (mpow(mpow(a, x, p), -1, p) * b) % p
        if unhex:
            return unhexlify(hex(m)[2:]).decode("utf-8")
        return m

    def encrypt(self, m):
        p = self.p
        y = self.y
        g = self.g
        k = randint(2, p - 1)

        try:
            m = int(m)
        except ValueError:
            m = int(hexlify(m.encode("utf-8")), 16)
        return mpow(g, k, p), (m * mpow(y, k, p)) % p
