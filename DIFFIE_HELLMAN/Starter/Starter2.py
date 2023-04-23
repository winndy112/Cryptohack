def order(g, p):
    for n in range(2,p):
        if pow(g, n, p)==g:
            return n
    return p           

p=28151
for g in range(2, p):
    o=order(g,p)
    if o==p:
        print(f"{g=} if a flag")
        break
