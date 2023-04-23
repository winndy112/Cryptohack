from Crypto.Util.number import getPrime, inverse, GCD
from Crypto.Util.number import  bytes_to_long as btl
from Crypto.Util.number import long_to_bytes as ltb
n = 742449129124467073921545687640895127535705902454369756401331
e = 3
ct = 39207274348578481322317340648475596807303160111338236677373
flag=b""
p=752708788837165590355094155871
q= 986369682585281993933185289261
d = pow(e, -1, (p-1)*(q-1))
pt = pow(ct, d, n)
flag=ltb(pt)
print(flag)

