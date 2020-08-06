import math

import matplotlib.pyplot as plt

def N_t(t):
    N = (C / y) * ((math.pi / 2) - math.atan((T1 - t) / y))
    return N

t = 2000
C = 172
T1 = 2000
y = 45
a = 2017
b = 2020
n = 10
h = (b - a) / (n - 1)

x_list = [a + h * i for i in range(n)]
f_list = [N_t(x) for x in x_list]

lin = plt.plot(x_list, f_list)
plt.setp(lin, color="red", linewidth=2)

plt.gca().spines["left"].set_position("center")

plt.gca().spines["bottom"].set_position("center")

plt.gca().spines["top"].set_visible(False)

plt.gca().spines["right"].set_visible(False)
plt.show()
