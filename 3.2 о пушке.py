import numpy as np


def get_trend(x, a):
    y = a[0] * x ** 2 + a[1] * x + a[2]
    return y


line_x = input()  # координаты движения снаряда по оси OX
line_y = input()  # координаты движения снаряда по оси OY
k_x = float(input())  # координаты мишени по оси ОХ
k_y = float(input())  # координаты мишени по оси OY

# список
list_x = line_x.split()
list_y = line_y.split()

# формируем массивы координат движения снаряда. помни что координаты с плавающей точкой
x_array = np.array(list_x, dtype=float)
y_array = np.array(list_y, dtype=float)

# линия движения
a = np.polyfit(x_array, y_array, 2)

# вычисляем высоту на которой находится пушка
h_zero = get_trend(0, a)

# где находится мишень
h_target = get_trend(k_x, a)

# вычисляем попадает ли снаряд в мишень
delta_h = abs(k_y - h_target)
if delta_h <= 0.5:
    print("h0 = %6.2f, yes" % h_zero)
else:
    print("h0 = %6.2f, no" % h_zero)

