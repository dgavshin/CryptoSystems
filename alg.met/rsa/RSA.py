from binascii import *
from mlib.mprime import *

def gen(b):
        q,p = getPrime((b // 2) + 1), getPrime(b // 2)
        return (p * q, q, p)

class generate:

    def encrypt(self, m):
        m = int(hexlify(m.encode("utf-8")), 16)
        return mpow(m, self.e, self.n)
    def decrypt(self, c):
        c = mpow(c, self.d, self.n)
        return unhexlify(hex(c)[2:]).decode("utf-8")
    
    def getParameters(self):
        return (self.e, self.n, self.q, self.p, self.d)

    def __init__(self, b = 1024):
        self.e = 65537
        self.n, self.q, self.p = gen(b)
        phi = (self.q - 1) * (self.p - 1)
        self.d = mpow(self.e, -1, phi)
