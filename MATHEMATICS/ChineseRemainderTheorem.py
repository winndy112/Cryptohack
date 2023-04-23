# Tìm nghịch đảo modulo bằng thuật toán oclid

def gcd_built(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_gcd(b, a % b)
        return gcd, y, x - (a // b) * y

def mod_inverse(num, p):
    g = gcd_built(num, p)
    if g != 1:
        print("Không tìm thấy nghịch đảo của số modulo p.")
    else:
        gcd, x, y = extended_gcd(num, p)
        nghich_dao = x % p
        return nghich_dao


# x ≡ 2 mod 5
# x ≡ 3 mod 11
# x ≡ 5 mod 17
# find a: x = a[mod 5 * 11 * 17]

# Định lý thặng dư Trung Hoa
# Phương trình có nghiệm duy nhất: x = a [mod 5 * 11 * 17]

# Xác định các biến
M = 5 * 11 * 17
p1 = 5
p2 = 11
p3 = 17
a1 = 2
a2 = 3
a3 = 5
M1 = 11 * 17
M2 = 5 * 17
M3 = 5 * 11

# Tính nghịch đảo modulo
y1 = mod_inverse(M1,p1)
y2 = mod_inverse(M2,p2)
y3 = mod_inverse(M3,p3)

flag = (a1*y1*M1 + a2*y2*M2 + a3*y3*M3) % M
print(flag)