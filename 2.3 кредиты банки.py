# формула дефференцированного расчета выплат
def deff(t, s, n, k):
    p = s / n + (s - (t - 1) * s / n) * (k / (12 * 100))
    return p


# формула аннуитентной выплаты
def ann(s, n, k):
    r = (k / (12 * 100)) * ((1 + (k / (12 * 100))) ** n) / ((1 + (k / (12 * 100))) ** n - 1) * s
    return r


# сумма кредита
s = int(input())
# срок кредита
n = int(input())
# процент
k = float(input())
t = 1
a = 1
h = 1

t_list = [t + a * h for t in range(0, n)]
pay_list = [deff(t, s, n, k) for t in t_list]  # лист вычесленный из дефф функции
pay_ann_list = [ann(s, n, k) for t in t_list]
for t in range(len(t_list)):
    su = (sum(pay_list)) - s  # сумма
    su_ann = (sum(pay_ann_list)) - s
    print("%2d месяц - (диф.) %8.2f руб - (анн.) %8.2f руб"
          % (t_list[t], pay_list[t], pay_ann_list[t]))
print("Доход банка - (диф.) %6.2f руб - (анн.) %6.2f руб" % (su, su_ann))
