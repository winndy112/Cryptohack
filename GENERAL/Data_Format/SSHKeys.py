from Crypto.PublicKey import RSA

f = open(r'D:\Cryptohack\GENERAL\Data_Format\bruce_rsa_6e7ecd53b443a97013397b1a1ea30e14.pub', 'r')
pubkey = RSA.import_key(f.read())

print(pubkey.n)
