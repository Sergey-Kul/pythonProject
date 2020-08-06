import math  # импортируем математич


# функция популяции
def compute_population(t):
    N = (C / y) * ((math.pi / 2) - math.atan((T1 - t) / y))
    return N


# константы для функции
C = 172
T1 = 2000
y = 45
# список годов
years0 = [1000, 1750, 1800, 1850, 1900, 1950, 1955,
         1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995,
         2000, 2005, 2010, 2011, 2012, 2013, 2014, 2015,
         2016, 2017, 2018, 2019]
# список популяции
population0 = [0.400, 0.791, 1.000, 1.262, 1.650, 2.519,
              2.756, 3.021, 3.335, 3.692, 4.068, 4.435, 4.831,
              5.264, 5.674, 6.071, 6.344, 6.933, 7.015, 7.100,
              7.162, 7.271, 7.358, 7.444, 7.530, 7.669, 7.763]
# ввести границы среза
a = int(input())
b = int(input())
# сделать срез
years = years0[a:b+1]
population = population0[a:b+1]
# вывели расчётный лист популяции
population_list = [compute_population(t) for t in years]
# относительная погрешность
error_list = [abs(population_list[i] - population[i]) / population[i]
              for i in range(len(years))]
# минимальная погрешность
min_error = min(error_list)
index_min_error = error_list.index(min_error)
# максимальная погрешность
max_error = max(error_list)
index_max_error = error_list.index(max_error)
# средняя погрешность
avg_error = sum(error_list) / len(population_list)
# выводим в продакшн
print("Погрешность - минимальная, год: %4d, максимальная, год: %4d, средняя, процент: %6.3f"
      % (years[index_min_error], years[index_max_error], (avg_error * 100)))
