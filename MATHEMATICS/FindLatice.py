from Crypto.Util.number import getPrime, inverse, long_to_bytes
import random
import math
from math import sqrt

FLAG = b'crypto{?????????????????????}'





def gen_key():
    q = getPrime(512)
    upper_bound = int(math.sqrt(q // 2))
    lower_bound = int(math.sqrt(q // 4))
    f = random.randint(2, upper_bound)
    while True:
        g = random.randint(lower_bound, upper_bound)
        if math.gcd(f, g) == 1:
            break
    h = (inverse(f, q)*g) % q
    return (q, h), (f, g)


def encrypt(q, h, m):
    assert m < int(math.sqrt(q // 2))
    r = random.randint(2, int(math.sqrt(q // 2)))
    e = (r*h + m) % q
    return e


def decrypt(q, h, f, g, e):
    a = (f*e) % q
    m = (a*inverse(f, g)) % g
    return m


def dot_product(v1, v2):
    return sum(a*b for a, b in zip(v1, v2)) # tương đương với a in v1 * b in v2
def vector_norm(v):
    return sqrt(dot_product(v, v))

# Tìm cơ sở có n2-norm nhỏ
def gauss_reduction(v1, v2):
    while True:
        if vector_norm(v2) < vector_norm(v1):
            v1, v2 = v2, v1 #đổi chỗ
        m = round( dot_product(v1,v2) / dot_product(v1,v1) )
        if m == 0:
            return (v1, v2)
        k = [m * x for x in v1]
        v2 = [x1 - x2 for x1,x2 in zip(v2,k)] # Bước giảm


public, private = gen_key()
q, h = 7638232120454925879231554234011842347641017888219021175304217358715878636183252433454896490677496516149889316745664606749499241420160898019203925115292257, 2163268902194560093843693572170199707501787797497998463462129592239973581462651622978282637513865274199374452805292639586264791317439029535926401109074800

# fh = g[q]

v1 = [1,h]
v2 = [0,q]
basis = gauss_reduction(v1,v2)


# Suy ra
f, g = basis[0][0], basis[0][1] # có thể vector còn lại
e = 5605696495253720664142881956908624307570671858477482119657436163663663844731169035682344974286379049123733356009125671924280312532755241162267269123486523

flag = long_to_bytes(decrypt(q,h,f,g,e))

print(flag)


