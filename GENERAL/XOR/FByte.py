from pwn import xor
bytes_string= bytearray.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')
bytes=0x00
for i in range(256):
    flag=xor(bytes_string, bytes).decode("utf-8")
    if("crypto" in flag):
        print(flag)
        break
    bytes+=0x01