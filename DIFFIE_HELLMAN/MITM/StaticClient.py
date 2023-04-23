from pwn import *
import json 
from Crypto.Util.number import getPrime
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib

def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)
    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')

io = remote('socket.cryptohack.org', 13373)
alice = json.loads(io.recvline().strip().decode().split("e: ")[1])

p = int(alice['p'], 16)
g = int(alice['g'], 16)
A = int(alice['A'], 16)

bob = json.loads(io.recvline().strip().decode().split("b: ")[1])
B = int(bob['B'], 16) 

ct = json.loads(io.recvline().strip().decode().split("e: ")[1])
iv = ct['iv']
enc_flag = ct['encrypted']

send_bob = dict()
q = getPrime(15)
n = q ** 200

send_bob['p'] = hex(n)
send_bob['g'] = hex(g)
send_bob['A'] = hex(g)

io.sendline(json.dumps(send_bob).encode())
bob_secret = json.loads(io.recvline().strip().decode().split("u: ")[1])
bob_encrypted = json.loads(io.recvline().strip().decode().split("u: ")[1])
bob_encrypted_iv = bob_encrypted['iv']
bob_encrypted_sth = bob_encrypted['encrypted']

bob_secret = int(bob_secret['B'], 16)
F = Zmod(n)
g = F(g)
bob_secret = F(bob_secret)
b = discrete_log(bob_secret, g)
shared_secret = pow(A, b, p)
print(decrypt_flag(shared_secret, iv, enc_flag))