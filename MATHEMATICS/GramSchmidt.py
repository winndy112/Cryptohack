from math import sqrt
# Hàm nhân vector
def dot_product(v1, v2):
    return sum(a*b for a, b in zip(v1, v2)) # tương đương với a in v1 * b in v2

# Hàm tính norm ~ 2
def vector_norm(v):
    return sqrt(dot_product(v, v))

vectors = [[4, 1, 3, -1], [2, 1, -3, 4], [1, 0, -2, 7], [6, 2, 9, -5]]
# Gram smith
def gram_smith(vectors):
    u = []
    for i in range(len(vectors)):
        ui = vectors[i]
        for j in range(i):
            muj = dot_product(vectors[i], u[j]) / vector_norm(u[j])**2
            ui = [ui[k] - muj * u[j][k] for k in range(len(ui))]
        u.append(ui)
    return u

flag = round(gram_smith(vectors)[3][1],5)
print(flag)