import numpy as np

# ввод значений строк
line_a = input()  # длина дороги
line_b = input()  # средние скорости
k = int(input())  # номер участка, на котором автомобиль въехал на дорогу
p = int(input())  # номер участка, после которого выехал
# списки
list_a = line_a.split()[k:p+1]
list_b = line_b.split()[k:p+1]
# переводим в массив
pach = np.array(list_a, dtype=int)
speed = np.array(list_b, dtype=int)
# время пути
time = pach / speed
sum_time = time.sum()
# длина пути
len_path = pach.sum()
# средняя скорость
avg_speed = len_path / sum_time

print("S = %3d км, T = %5.2f час, V = %5.2f км/ч" % (len_path, sum_time, avg_speed))
