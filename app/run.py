# encoding:utf-8
from pprint import pprint

from flask import Flask, request, url_for
import config

from app.notice.mail import send_email
from app.weather.caiyun import check_unuaual_weather, realtime

app = Flask(__name__)
app.config.from_object(config)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return 'Hello, World!!!!+++'


@app.route('/unusualWeather', methods=['GET', 'POST'])
def unusual_weather():
    if request.method == 'POST':
        longitude = request.form['longitude']
        latitude = request.form['latitude']
        receiverEmail = request.form['receiverEmail']
        result = check_unuaual_weather(longitude, latitude)
        if result != '':
            # 发送邮件
            send_email(receiverEmail, result)
            return str(result)
        return "no unusual weather."
    else:
        return 'get method  no support'


@app.route('/sendMail', methods=['GET', 'POST'])
def send_mail():
    result = send_email("vipheyue@foxmail.com", "邮件测试")
    return str(result)


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


def application(env, start_response):
    str(env)
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World------------------"]

if __name__ == '__main__':
    app.run(host='0.0.0.0')

    # schedule_task()
