# p = [3.4 0.7 2.0 0.4 2.5 2.6 1.7 0.2 4.0 2.5] - строка
# z = [6.4 8.3 6.8 6.7 7.4 6.4 8.9 4.7 5.3 7.6] - СТРОКА
# строка
line0 = input('введите значения температур в 0 часов: ')
# строка
line12 = input('вводите значения температур в 12 часов: ')
# средняя темп-ра
k = float(input('средняя тем-ра: '))
str_line0 = line0.split()  # лист
str_line12 = line12.split()  # лист

list_line0 = [float(x) for x in str_line0]  # перевели в вещесвенное число
list_line12 = [float(x) for x in str_line12]  # перевели в вещественное число

avg_line = [(x + y) / 2.0 for x, y in zip(list_line0, list_line12)]  # средннее значение темп-р


for i in range(len(avg_line)):
    t = avg_line[i]
    if t > k:
        print(i)
