#!/usr/bin/env python3
# -- coding: utf-8 --

from base64 import b64decode, b64encode
from Crypto.Util.number import bytes_to_long, long_to_bytes
from binascii import *
from mprime import *


class Generate:

    def make_keypair(self, b):
        q, p = get_prime((b // 2) + 1), get_prime(b // 2)
        return p * q, q, p

    def encrypt(self, m):
        m = bytes_to_long(str(m).encode("utf-8"))
        c = long_to_bytes(mpow(m, self.e, self.n))
        return b64encode(c).decode()

    def decrypt(self, c):
        c = b64decode(str(c).encode("utf-8"))
        c = bytes_to_long(c)
        c = mpow(c, self.d, self.n)
        return long_to_bytes(c).decode("utf-8")

    def get_parameters(self):
        return self.e, self.n, self.q, self.p, self.d

    def __init__(self, b=1024):
        self.e = 65537
        self.n, self.q, self.p = self.make_keypair(b)
        phi = (self.q - 1) * (self.p - 1)
        self.d = mpow(self.e, -1, phi) % phi


