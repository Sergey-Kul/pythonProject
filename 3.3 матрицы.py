import numpy as np
import numpy.linalg as alg

a = np.array([[-2, 0, 2.5, 0.3], [-8.5, 2.4, 1.6, -0.4], [-3.4, 0, 2.1, -4.8], [3.5, 8.2, 3, 4.6]])
b = np.array([-1.8, -3.28, -0.5, -2.83])

a_inv = alg.inv(a)
x = a_inv * b

print(np.round(x, 1))
