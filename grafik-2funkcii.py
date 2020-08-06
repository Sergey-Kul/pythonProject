import matplotlib.pyplot as plt
import math


def f_x(x):
    y = (math.exp(math.cos(x))) + math.log(math.sin(0.8 * x) ** 2 + 1) * math.cos(x)

    return y


def y_x(x):
    y = - math.log((math.cos(x) + math.sin(x)) ** 2 + 1.7) + 2

    return y


a = -2

b = 6

n = 100

h = (b - a) / (n - 1)

x_list = [a + h * i for i in range(n)]

f_list = [f_x(x) for x in x_list]

y_list = [y_x(x) for x in x_list]

line_f = plt.plot(x_list, f_list, label='f(x)')

line_y = plt.plot(x_list, y_list, label='y(x)')
plt.setp(line_f, color="blue", linewidth=2)

plt.setp(line_y, color="red", linewidth=2)

plt.gca().spines["left"].set_position("zero")

plt.gca().spines["bottom"].set_position("zero")

plt.gca().spines["top"].set_visible(False)

plt.gca().spines["right"].set_visible(False)

plt.legend()

plt.title("Графики функций")

plt.show()
