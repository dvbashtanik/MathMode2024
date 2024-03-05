# save this as app.py
import time
from pydantic import BaseModel, Field

import flask
from flask import Flask, abort

app = Flask(__name__)
db = []
for i in range(3):
    db.append({
        'name': 'Anton',
        'time': 12343,
        'text': 'text01923097'
    })

@app.route("/")
def hello():
    return "Hello, World!"

class MessINFO(BaseModel):
    name: str = Field(min_length=1)
    text: str

@app.route("/send", methods= ['POST'])
def send_message():
    '''
    функция для отправки нового сообщения пользователем
    :return:
    '''
    # TODO
    # проверить, является ли присланное пользователем правильным json-объектом
    # проверить, есть ли там имя и текст
    # Добавить сообщение в базу данных db
    data = flask.request.json

    data = MessINFO(**data)

    text = data.text
    name = data.name

    message = {
        'text': text,
        'name': name,
        'time': time.time()
    }
    db.append(message)
    return {'ok': True}

@app.route("/messages")
def get_messages():
    try:
        after = float(flask.request.args['after'])
    except:
        abort(400)
    db_after = []
    for message in db:
        if message['time'] > after:
            db_after.append(message)
    return {'messages': db_after}

@app.route("/status")
def print_status():
    users = []
    for i in db:
        users.append(i['name'])
    return flask.render_template('status.html', users=len(set(users)), messages=len(db))

@app.route('/index')
def lionel(): 
    return flask.render_template('index.html')


app.run()