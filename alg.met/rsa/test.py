from Crypto.Util.number import *
import RSA

def menu():
    print()
    print('[1] Encrypt')
    print('[2] Decrypt')
    print('[3] Secrets')
    print('[4] Exit')
    return input()

rsa = RSA.generate() # 1024 default

while True:
    choice = menu()

    if choice == '1':
        m = input('\nPlaintext > ').strip()
        print('\nEncrypted: ' + str(rsa.encrypt(m)))

    elif choice == '2':
        c = int(input('\nCiphertext > ').strip())
        m = rsa.decrypt(c)
        print('\nDecrypted: ' + m)

    elif choice == '3':
        print ("e = {a[0]}\nn = {a[1]}\nq = {a[2]}\np = {a[3]}\nd = {a[4]}"
        .format(a = rsa.getParameters()))
        
    elif choice == '4':
        print('Bye!')
        break

    else:
        continue
