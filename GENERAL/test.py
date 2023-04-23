data="0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
#tìm độ dài của data
data_bytes=bytes.fromhex(data)
# cnt=0
# for x in data_bytes:
#      cnt+=1
# print(cnt) 
# #tìm secret key
# res="crypto{"
# res_bytes=bytearray()
# for i in res:
#     res_bytes.append(ord(i))
# for x in range(len(res_bytes)):
#     print(chr(data_bytes[x]^res_bytes[x]))

# #số byte của data_bytes là 42 => lặp lại 6 lần key để được độ dài key lớn hơn data
# #decode các kí tự trong key thành từng bytes
# # và lưu trong biến hex_str
# key="myXORkeymyXORkeymyXORkeymyXORkeymyXORkeymyXORkey"
# hex_str=""
# for x in key:
#     hex_str = "".join([hex(ord(c))[2:] for c in key]) 
# hex_str=bytes.fromhex(hex_str)
# #tìm flag bằng cách xor từng bytes trong hex_tr với từng byte của data
# flag=""
# for i in range(len(data_bytes)):
#     flag+=chr(hex_str[i]^data_bytes[i])
# print(flag)
#print(pow(209, -1, 991))
def order(g, p): 
  #thử n từ 2 đến p.
    for n in range(2, p): 
        if pow(g, n, p) == g:
            return n
    return p

p = 28151
#thử g từ 2 đến p. 
for g in range(2,p):
    o = order(g, p)
    #do tìm g nhỏ nhất nên khi vừa tìm thấy g thì dừng chương trình.
    if o == p:
        print(f"{g=} is a flag")
        break