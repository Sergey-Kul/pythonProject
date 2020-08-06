# подключить модуль math или импортировать из него все нужные функции
from math import sqrt

x_a = float(input())

y_a = float(input())

x_b = float(input())

y_b = float(input())

x_c = float(input())

y_c = float(input())


# реализовать решение задачи
def compute_area(a_1, a_2, a_3):
    p = (a_1 + a_2 + a_3) / 2
    area = sqrt(p * (p - a_1) * (p - a_2) * (p - a_3))
    return area


def dlina_otrezka(x_0, y_0, x_1, y_1):
    len_line = sqrt((x_1 - x_0) ** 2 + (y_1 - y_0) ** 2)
    return len_line


a = dlina_otrezka(x_b, y_b, x_c, y_c)
b = dlina_otrezka(x_a, y_a, x_c, y_c)
c = dlina_otrezka(x_a, y_a, x_b, y_b)

if a + b <= c or a + c <= b or b + c <= a:
    print('error')
else:
    s = compute_area(a, b, c)
    p = a + b + c
    r = sqrt(((p / 2 - a) * (p / 2 - b) * (p / 2 - c)) / (p / 2))
    R = (a * b * c) / (4 * s)
    Ma = 1 / 2 * sqrt(2 * (c ** 2 + b ** 2) - a ** 2)
    Mb = 1 / 2 * sqrt(2 * (a ** 2 + c ** 2) - b ** 2)
    Mc = 1 / 2 * sqrt(2 * (a ** 2 + b ** 2) - c ** 2)
    M = Ma + Mb + Mc
    # вывести результаты
    print(round(r, 4), round(R, 4), round(M, 4))
