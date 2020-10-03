#!/usr/bin/env python3
# -- coding: utf-8 --

from mprime import *
from math import log
from array import array
from base64 import b64decode, b64encode
from Crypto.Util.number import bytes_to_long, long_to_bytes
import bbs

class Generate:

    def __init__(self, b = 1024):
        self.rand = bbs.Generator(b)
        self.n = self.rand.n
        self.p = self.rand.p
        self.q = self.rand.q

        #self.h = round(log(log(self.n, 2), 2))
        self.h = 1
        self.mask = (2 ** self.h) - 1

    def unsplit(self, m):
        m = "".join([bin(x)[2:] for x in m])
        return long_to_bytes(int(m, 2)).decode()

    def split(self, m):
        blocks = []
        while m:
            blocks.insert(0, m & self.mask)
            m >>= self.h
        return blocks

    def decrypt(self, c, x):
        t = len(c)
        dp = mpow((self.p + 1) // 4, t + 1, self.p - 1)
        dq = mpow((self.q + 1) // 4, t + 1, self.q - 1)

        up = mpow(x, dp, self.p)
        uq = mpow(x, dq, self.q)

        rp, rq, d = egcd(self.p, self.q)
        assert d == 1

        x0 = (uq * rp * self.p + up * rq * self.q) % self.n

        self.rand.state = x0
        gamma = []
        for i in range(0, t):
            xi = self.rand.get_next()
            gamma.append(xi & self.mask)
        mes = [a ^ b for a, b in zip(gamma, cipher)]
        return self.unsplit(mes)

    def encrypt(self, m):

        blocks = self.split(bytes_to_long(m.encode("utf-8")))
        cipher = []
        gamma = []
        for block in blocks:
            p = self.rand.get_next() & self.mask
            cipher.append(p ^ block)
            gamma.append(p)
        x = self.rand.get_next()
        return cipher, x

m = "privet!"
print (f"[/] I will encrypt message = {m}")
print ("[+] Encrypting...")
a = Generate()
cipher, x = a.encrypt(m)
print(cipher)
mes = a.decrypt(cipher, x)
print ("[+] Decrypting... ")
print (mes == "privet!")
print (f"Yeah! {mes} == {m}")
