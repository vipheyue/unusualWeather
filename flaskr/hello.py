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
    json = r.json()
    desc = json["result"]["comfort"]['desc']
    # print("人体感觉: " + desc)
    pm25 = json["result"]["pm25"]
    # print("PM2.5: " + str(pm25))
    weather = str(json["result"]["skycon"])
    # print("天气: " + WeatherEnum[weather].value)
    wind = json["result"]["wind"]
    # print(wind)
    realtime_context=f'当前时刻天气 -> 人体感觉: {desc} , PM2.5值:{pm25}, 天气: {WeatherEnum[weather].value}'
    print(realtime_context)
    # pprint(r.json())


def forecast():
    url = 'https://api.caiyunapp.com/v2/Kg47BflU7B5pPOGN/121.6544,25.1552/forecast.json'
    r = requests.get(url)
    json = r.json()
    forecast_keypoint = json["result"]["forecast_keypoint"]
    # print(forecast_keypoint)
    # 总天气列表 48个小时
    skycon_list = json["result"]['hourly']["skycon"]
    # 降雨量
    precipitation_list = json["result"]['hourly']["precipitation"]
    # print(precipitation_list)

    skycon_scope_list = skycon_list[:18]
    # print(skycon_list)
    # print(WeatherEnum.RAIN.name)

    # 有雨的时间 item
    rain_list = []
    for item in skycon_scope_list:
        if item['value'] == WeatherEnum.RAIN.name:
            rain_list.append(item)


        # print(item['value'])
    # pprint(r.json())

    if len(rain_list) > 0:
        rain_time_list = []
        for item in rain_list:
            rain_time_list.append(item['datetime'])
            forecast_context="{}  接下来的{}个小时内有雨哦,分别是{}".format(forecast_keypoint,len(skycon_scope_list), str(rain_time_list))
        print(forecast_context)

if __name__ == '__main__':
    # app.run()
    realtime()
    forecast()
