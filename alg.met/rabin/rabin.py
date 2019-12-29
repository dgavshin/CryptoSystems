from mlib.mprime import *
from math import sqrt

class generate:
    def decrypt(self, c):
        a = None
    
    def encrypt(self, m):
        c = mpow(m, 2, self.n)

    class __init__(self, b):
        self.q, self.p = getpq(b)
        self.n = self.p * self.q

def getpq(b):
    q, p = getPrime(b // 2), getPrime((b // 2) + 1)
    while q % 4 != 3 or p % 4 != 3:
        q, p = getPrime(b // 2), getPrime((b // 2) + 1)
    return (q, p)

    