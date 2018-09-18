from pprint import pprint

import requests
from pip._internal.utils.deprecation import deprecated

from app.WeatherEnum import WeatherEnum


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





def daily_temperature(json):
    description = json["result"]['hourly']["description"]
    temperature = json["result"]['hourly']["temperature"][:8]

    moring_temperature_now = temperature[0]  # 现在温度
    moring_temperature_later = temperature[2]  # 3小时 后温度

    moring_temperature_clodest = temperature[0]  # 最低温度
    moring_temperature_hottest = temperature[0]  # 最高温度
    for item in temperature:
        if item["value"] > moring_temperature_hottest["value"]:
            moring_temperature_hottest = item
        if item["value"] < moring_temperature_clodest["value"]:
            moring_temperature_clodest = item

    st = moring_temperature_later["datetime"]
    # st = "2017-11-23 16:10:10"
    import datetime
    last_date = datetime.datetime.strptime(st, "%Y-%m-%d %H:%M")

    returnresult = f'当前:{description}\n' \
                   f'当前温度: {moring_temperature_now["value"]} ℃ \n' \
                   f'2小时后温度:{moring_temperature_later["value"]} ℃ \n' \
                   f'8小时内:{moring_temperature_clodest["value"]}~{moring_temperature_hottest["value"]} ℃ \n'

    # print(returnresult)
    return returnresult


def daily_aqi(json):
    aqi_list = json["result"]['hourly']["aqi"][:8]
    aqi_max = aqi_list[0]
    for item in aqi_list:
        if item["value"] > aqi_max["value"]:
            aqi_max = item
    return_resultl = f'当日污染最大值为:{aqi_max["value"]}\n'
    return return_resultl


def daily_forest(longitude, latitude):
    json = forecast_data(longitude, latitude)
    rain_result = have_rain_detail(json)
    temperature_result = daily_temperature(json)
    aqi_result = daily_aqi(json)

    result = rain_result + temperature_result + aqi_result
    print(result)

    return result


def rain_2h(json):
    precipitation_list = json["result"]['minutely']["precipitation_2h"]
    # precipitation_list = [0.0, 2.0, 1.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    #                       0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    #                       0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    #                       0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    #                       0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    #                       0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    #                       0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
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
        result = f'{first_rain_index}分钟后有雨 两小时内下雨分钟数:{len(rain_list)}分钟 平均雨量 {rain_average}\n'
        print(result)
        return result
    return ""


def have_rain_detail(json):
    # 降雨量
    precipitation_list = json["result"]['hourly']["precipitation"][:12]
    # precipitation_list = [{'value': 1.0, 'datetime': '2018-09-18 14:00'},
    #                       {'value': 2.0, 'datetime': '2018-09-18 15:00'},
    #                       {'value': 0.0, 'datetime': '2018-09-18 16:00'},
    #                       {'value': 0.0, 'datetime': '2018-09-18 17:00'},
    #                       {'value': 0.0, 'datetime': '2018-09-18 18:00'},
    #                       {'value': 0.0, 'datetime': '2018-09-18 19:00'},
    #                       {'value': 0.0, 'datetime': '2018-09-18 20:00'},
    #                       {'value': 0.0, 'datetime': '2018-09-18 21:00'},
    #                       {'value': 3.0, 'datetime': '2018-09-18 22:00'},
    #                       {'value': 0.0, 'datetime': '2018-09-18 23:00'},
    #                       {'value': 0.0, 'datetime': '2018-09-19 00:00'},
    #                       {'value': 0.0, 'datetime': '2018-09-19 01:00'}]
    print(precipitation_list)

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

        result = f'请带伞,平均雨量:{rain_total/len(rain_list)},最大雨量:{rain_max["value"]} \n' \
                 f'{rain_str}\n \n'
        return result
    else:
        return ''


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
    # interval_monitor(longitude, latitude)
