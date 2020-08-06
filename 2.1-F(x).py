import math
def f_x(x):
    try:
        y = 1 / (x+1) + x / (x-3)
    except:
        y = math.inf
    return y

t = float (input('t = '))
y = f_x(t)
print('f(%4.2f) = %6.3f' % (t, y))

