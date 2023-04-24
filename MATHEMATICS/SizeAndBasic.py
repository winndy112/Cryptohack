from math import sqrt
def dot_product(v1,v2):
    return sum(a*b for a,b in zip(v1,v2))
def vector_norm(v):
    return sqrt(dot_product(v,v))
v = (4, 6, 2, 5)
print(vector_norm(v))