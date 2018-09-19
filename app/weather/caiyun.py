from pprint import pprint

import requests
from pip._internal.utils.deprecation import deprecated

from app.WeatherEnum import WeatherEnum
from app.weather.weather_bean import WeatherBean
import datetime


def realtime(longitude, latitude):
    json = real_time_data(longitude, latitude)
    desc = json["result"]["comfort"]['desc']
    # print("人体感觉: " + desc)
    pm25 = json["result"]["pm25"]
    # print("PM2.5: " + str(pm25))
    weather = str(json["result"]["skycon"])
    temperature = str(json["result"]["temperature"])
    # print("天气: " + WeatherEnum[weather].value)
    wind = json["result"]["wind"]
    # print(wind)
    realtime_context = f'当前 人体感觉:{desc},温度:{temperature},雾霾值:{pm25},天气:{WeatherEnum[weather].value} '
    # print(realtime_context)
    # pprint(r.json())
    return realtime_context


def real_time_data(longitude, latitude):
    url = f'https://api.caiyunapp.com/v2/Kg47BflU7B5pPOGN/{longitude},{latitude}/realtime.json'
    r = requests.get(url)
    json = r.json()
    return json


def daily_temperature(json, weather_bean):
    description = json["result"]['hourly']["description"]
    temperature = json["result"]['hourly']["temperature"][:13]

    # 取出数据

    weather_bean.temperature_current = temperature[0]  # 现在温度
    weather_bean.temperature_next_moment = temperature[2]  # 2小时 后温度
    weather_bean.temperature_after_work = temperature[12]  # 12小时 后温度

    weather_bean.temperature_lowest_scop = temperature[0]  # 最低温度
    weather_bean.temperature_highest_scop = temperature[0]  # 最高温度

    temperature_buffer = ""
    temp_last = weather_bean.temperature_current["value"]

    temperature_upward_last = True
    index = 0
    for item in temperature:
        if item["value"] > weather_bean.temperature_highest_scop["value"]:
            weather_bean.temperature_highest_scop = item
        if item["value"] < weather_bean.temperature_lowest_scop["value"]:
            weather_bean.temperature_lowest_scop = item
        # print(str(int(item["value"])))

        last_date = datetime.datetime.strptime(item["datetime"], "%Y-%m-%d %H:%M")

        temperature_arrow = "↗" if item["value"] >= temp_last else "↘"

        temperature_upward_this = True
        if item["value"] >= temp_last:
            temperature_upward_this = True
        else:
            temperature_upward_this = False

        # temperature_buffer += str(last_date.hour) + "点(" + str(int(item["value"])) + temperature_arrow + ")  "
        # temp_last = item["value"]
        # 添加过滤条件
        if temperature_upward_last != temperature_upward_this or index == 0 or index == len(temperature) - 1:
            temperature_buffer += str(last_date.hour) + "点(" + str(int(item["value"])) + "度" + temperature_arrow + ")  "
            temp_last = item["value"]
        temperature_upward_last = temperature_upward_this
        index += 1

    # print(temperature_buffer)
    weather_bean.temperature_desc = temperature_buffer

    if weather_bean.temperature_highest_scop["value"] > 30:
        weather_bean.temperature_suggest += f'注意防晒,最高温{weather_bean.temperature_highest_scop["value"]}度. '

    if weather_bean.temperature_lowest_scop["value"] < 18:
        weather_bean.temperature_suggest += f'注意保暖,低温{weather_bean.temperature_lowest_scop["value"]}度. '
    return weather_bean


def daily_aqi(json, weather_bean):
    aqi_list = json["result"]['hourly']["aqi"][:12]
    aqi_max = aqi_list[0]
    for item in aqi_list:
        if item["value"] > aqi_max["value"]:
            aqi_max = item
    return_resultl = f'当日污染最大值为:{aqi_max["value"]}\n'
    weather_bean.aqi_max = aqi_max
    weather_bean.aqi_desc = return_resultl
    if weather_bean.aqi_max["value"] > 70:
        weather_bean.aqi_needmasks = True
        weather_bean.aqi_suggest = f'戴口罩;'
    return weather_bean


