#!/usr/bin/env python3
# -- coding: utf-8 --

from random import randint
from functools import reduce

''' 
    Prime tests
'''


def simple_test(a):
    if 0 < a < 3:
        return True
    if a % 2 == 0:
        return False

    for i in range(3, 256 if a > 256 else a - 1, 2):
        if a % i == 0:
            return False
    return True


def ferma_test(x):
    if x == 2:
        return True
    for i in range(100):
        a = randint(2, x - 1)
        if (gcd(a, x)) != 1:
            return False
        if mpow(a, x - 1, x) != 1:
            return False
    return True


def miller_rabin_test(n):
    rounds = 32
    s = 0
    t = n - 1
    while t & 1:
        s += 1
        t >>= 1
    for _ in range(rounds):
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


''' Chinese remainder'''


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mpow(p, -1, n_i) * p
    return sum % prod


''' Fast pow'''


def mpow(a, m, n):
    res = 1

    ''' Inverse mode '''
    if m == -1:
        x, y, g = egcd(a, n)
        assert g == 1
        return x

    ''' Pow mode '''
    while m >= 1:
        if m & 1:
            res = res * a % n
        a = (a ** 2) % n
        m >>= 1
    return res


''' GCD, EGCD '''


def egcd(a, b):
    if not b:
        return 1, 0, a
    y, x, g = egcd(b, a % b)
    return x, y - (a // b) * x, g


def gcd(a, b):
    if not b:
        return a
    return gcd(b, a % b)


def rand_bytes(b):
    return randint(2 ** (b - 1), (2 ** b) - 1)


''' Get probable prime  Safe --> (p - 1)//2 is prime
                        Root --> p == 3 (mod 4)'''


def get_safe_prime(b):
    p = get_prime(b)
    q = (p - 1) // 2
    while not simple_test(q) or not miller_rabin_test(q):
        p += 2
        q = (p - 1) // 2
    return p


def quad_prime(b):
    q = get_prime(b)
    while q % 4 != 3:
        q = get_prime(b)
    return q


def get_prime(b, t=None):
    if t == "root":
        return quad_prime(b)
    elif t == "safe":
        return get_safe_prime(b)
    n = rand_bytes(b)
    while not simple_test(n) or not miller_rabin_test(n):
        if n % 2 == 0:
            n += 1
        n += 2
    return n


def f(x, n): return (x * x + 1) % n


def factorize(N, prime_only=False, func=f):
    factors = []
    prime_factors = set()

    while N > 1:
        if ferma_test(N):
            factors.append(N)
            prime_factors.add(N)
            break
        x = 2
        y = 1
        i = 0
        stage = 2
        g = gcd(N, abs(x - y))
        while g == 1:
            if i == stage:
                y = x
                stage = stage * 2
            x = func(x, N)
            i += 1
            g = gcd(N, abs(x - y))
        factors.append(g)
        if simple_test(g):
            prime_factors.add(g)
        N //= g
    if prime_only:
        return prime_factors
    return factors


''' Get primitive root '''


def get_primitive_root(n, factors=None):
    if factors is None:
        factors = factorize(n, prime_only=True)
    g = randint(2, n - 1)
    for q in factors:
        if mpow(g, (n - 1) // q, n) == 1:
            return get_primitive_root(n, factors)
    return g


def jacobi(n, k):
    assert k > 0 and k % 2 == 1
    n = n % k
    t = 1

    while n != 0:
        while n % 2 == 0:
            n //= 2
            r = k % 8
            if r == 3 or r == 5:
                t = -t
        n, k = k, n
        if n % 4 == 3 and k % 4 == 3:
            t = -t
        n = n % k

    if k == 1:
        return t
    else:
        return 0
