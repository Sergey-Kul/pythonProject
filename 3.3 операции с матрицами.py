import numpy as np

n = int(input())  # ко-во вершин многоугольника
points = []  # список вершин многоугольника
for i in range(n):
    line = input()
    array_str = line.split()
    points.append(array_str)
a = np.array(points, dtype=int)  # массив из вершин
angle = int(input())  # угол поворота в градусах
yg = (angle / 180) * np.pi  # переводим градусы в радианы
rotate = np.array([[np.cos(yg), np.sin(yg)],
                   [-np.sin(yg), np.cos(yg)]])  # матрица поворота вокруг центра координат
pov = np.dot(a, rotate)  # координаты вершин после поворота

avg_x = np.mean(pov, 0)[0]
avg_y = np.mean(pov, 0)[1]
print("avg_x = %6.2f, avg_y=%6.2f" % (avg_x, avg_y))
