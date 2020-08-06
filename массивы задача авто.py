import numpy as np

# ввести список
line_a = input()
line_b = input()
list_a = line_a.split()
list_b = line_b.split()
# переводим в массив
pach = np.array(list_a, dtype=int)
speed = np.array(list_b, dtype=int)
# длина пути
len_path = pach.sum()
# время пути
time = pach / speed
sum_time = time.sum()
# средняя скорость
avg_speed = len_path / sum_time

print("S = %3d км, T = %5.2f час, V = %5.2f км/ч" % (len_path, round(sum_time, 2),
      round(avg_speed, 2)))
