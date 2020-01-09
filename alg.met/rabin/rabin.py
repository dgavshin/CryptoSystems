#!/usr/bin/env python3
# -- coding: utf-8 --

from mprime import *
from base64 import b64decode, b64encode
from Crypto.Util.number import long_to_bytes, bytes_to_long


class Generate:

    def decrypt(self, c):
        c = b64decode(str(c).encode("utf-8"))
        c = bytes_to_long(c)
        mq = mpow(c, (self.q + 1)//4, self.q)
        mp = mpow(c, (self.p + 1)//4, self.p)

        yp, yq, _ = egcd(self.p, self.q)

        r1 = chinese_remainder([self.n], [yp * self.p * mq + yq * self.q * mp])
        r2 = self.n - r1
        r3 = chinese_remainder([self.n], [yp * self.p * mq - yq * self.q * mp])
        r4 = self.n - r3
        r = [r1, r2, r3, r4]

        return [long_to_bytes(x) for x in r]

    def encrypt(self, m):
        m = bytes_to_long(str(m).encode("utf-8"))
        c = mpow(m, 2, self.n)
        return b64encode(long_to_bytes(c)).decode()

    def __init__(self, b=1024):
        self.p = get_prime(b // 2, "root")
        self.q = get_prime(b // 2 + 1, "root")
        self.n = self.p * self.q

