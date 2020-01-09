#!/usr/bin/env python3
# -- coding: utf-8 --

import random
from mprime import *
from Crypto.Util.number import long_to_bytes, bytes_to_long

class Generator:

    def make_keypair(self, b):
        p = get_prime(b // 2, "root")
        q = get_prime(b // 2 + 1, "root")
        return p * q, p, q

    def __init__(self, b = 1024):
        assert b > 0

        self.n, self.p, self.q = self.make_keypair(b)

        self.seed = random.randint(1, self.n)
        self.state = mpow(self.seed, 2, self.n)

    def get_next(self):
        result = 0
        self.state = pow(self.state, 2, self.n)
        return self.state


