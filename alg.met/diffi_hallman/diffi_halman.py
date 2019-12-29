from mlib.mprime import *
from base64 import b64encode, b64decode
from hashlib import md5

from Crypto.Util.number import long_to_bytes
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

class generate:
    def getPublicKey(self):
        return (self.A)

    def setPrivateKey(self, B):
        key = long_to_bytes(mpow(B, self.a, self.p))
        self.key = md5(key).digest()

    def encrypt(self, data):
        iv = get_random_bytes(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return b64encode(iv + cipher.encrypt(pad(data.encode('utf-8'), 
            AES.block_size)))

    def decrypt(self, data):
        raw = b64decode(data)
        cipher = AES.new(self.key, AES.MODE_CBC, raw[:AES.block_size])
        return unpad(cipher.decrypt(raw[AES.block_size:]), AES.block_size)


    def __init__(self, publiclen = 300, 
                 secretlen = 1024, 
                 p = -1,
                 g = 7):
        if p == -1:
            self.p = getStrongPrime(secretlen)
        else:
            self.p = p
        self.g = g
        self.a = randbytes(publiclen)
        self.A = mpow(self.g, self.a, self.p)

