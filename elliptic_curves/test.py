#!/usr/bin/env python3
# -- coding: utf-8 --

from ECDH import *
from time import sleep
from random import randint
from clint.textui import progress


def menu():
    print()
    print('[1] Encrypt')
    print('[2] Decrypt')
    print('[3] Receive Bob\'s pubkey')
    print('[4] Exit')
    return input()


alice = Generate()
bob = Generate()
hasKey = False

print("Hello Alice!")
while True:
    choice = menu()
    if choice == '1':
        if hasKey:
            m = input('\nPlaintext > ').strip()
            print('\nEncrypted: ' + str(alice.encrypt(m))[2:-1])
        else:
            print("\nFirst, get Bob's key!")

    elif choice == '2':
        if hasKey:
            c = input('\nCipher > ').strip().encode()
            m = alice.decrypt(c)
            print('\nDecrypted: ' + m.decode())
        else:
            print("\nFirst, get Bob's key!")

    elif choice == '3':
        print("Okay, send request to Bob")
        for i in progress.bar(range(randint(6, 10))):
            sleep(.5)
        alice.set_signature(bob.pubkey)
        print("Received an very private key for Bob! Be careful")
        hasKey = True

    elif choice == '4':
        print('Bye!')
        break

    else:
        continue
