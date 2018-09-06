# encoding:utf-8
from pprint import pprint

import requests



from flask import Flask, request, url_for
import config

from flaskr.WeatherEnum import WeatherEnum

app = Flask(__name__)
app.config.from_object(config)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return 'Hello, World!!!!+++'


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        username = request.form['username']
        return 'Hello, hello post' + username
    else:
        return 'get'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


# with app.test_request_context():
#     print(url_for('hello'))
#     print(url_for('hello', username='John Doe'))


def realtime():
    url = 'https://api.caiyunapp.com/v2/Kg47BflU7B5pPOGN/121.6544,25.1552/realtime.json'
    r = requests.get(url)
    json=r.json()
    desc=json["result"]["comfort"]['desc']
    print("人体感觉: "+desc)
    pm25=json["result"]["pm25"]
    print("PM2.5: "+str(pm25))
    weather=str(json["result"]["skycon"])
    print("天气: "+WeatherEnum[weather].value)
    wind=json["result"]["wind"]
    print(wind)
    # pprint(r.json())



def forecast():
    url = 'https://api.caiyunapp.com/v2/Kg47BflU7B5pPOGN/121.6544,25.1552/forecast.json'
    r = requests.get(url)
    json = r.json()
    forecast_keypoint=json["result"]["forecast_keypoint"]
    print(forecast_keypoint)
    skyconList=json["result"]['hourly']["skycon"]
    print(skyconList)
    print(str(skyconList))

    # pprint(r.json())


if __name__ == '__main__':
    # app.run()
    # realtime()
    forecast()
