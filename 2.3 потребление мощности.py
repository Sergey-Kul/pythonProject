# потребления за каждый месяц, str
str_p = input()
# месячная норма потребления
n = int(input())
n_1 = 0
# стоимость 1 кВт/ч в пределах нормы а
a = float(input())
# стоимость 1 кВт/ч сверх нормы b
b = float(input())
# в список
lis_p = str_p.split()
list_p = [int(x) for x in lis_p]
# общее потребление
op = sum(list_p)

for x in range(len(list_p)):
    list_p1 = list_p[x]
    if list_p1 <= n:
        norma = list_p1 * a
        n_1 += norma
    else:
        sverh = ((list_p1 - n) * b) + (n * a)
        n_1 = n_1 + sverh
print("Сумма: %6d кВт ч, стоимость %7.2f руб" % (op, n_1))