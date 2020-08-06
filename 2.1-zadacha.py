import math


# вычислить численность населения для года t по формуле
def compute_population(t):
    N = (C / y) * ((math.pi / 2) - math.atan((T1 - t) / y))
    return N


C = 172
T1 = 2000
y = 45

# ввести строку с перечисленными через пробел годами
line = input()
years_str_list = line.split()  # преобразовать строку в список из строковых значений годов
n = len(years_str_list)  # вычислить количество элементов в списке

# сформировать список years_list на основе years_str_list,преобразовав строковые значения в целые
years_list = [float(t) for t in years_str_list]

for t in years_list:
    population_list = compute_population(t)

    print("%5d - %6.3f миллиард(ов)" % (t, population_list))
# 1220 2369 2636 1032 2657 198 1118
