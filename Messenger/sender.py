import requests
import datetime

name = input('Введите имя: ')
while True:
    text = input('Введите сообщение: ')
    if text == '/hello': # поздороваться с чат ботом
        print('Привет, это чат бот!')
    elif text == '/myname': # солучить своё имя
        print('выше имя:', name)
    elif text == '/gettime': # посмотреть, сколько времени
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) # копаст с стэковерфлоу
    response = requests.post('http://127.0.0.1:5000/send',
                             json={
                                 'name': name,
                                 'text': text
                             }
                            )
