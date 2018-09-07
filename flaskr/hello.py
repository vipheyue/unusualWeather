# encoding:utf-8
from pprint import pprint

import requests
import schedule
import time
from flask import Flask, request, url_for
import config

from flaskr.WeatherEnum import WeatherEnum
from flaskr.notice.mail import send_email

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


# with app.test_request_context():
#     print(url_for('hello'))
#     print(url_for('hello', username='John Doe'))


def realtime(longitude, latitude):
    url = f'https://api.caiyunapp.com/v2/Kg47BflU7B5pPOGN/{longitude},{latitude}/realtime.json'
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
    realtime_context = f'当前 人体感觉:{desc},雾霾值:{pm25},天气:{WeatherEnum[weather].value} '
    # print(realtime_context)
    return realtime_context
    # pprint(r.json())


def check_unuaual_weather(longitude, latitude):
    url = f'https://api.caiyunapp.com/v2/Kg47BflU7B5pPOGN/{longitude},{latitude}/forecast.json'
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

    if len(rain_list) > 0:
        rain_time_list = []
        for item in rain_list:
            rain_time_list.append(item['datetime'])
        forecast_context = " 接下来的{}个小时内有雨哦,分别是{}".format(len(skycon_scope_list), str(rain_time_list))
        # print(forecast_context)
        realtime_context = realtime(longitude, latitude)
        result = realtime_context + "\n" + forecast_context
        print(result)
        return result
    else:
        return ''


def job():
    # 121.6544,25.1552

    longitude = 116.298056  # 经度
    latitude = 39.959912  # 纬度
    # longitude = 121.6544  # 经度
    # latitude = 25.1552  # 纬度
    # realtime(longitude, latitude)
    result = check_unuaual_weather(longitude, latitude)
    if result != '':
        # 发送邮件
        send_email("vipheyue@foxmail.com", result)
        return result


def schedule_task():
    schedule.every(2).seconds.do(job)
    # schedule.every().day.at("10:37").do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    app.run()
    # schedule_task()
