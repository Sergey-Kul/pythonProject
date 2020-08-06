from math import sqrt

a = float(input())
h = float(input())

if a <= 0 or h <= 0:
    print('error')
else:
    v = (a ** 2 * h) / (4 * sqrt(3))
    s = ((a ** 2 * sqrt(3)) / 4) + ((3 * a / 2) * (sqrt(h ** 2 + a ** 2 / 12)))
    print(round(v, 3), round(s, 3))
