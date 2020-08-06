import requests
response = requests.get('https://pikabu.ru')
print(response.status_code)
