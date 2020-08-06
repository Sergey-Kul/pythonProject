# импортируем библиотеки
import requests
import datetime
# адреса на которые будет посылаться запрос
addresses = ["https://ntsk.ru"]


def request(address, count):  # функция по запросу адреса
    print(f'{count} кол-во запросов по адресу', address)
    print("Начинаем: ", datetime.datetime.now())
    for i in range(count):
        time = datetime.datetime.now()
        response = requests.get(address)
        time = datetime.datetime.now() - time
        print(str(i).ljust(5), response.status_code, time)
    print('закончили в: ', datetime.datetime.now())


for address in addresses:
    request(address, 1000) # получаем запрос от сайтов
