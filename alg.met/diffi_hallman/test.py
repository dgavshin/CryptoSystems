import diffi_halman
from time import sleep
from random import randint
from clint.textui import progress

def menu():
    print()
    print('[1] Encrypt')
    print('[2] Decrypt')
    print('[3] Receive Bob\'s publickey')
    print('[4] Exit')
    return input()

alice = diffi_halman.generate(300, 1024) # 1024 default
bob = diffi_halman.generate(300, None, alice.p, alice.g)
hasKey = False

print("Hello Alice!")
exit()
while True:
    choice = menu()
    if choice == '1':
        if hasKey:
            m = input('\nPlaintext > ').strip()
            print('\nEncrypted: ' + str(alice.encrypt(m))[2:-1])
        else:
            print("\nFirst get Bob's key!")

    elif choice == '2':
        if hasKey:
            c = input('\nCiphertext > ').strip().encode()
            m = alice.decrypt(c)
            print('\nDecrypted: ' + m.decode())
        else:
            print("\nFirst get Bob's key!")

    elif choice == '3':
        print("Okey, sended requests to Bob")
        for i in progress.bar(range(randint(6, 10))):
            sleep(.5)
        alice.setPrivateKey(bob.A)
        print("Received an very private key for Bob! Be careful")
        hasKey = True
        
    elif choice == '4':
        print('Bye!')
        break

    else:
        continue