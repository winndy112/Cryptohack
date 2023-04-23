import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import long_to_bytes, bytes_to_long

def response(byte_string):
	url = "http://aes.cryptohack.org/ecbcbcwtf/decrypt/"
	url += byte_string.hex()
	url += "/"
	r = requests.get(url)
	js = r.json()
	return bytes.fromhex(js["plaintext"])

def encrypt_flag():
	url = "http://aes.cryptohack.org/ecbcbcwtf/encrypt_flag/"
	r = requests.get(url)
	js = r.json()
	return bytes.fromhex(js["ciphertext"])

def xor(a, b):
	return long_to_bytes(bytes_to_long(a) ^ bytes_to_long(b))
#lấy ciphertext
enc = encrypt_flag()
#chia ciphertext thành các block, trong đó iv là 16 bytes đầu tiên
iv = enc[:16]
block1 = enc[16:32]
block2 = enc[32:]

decrypt_block1 = xor(response(block1), iv) #được plaintext của block1
decrypt_block2 = xor(response(block2), block1) #được plaintext của block2
print(decrypt_block1 + decrypt_block2)