import numpy as np


def get_trend1(x, a):
    y = a[0] * x + a[1]
    return y


def get_trend2(x, a):
    y = a[0] * x ** 2 + a[1] * x + a[2]
    return y


def otn_pogr(y, yr):
    p = abs((yr - y) / y) * 100
    return p


line_x = input()  # координаты по оси OX
line_y = input()  # координаты по оси OY
# список
list_x = line_x.split()
list_y = line_y.split()
# формируем массивы координат
x_array = np.array(list_x, dtype=float)
y_array = np.array(list_y, dtype=float)
# коэфф полинома
k_poly_1 = np.polyfit(x_array, y_array, 1)  # полином для первой степени
k_poly_2 = np.polyfit(x_array, y_array, 2)  # полином для второй степени
# полином 1 степени
x_trend_1 = [get_trend1(x, k_poly_1) for x in x_array]
y_trend_1 = [get_trend1(y, k_poly_1) for y in x_array]
# полином 2 степени
x_trend_2 = [get_trend2(x, k_poly_2) for x in x_array]
y_trend_2 = [get_trend2(y, k_poly_2) for y in x_array]
# средняя ошибка между известными У и трендом
y_avg_1 = otn_pogr(y_trend_1, y_array)
y_avg_2 = otn_pogr(y_trend_2, y_array)
sred_pogr_1 = np.mean(y_avg_1)
sred_pogr_2 = np.mean(y_avg_2)

if sred_pogr_1 < sred_pogr_2:
    print('%5.3f %5.3f' % (k_poly_1[0], k_poly_1[1]))
else:
    print('%5.3f %5.3f %5.3f' % (k_poly_2[0], k_poly_2[1], k_poly_2[2]))
