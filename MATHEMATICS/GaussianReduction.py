import numpy as np
from math import sqrt
def dot_product(v1, v2):
    return sum(a*b for a, b in zip(v1, v2)) # tương đương với a in v1 * b in v2
def vector_norm(v):
    return sqrt(dot_product(v, v))

v = [846835985, 9834798552]
u = [87502093, 123094980]


def gauss_reduction(v1, v2):
    while True:
        if vector_norm(v2) < vector_norm(v1):
            v1, v2 = v2, v1 # swap step
        m = round( dot_product(v1,v2) / dot_product(v1,v1) )
        if m == 0:
            return (v1, v2)
        k = [m * x for x in v1]
        v2 = [x1 - x2 for x1,x2 in zip(v2,k)] # reduction step

basis = gauss_reduction(v,u)

flag = dot_product(basis[0],basis[1])

print(flag)


