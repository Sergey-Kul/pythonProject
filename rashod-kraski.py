import math
a = float(input('введите длину: '))
b = float(input('введите расход краски на кв.м: '))
v = int(input("введите объём банки в литрах: "))

if a < 1 or b < 1 or v < 1:
    print('неверные значения')
else:
    s = (a**2) * 5 # общая площадь бассейна
    r = (b * s) / 1000 # расход в литрах
    b = r / v # кол-во банок
    print('площадь ', s, 'кв.м')
    print('расход ', r, 'литров')
    print("кол-во банок нужно ", math.ceil(b))