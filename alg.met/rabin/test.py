#!/usr/bin/env python3
from rabin import *


def menu():
    print()
    print('[1] Encrypt')
    print('[2] Decrypt')
    print('[3] Secrets')
    print('[4] Exit')
    return input()


rabin = Generate()  # 1024 default

while True:
    choice = menu()

    if choice == '1':
        m = input('\nPlaintext > ').strip()
        print('\nEncrypted: ' + str(rabin.encrypt(m)))

    elif choice == '2':
        c = input('\nCipher > ').strip()
        m = rabin.decrypt(c)
        print(f'\nDecrypted: {m}')

    elif choice == '3':
        q, p, n = rabin.q, rabin.p, rabin.n
        print(f"n = {n}\nq = {q}\np = {p}")

    elif choice == '4':
        print('Bye!')
        break

    else:
        continue
