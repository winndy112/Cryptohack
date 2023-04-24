import numpy as np
v1=[6, 2, -3]
v2=[5, 1, 4]
v3=[2, 7, 1]

numpy_array=np.asarray([v1,v2,v3])
det = np.linalg.det(numpy_array)
print(f"Volume: {abs(det)}")