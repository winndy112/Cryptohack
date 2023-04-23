import numpy as np
v = np.asarray([2,6,3])
w = np.asarray([1,0,0])
u = (7,7,2)
# print(v@w)
#3*(2*v - w)*2
k = 3*(2*v - w)*2
#k * u
re = np.matmul(k,u) # nhân vô hướng vector
print(re)
