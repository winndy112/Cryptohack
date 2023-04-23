# `from Crypto.PublicKey import RSA` is importing the RSA module from the Crypto library. This module
# provides functionality for generating, importing, and exporting RSA keys and for encrypting and
# decrypting data using RSA.
from Crypto.PublicKey import RSA
key = RSA.importKey(open(r'D:\Cryptohack\GENERAL\Data_Format\2048b-rsa-example-cert_3220bd92e30015fe4fbeb84a755e7ca5.der', 'rb').read())
print(key.n)