def daily_forest(longitude, latitude):
    json = forecast_data(longitude, latitude)
    weather_bean = WeatherBean()
    weather_bean = have_rain_detail(json, weather_bean)
    weather_bean = daily_temperature(json, weather_bean)
    weather_bean = daily_aqi(json, weather_bean)

    rain_have_desc = "有" if weather_bean.rain_have == True else "无"
    aqi_needmasks_desc = "戴" if weather_bean.aqi_needmasks == True else "否"
    result = f'雨({rain_have_desc}) 污染物({weather_bean.aqi_max["value"]})  温度:{weather_bean.temperature_desc}  \n' \
             f'建议: {weather_bean.get_suggest()}'
             # f'\n{weather_bean.rain_desc}'\

    print(result)

    return result


def rain_2h(json):
    precipitation_list = [0.0, 2.0, 1.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                          0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                          0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                          0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                          0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                          0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                          0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    precipitation_list = json["result"]['minutely']["precipitation_2h"]

    rain_list = []
    rain_total = 0.0
    index = 0
    first_rain_index = 0
    first_rain_flag = False
    for item in precipitation_list:
        index += 1
        if item > 0.05:
            if first_rain_flag == False:
                first_rain_index = index
                first_rain_flag = True

            rain_list.append({"value": item, "index": index})
            rain_total += item
    if len(rain_list) > 0:
        rain_average = rain_total / len(rain_list)
        result = f'异常天气!! \n{first_rain_index}分钟后有雨 两小时内下雨分钟数:{len(rain_list)}分钟 平均雨量 {rain_average}\n'
        print(result)
        return result
    return ""


def have_rain_detail(json, weather_bean):
    # 降雨量
    precipitation_list = [{'value': 1.0, 'datetime': '2018-09-18 14:00'},
                          {'value': 2.0, 'datetime': '2018-09-18 15:00'},
                          {'value': 0.0, 'datetime': '2018-09-18 16:00'},
                          {'value': 0.0, 'datetime': '2018-09-18 17:00'},
                          {'value': 0.0, 'datetime': '2018-09-18 18:00'},
                          {'value': 0.0, 'datetime': '2018-09-18 19:00'},
                          {'value': 0.0, 'datetime': '2018-09-18 20:00'},
                          {'value': 0.0, 'datetime': '2018-09-18 21:00'},
                          {'value': 3.0, 'datetime': '2018-09-18 22:00'},
                          {'value': 0.0, 'datetime': '2018-09-18 23:00'},
                          {'value': 0.0, 'datetime': '2018-09-19 00:00'},
                          {'value': 0.0, 'datetime': '2018-09-19 01:00'}]
    precipitation_list = json["result"]['hourly']["precipitation"][:12]

    # print(precipitation_list)

    # 有雨的时间 item
    rain_list = []
    rain_max = precipitation_list[0]
    for item in precipitation_list:
        if item['value'] > 0:
            rain_list.append(item)
        if item['value'] > rain_max['value']:
            rain_max = item
    if len(rain_list) > 0:
        rain_str = ""
        rain_total = 0.0
        for item in rain_list:
            rain_total += item["value"]
            rain_str += f'{item["datetime"]} 雨量:{item["value"]}\n'

        result = f'平均雨量:{rain_total/len(rain_list)},最大雨量:{rain_max["value"]} \n' \
                 f'{rain_str}\n \n'

        # print(result)
        weather_bean.rain_have = True
        weather_bean.rain_desc = result
        weather_bean.rain_suggest += "带伞;"
        return weather_bean
    else:
        weather_bean.rain_have = False
        weather_bean.rain_desc = ''
        return weather_bean


def forecast_data(longitude, latitude):
    url = f'https://api.caiyunapp.com/v2/Kg47BflU7B5pPOGN/{longitude},{latitude}/forecast.json'
    r = requests.get(url)
    json = r.json()
    return json


def rain_monitor(longitude, latitude):
    json = forecast_data(longitude, latitude)
    result = rain_2h(json)
    return result


if __name__ == '__main__':
    longitude = 116.298056  # 经度-何悦
    latitude = 39.959912  # 纬度
    # realtime(longitude, latitude)

    daily_forest(longitude, latitude)
    # rain_monitor(longitude, latitude)
