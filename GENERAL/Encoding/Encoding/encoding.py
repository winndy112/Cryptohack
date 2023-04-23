from pwn import *
import json
from Crypto.Util.number import bytes_to_long, long_to_bytes
import base64
import binascii
import codecs
import sys

def decode(encode_type, encoded_string):
    if encode_type == 'base64':
        return base64.b64decode(encoded_string ).decode('utf-8')
    elif encode_type == 'hex':
        return binascii.unhexlify(encoded_string).decode('utf-8')
    elif encode_type == 'bigint':
        return long_to_bytes(int(encoded_string,16)).decode('utf-8')
    elif encode_type == 'rot13':
        return codecs.encode(encoded_string, 'rot_13')
    elif encode_type == 'utf-8':
        return "".join(chr(i) for i in encoded_string)

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

while True:
    received = json_recv()
    encode_type=received["type"]
    encoded_string=received["encoded"]
    if "flag" in received:
        print("FLAG: %s" % received["flag"])
        sys.exit(0)
    to_send = {
        "decoded": decode(received["type"], received["encoded"])
    }
    json_send(to_send)