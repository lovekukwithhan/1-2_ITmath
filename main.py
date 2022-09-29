#0922
#Ex01_ITmath

import numpy as np
a = np.array([4,3,1])
b = np.array([10, 2, -1])

print(np.linalg.norm(a))
print(np.linalg.norm(b))


#distance
print(np.linalg.norm(a-b))
print(np.linalg.norm(b-a))


#magnitude of the angle
#between two vectors
Va = np.array([0, 1])
Vb = np.array([-1, np.sqrt(3)])

#vector internal
Va_dot_Vb = np.dot(Va, Vb)

#vector norm
#cos_theta = a dot b / (||a|| dot ||b||)

Va_mul_Vb = np.linalg.norm(a) * np.linalg.norm(b)
cos_theta = Va_dot_Vb / Va_mul_Vb
theta = np.arccos(cos_theta)
theta_degree = theta / np.pi * 100

print(Va_dot_Vb)
print(Va_mul_Vb)
print(cos_theta)
print(theta)
print(theta_degree)
