def compute_payment(t, s, n, k):
    p = s / n + (s - (t - 1) * s / n) * (k / (12 * 100))
    return p


s = int(input())  # сумма кредита
n = int(input())  # срок месяцы
k = float(input())  # %
t=1
a=1
h=1
if n <= 0:
    print('ошибка')
else:
    t_list = [t + a * h for t in range(0, n)]
    pay_list = [compute_payment(t, s, n, k) for t in t_list]
    for t in range(len(t_list)):
        su = (sum(pay_list)) - s
        print("%2d месяц - %8.2f руб" % (t_list[t], pay_list[t]))
    print('Доход банка - %6.2f руб' % (su))