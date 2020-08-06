k = int(input())
if k < 1 or k > 99:
    print('ошибка')
elif k == 11 or k==12 or k== 13 or k==14:
    print(k,'рублей')
else:
    if k % 10 == 1:
        print(k, 'рубль')
    elif 2 <= k % 10 <= 4:
        print(k, 'рубля')
    else:
        print(k, 'рублей')
