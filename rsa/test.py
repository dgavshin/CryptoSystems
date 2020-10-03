#!/usr/bin/env python3
from RSA import *


def menu():
    print()
    print('[1] Encrypt')
    print('[2] Decrypt')
    print('[3] Secrets')
    print('[4] Exit')
    return input()


rsa = Generate(1024)  # 1024 default

while True:
    choice = menu()

    if choice == '1':
        m = input('\nPlaintext > ').strip()
        print('\nEncrypted: ' + str(rsa.encrypt(m)))

    elif choice == '2':
        c = input('\nCipher > ').strip()
        m = rsa.decrypt(c)
        print('\nDecrypted: ' + m)

    elif choice == '3':
        e, n, q, p, d = rsa.get_parameters()
        print(f"e = {e}\nn = {n}\nq = {q}\np = {p}\nd = {d}")

    elif choice == '4':
        print('Bye!')
        break

    else:
        continue
