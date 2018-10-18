import binascii
from Cryptodome import Random
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import AES, PKCS1_v1_5


class EncryptionManager(object):

    def __init__(self, server_info, plain_password):
        self.AES_KEY_SIZE = 32
        self.rsa_public_key = server_info.get('publicKey')
        self.AESSessionKey = self._generate_key()

        # Encrypting sensitive login data
        self.encrypted_session_key = bytes.decode(binascii.hexlify(self.AESSessionKey)).encode('ascii')
        self.encrypted_session_key = self.rsa_encrypt(self.encrypted_session_key)
        self.encrypted_password = self.aes_encrypt(plain_password)

    def aes_encrypt(self, data):
        if isinstance(data, str):
            data = data.encode('utf-8')

        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.AESSessionKey, AES.MODE_CBC, iv)
        data = self._pad_data(data)
        return iv + cipher.encrypt(data)

    def aes_decrypt(self, data):
        if isinstance(data, str):
            data = binascii.unhexlify(data)

        iv = data[:AES.block_size]
        data = data[AES.block_size:]
        cipher = AES.new(self.AESSessionKey, AES.MODE_CBC, iv)
        data = cipher.decrypt(data)
        return self._unpad_data(data)

    def rsa_encrypt(self, data):
        # Construct key using exponent and modulus
        e = int.from_bytes(
            binascii.unhexlify(
                self.rsa_public_key['exponent']),
            byteorder='big',
            signed=False)
        n = int.from_bytes(
            binascii.unhexlify(
                self.rsa_public_key['modulus']),
            byteorder='big',
            signed=False)
        key = RSA.construct((n, e))
        cipher = PKCS1_v1_5.new(key)
        return cipher.encrypt(data)

    def get_encrypted_password(self):
        return {
            'password': bytes.decode(
                binascii.hexlify(self.encrypted_password)), 'key': bytes.decode(
                binascii.hexlify(self.encrypted_session_key))}

    def _generate_key(self):
        return Random.new().read(self.AES_KEY_SIZE)

    def _pad_data(self, data):
        pad_length = AES.block_size - (len(data) % AES.block_size)
        return data + bytes([pad_length]) * pad_length

    def _unpad_data(self, data):
        pad_length = data[-1]
        return data[:-pad_length]
