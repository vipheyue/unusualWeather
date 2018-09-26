# encoding:utf-8
import json
from pprint import pprint
import time

from flask import Flask, request, url_for
import requests
from app.notice.mail import send_email
from app.user.user import user_blueprints
from app.weather.weather import weather_blueprints
from app.task.scheduler import scheduler_blueprints


app = Flask(__name__)
app.register_blueprint(user_blueprints, url_prefix='/user')
app.register_blueprint(weather_blueprints, url_prefix='/weather')
app.register_blueprint(scheduler_blueprints, url_prefix='/scheduler')


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    print(" net hello world")
    return 'Hello, World!!!!+++ %s' % time.asctime()




@app.route('/sendMail', methods=['GET', 'POST'])
def send_mail():
    result = send_email("vipheyue@foxmail.com", "邮件测试")
    return str(result)


@app.route('/bridge', methods=['GET', 'POST'])
def bridge():
    url = request.form['url']
    json_string = json.dumps(requests.get(url).json())
    return str(json_string)


if __name__ == '__main__':
    # app.run(host='0.0.0.0')
    app.run(host='0.0.0.0',port=8080)


# export FLASK_ENV=development
# export FLASK_APP=run.py
# flask run  --port=8080
