# encoding:utf-8
from pprint import pprint



from flask import Flask, request, url_for
import config

from flaskr.notice.mail import send_email
from flaskr.weather.caiyun import check_unuaual_weather, realtime

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
            return result
    else:
        return 'get method  no support'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


if __name__ == '__main__':
    app.run()

    # schedule_task()
