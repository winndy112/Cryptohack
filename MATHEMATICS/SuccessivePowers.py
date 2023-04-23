from sympy import mod_inverse

t = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]


start = max(t) + 1
end = 1000
re = []
Stop = False
for p in range(start,end):
    try:
        x = [(t[i + 1] * mod_inverse(t[i],p)) % p for i in range(len(t) - 1)]
        if len(set(x)) == 1:
            print(p,x[0])
            break
    except:
        continue


