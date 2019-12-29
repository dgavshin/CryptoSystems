from mlib.mprime import *
from binascii import hexlify, unhexlify

def getp(b):
    q = getPrime(b)
    p = q * 2 + 1
    while not fermaTest(p):
        q = getPrime(b)
        p = q * 2 + 1
    return (p)


class generate:

    def __init__(self, b = 1024):
        p = self.p = getp(b)
        g = self.g = randint(2, p - 1)
        x = self.x = randint(2, p - 1)

        while mpow(g, p - 1, p) != 1:
            self.g = randint(1, p-1)
        
        self.y = mpow(g, x, p)

    def decrypt(self, a, b, unhex = False):
        p = self.p
        x = self.x

        m = (mpow(mpow(a, x, p), -1, p) * b) % p
        if unhex:
            return unhexlify(hex(m)[2:]).decode("utf-8")
        return (m)
        
    def encrypt(self, m):
        p = self.p
        y = self.y
        g = self.g
        k = randint(2, p - 1)

        try:
            m = int(m)
        except ValueError:
            m = int(hexlify(m.encode("utf-8")), 16)
        return (mpow(g, k, p), (m * mpow(y, k, p)) % p)
