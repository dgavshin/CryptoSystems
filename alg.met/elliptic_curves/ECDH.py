#!/usr/bin/env python3
# -- coding: utf-8 --

from elliptic import *

from hashlib import md5
from base64 import b64decode, b64encode
from Crypto.Util.number import long_to_bytes
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


class Generate:
    def set_signature(self, b):
        key = "".join(map(str, self.E.mul(b, self.privkey).xy())).encode("utf-8")
        self.S = md5(key).digest()

    def encrypt(self, data):
        iv = get_random_bytes(AES.block_size)
        cipher = AES.new(self.S, AES.MODE_CBC, iv)
        return b64encode(iv + cipher.encrypt(pad(data.encode('utf-8'),
                                                 AES.block_size)))

    def decrypt(self, data):
        raw = b64decode(data)
        cipher = AES.new(self.S, AES.MODE_CBC, raw[:AES.block_size])
        return unpad(cipher.decrypt(raw[AES.block_size:]), AES.block_size)

    def make_keypair(self):
        private_key = randint(1, self.n - 1)
        public_key = self.E.mul(private_key, self.G)

        return private_key, public_key

    def __init__(self, parameters=None):
        if parameters is None:
            parameters = OSSL_PARAMS
        self.a = parameters['a']
        self.b = parameters['b']
        self.G = parameters['G']
        self.p = parameters['p']
        self.n = parameters['n']
        self.h = parameters['h']
        self.E = EllipticCurve(Field(self.p, True), [self.a, self.b])
        self.pubkey, self.privkey = self.make_keypair()

