import schedule
import time
from app.notice.mail import send_email
from app.weather.caiyun import check_unuaual_weather, realtime

import logging
from app.log.log_manager import initLog
from app.log.test import testlog


def job():
    # 121.6544,25.1552

    # longitude = 116.298056  # 经度-何悦
    # latitude = 39.959912  # 纬度
    longitude = 121.6544  # 经度
    latitude = 25.1552  # 纬度
    # realtime(longitude, latitude)
    result = check_unuaual_weather(longitude, latitude)
    if result != '':
        # 发送邮件
        send_email("vipheyue@foxmail.com", result)


def dailyWeather():
    longitude = 116.298056  # 经度-何悦
    latitude = 39.959912  # 纬度
    result = realtime(longitude, latitude)
    send_email("vipheyue@foxmail.com", result)


def schedule_task():
    # schedule.every(2).seconds.do(job)
    schedule.every().day.at("7:30").do(job)
    schedule.every().day.at("22:30").do(job)

    schedule.every().day.at("7:30").do(dailyWeather)
    schedule.every().day.at("12:01").do(dailyWeather)
    schedule.every().day.at("18:00").do(dailyWeather)
    while True:
        schedule.run_pending()
        time.sleep(20)


def test():
    print(" test......")


def schedule_task_test():
    schedule.every(2).seconds.do(test)
    while True:
        schedule.run_pending()
        time.sleep(1)


logger = logging.getLogger('main.task')
if __name__ == '__main__':
    # initLog()
    # logger.info("xcxcxc")
    # testlog()

    # schedule_task()
    schedule_task_test()
