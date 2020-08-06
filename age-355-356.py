age = int(input())

if age <= 1582:
    print('error')
elif age % 4 != 0 or (age % 100 == 0 and age % 400 != 0):
    print('365')
else:
    print('366')
