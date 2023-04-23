# Đề bài như sau:
# KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
# KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
# FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf

from pwn import *

KEY1 ='a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
key1=bytes.fromhex(KEY1) #decode key1 từ hex thành bytes
mask='37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
mask=bytes.fromhex(mask)

key2=bytearray() 
#tìm key2 
for i in range(len(key1)):
    key2.append(key1[i]^ mask[i])
    #print(hex(key2[i]))


mask2='c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
mask2=bytes.fromhex(mask2)
key3=bytearray()
#tìm key3
for i in range(len(key2)):
    key3.append(key2[i]^mask2[i])
    #print(key3[i])
mask3='04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'
mask3=bytes.fromhex(mask3) 

#tìm flag
flag=bytearray()

for x in range(len(key1)):
    flag.append(key1[x]^key2[x]^key3[x])

for x in range(len(flag)):
    flag[x]=mask3[x]^flag[x]
print("".join(chr(x) for x in flag))