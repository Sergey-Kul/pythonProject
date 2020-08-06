import math  # импортируем модуль


# формула длин сторон
def dline(x_0, y_0, x_1, y_1):
    len_line = math.sqrt((x_1 - x_0) ** 2 + (y_1 - y_0) ** 2)
    return len_line


# вводим значения
line_x = input()
line_y = input()
k = int(input())
r = int(input())
count = 0
# присваиваем лист из строк
str_x = line_x.split()
str_y = line_y.split()
# переводим в вещественное число
list_x = [int(x) for x in str_x]
list_y = [int(x) for x in str_y]
# координаты пункта "К"
k_x = list_x[k]
k_y = list_y[k]
# расстояние от К до населенных пунктов
distances = [dline(k_x, k_y, x, y) for x, y in zip(list_x, list_y)]
n = len(distances)
# сколько населенных пункотов попадает под радиус рации
for d in distances:
    if d <= r:
        count = count + 1
print(count)

# 27 53 44 88 35 86 92 20 10 73 81
# 97 22 57 58 37 55 34 29 80 55 71
