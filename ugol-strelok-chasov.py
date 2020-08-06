h = int(input()) # hour
m = int(input()) # minut
s = int(input()) # second
if h < 0 or h > 11 or m < 0 or m > 59 or s < 0 or s > 59:
    print('error')
else:
    u = (h * 30 + m * 30 / 60 + s * 30 / 3600)
    print(round(u, 2))
