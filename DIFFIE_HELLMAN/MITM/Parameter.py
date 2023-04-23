{"iv": "faf349748682cf47fd2d4ef463eb470a", "encrypted_flag": "eaa84d09be6ed47b6041b41b06fdea6023e9df768139b7db9d5567b226e38eb1"}
from Crypto.Util.Padding import unpad
from Crypto.Cipher import AES
from hashlib import sha1
from math import sqrt, ceil
def inverse_modulo(base, exponent, mod):
    return pow(base, -exponent, mod)

def decrypt_flag(shared_secret, iv, ciphertext):
    key = sha1(str(shared_secret).encode()).digest()[:16]
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    plaintext = AES.new(key, AES.MODE_CBC, iv).decrypt(ciphertext)
    return unpad(plaintext, 16).decode()

g= 2
p= int(0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff)
A= int(0xa7d7f19236ca2bed9702bc21e73d7aa9a9bef717bc3933d798b6240d4723455c49e1f54f764ed615fcaaeac428a5100159a19ead301317bd59f3d17760dd0ec984cddb0b7059c8b4c7ad7b5719c8d1cc99378ba0df845a72ecdb2152f8801d59013f6e8a2bb9e104606d0079a2fd07c0e63bfb1479a6e8d350145efff807a5a82d54099dda068f8007c055f1007bcd6a856746bdb21bb65cc6f6c3b308b7182d27eee1c4ca0fea588e0111a6b96464da1f2325b7ef6b228a834e7a9cad1e49dd)
B= int(0x660eb508d07c064d8a47d193365acc963e3fb73e3175d342e557d2b9e4ee895097cd635882bf4fbf5e8471dc6dbb80724236c487287d2d91c296dda5f95c945d3b4117c588816506040b475fab7fe4ee6fffea6b6ad6e566ce203b4c88d39fbe0d27bd9715869693bb9adc2ee8bd70f28f44b8b046179730a9c477e81974a796d8eacaf8d85661af3c7b1f371bb3639cab91c1b8242d13751d6460fd6ab1dad31f7196c1e46565bee8077e002a083102a0e7a4a7b3bd73f68031be9139151937)
log_g_B = inverse_modulo(g, B, p)
b = log_g_B % (p-1)
shared_secret = pow(A, b, p)
iv = "faf349748682cf47fd2d4ef463eb470a"
ciphertext = "eaa84d09be6ed47b6041b41b06fdea6023e9df768139b7db9d5567b226e38eb1"
print(decrypt_flag(shared_secret, iv, ciphertext))
print(shared_secret)