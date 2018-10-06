from __future__ import absolute_import

import uuid

from app.notice.mail import send_email
from app.weather.caiyun import daily_forest, have_rain_detail, rain_2h, forecast_data, \
    rain_monitor
from pytz import utc

from app.task.celeryapp import app

import time

from app.weather.weather_bean import WeatherBean
from app.task.celeryapp import app
from app.notice.mail import send_email

from app.weather.caiyun import daily_forest, have_rain_detail, rain_2h, forecast_data, \
    rain_monitor
from datetime import datetime
import pytz


def query_order_position():
    '''
    从数据库查数据出来 ,active=true
    :return:
    '''
    data_list = []
    for index in range(1):
        bean = WeatherBean()
        bean.active = True
        bean.email_receiver = "vipheyue@foxmail.com"
        bean.reminder_time = ["7:20", "18:00", "3:29"]
        # bean.reminder_time = ["15:12"]
        bean.longitude = 116.298056
        bean.latitude = 39.959912
        data_list.append(bean)
    return data_list


@app.task(autoretry_for=(Exception,), default_retry_delay=60 * 3, retry_kwargs={'max_retries': 5})
def interval_rain_monitor():
    '''
    对需要监控雨的用户,对雨进行每两小时一次的监控
    两小时有定时器来执行 ,每次从数据库查一次
    :return:
    '''
    data_list = query_order_position()
    for bean in data_list:
        if bean.active == True:
            # # 交给 celery 发邮件
            # result = send_email.apply_async((bean.email_receiver, "邮件测试: interval_rain_monitor -- " + time.asctime()))
            longitude = bean.longitude  # 经度-何悦
            latitude = bean.latitude  # 纬度
            result = rain_monitor(longitude, latitude)
            if result != '':
                send_email.apply_async((bean.email_receiver, result))


@app.task(autoretry_for=(Exception,), default_retry_delay=60 * 3, retry_kwargs={'max_retries': 5})
def dailyWeather():
    '''
    根据用户设定的时间,来发送天气提醒给用户
    :return:
    '''
    data_list = query_order_position()
    for bean in data_list:
        for user_send_time in bean.reminder_time:
            setting_dt = datetime.strptime(user_send_time, "%H:%M")
            local_dt = datetime.now()
            tz = pytz.timezone('Asia/Shanghai')
            send_dt = tz.localize(
                datetime(local_dt.year, local_dt.month, local_dt.day, setting_dt.hour, setting_dt.minute))
            # # 交给 celery 发邮件
            # result = send_email.apply_async((bean.email_receiver, "邮件测试: " + time.asctime()), eta=send_dt)
            longitude = bean.longitude  # 经度-何悦
            latitude = bean.latitude  # 纬度
            result = daily_forest(longitude, latitude)+"  \n "+time.asctime()
            send_email.apply_async((bean.email_receiver, result), eta=send_dt)


if __name__ == '__main__':
    # interval_rain_monitor()
    dailyWeather()
    # print(datetime.utcnow())
    # print(datetime.now())
    # from app.task.tasks import print_task
    # print_task.delay("----")
    # from app.notice.mail import send_email
    # print(send_email.name)
    # result = send_email.delay("vipheyue@foxmail.com", "邮件测试: 1  " + time.asctime())
