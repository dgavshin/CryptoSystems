from math import log10, sqrt
from random import randint

def simpleTest(a):
    a = int(a)
    if a > 0 and a < 3:
        return True
    if a % 2 == 0:
        return False

    for i in range(3, 256 if a > 256 else a - 1, 2): # in range [1; 256] or [3; a]
        if a % i == 0:
            return False
    return True

def MillerRabinTest(n):
    rounds = int(log10(n))
    s = 0
    t = n - 1
    while t & 1:
        s += 1
        t >>= 1
    for _ in range(min(rounds, n - 2)):
        a = randint(2, n - 2)
        x = mpow(a, t, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = mpow(x, 2, n)
            if x == 1:
                return False
            else:
                break
        if x != n - 1:
            return False
    return True

def mpow(a, m, n):
    res = 1
    while m >= 1:
        if m & 1:
            res = res * a % n
        a = (a * a) % n
        m >>= 1
    return res

def gcd(a, b):
    if not b:
        return (1, 0, a)
    y, x, g = gcd(b, a % b)
    return (x, y - (a // b) * x, g)

def randbytes(b):
    return randint(2 ** (b - 1), (2 ** b) - 1)

def getPrime(b):
    n = randbytes(b)
    while not simpleTest(n) or not MillerRabinTest(n):
        n = randbytes(b)
    return (n)

def factorize(N, primeOnly=False):
    f = lambda x, n: (x * x + 1) % n
    factors = []
    primeFactors = set()
    
    while N > 1:
        if fermaTest(N):
            factors.append(N)
            primeFactors.add(N)
            break
        x = 2
        y = 1
        i = 0
        stage = 2
        g = gcd(N, abs(x - y))[2]
        while (g == 1):
            if (i == stage):
                y = x
                stage = stage * 2
            x = f(x,N)
            i += 1
            g = gcd(N, abs(x - y))[2]
        factors.append(g)
        if simpleTest(g):
            primeFactors.add(g)
        N //= g
    if primeOnly:
        return primeFactors
    return factors

def fermaTest(x):
    if x == 2:
        return True
    for i in range (100):
        a = randint(2, x - 1)
        if (gcd(a, x)[2]) != 1:
            return False
        if (mpow(a, x - 1, x) != 1):
            return False
    return True

def phi(x):
    l = 0
    delimeters = set()
    if fermaTest(x):
        return (x - 1)
    for f in factorize(x, 1):
        for i in range(f, x, f):
            delimeters.add(i)
    return (x - len(delimeters) - 1)


def getPrimitiveRoot(x):
    a = factorize(getPrime(300) - 1,1)

