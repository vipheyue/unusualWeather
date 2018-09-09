import requests
from app.WeatherEnum import WeatherEnum

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
        return str(result)
    else:
        return ''

